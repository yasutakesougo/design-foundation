#!/usr/bin/env python3
"""IMAGE-FIRST monoline raster -> normalized SVG centerline.

Modes: polyline (PR #88 baseline), bezier-fit, spline-bezier.
Local deps only: Pillow, NumPy, scikit-image.
"""
from __future__ import annotations
import argparse, json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence
import numpy as np
from PIL import Image
from skimage.morphology import skeletonize

Point=tuple[int,int]; Vec=np.ndarray
N8=[(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
@dataclass(frozen=True)
class Cubic: p0:Vec; p1:Vec; p2:Vec; p3:Vec

def semantic_stroke_mask(image:Image.Image,mode="auto",min_green=70,dominance=18,dark_threshold=180):
    a=np.asarray(image.convert("RGB"),dtype=np.int32); r,g,b=a[...,0],a[...,1],a[...,2]
    green=(g>=min_green)&(g-r>=dominance)&(g-b>=dominance)
    dark=(299*r+587*g+114*b)/1000.0<=dark_threshold
    if mode=="green": return green
    if mode=="dark": return dark
    if mode=="auto": return green|dark
    raise ValueError(mode)

def build_graph(skel):
    ys,xs=np.nonzero(skel); nodes={(int(x),int(y)) for x,y in zip(xs,ys)}
    graph={p:[(p[0]+dx,p[1]+dy) for dx,dy in N8 if (p[0]+dx,p[1]+dy) in nodes] for p in nodes}
    return nodes,graph

def edge(a,b): return (a,b) if a<=b else (b,a)

def trace_polylines(skel):
    nodes,graph=build_graph(skel)
    if not nodes:return []
    seen=set(); out=[]
    def walk(a,b):
        path=[a,b]; seen.add(edge(a,b)); prev,cur=a,b
        while len(graph[cur])==2:
            q=[x for x in graph[cur] if x!=prev][0]; e=edge(cur,q)
            if e in seen:break
            path.append(q);seen.add(e);prev,cur=cur,q
        return path
    for p in sorted(x for x in nodes if len(graph[x])!=2):
        for q in sorted(graph[p]):
            if edge(p,q) not in seen:out.append(walk(p,q))
    for p in sorted(nodes):
        for q in sorted(graph[p]):
            if edge(p,q) in seen:continue
            path=[p,q];seen.add(edge(p,q));prev,cur=p,q
            while True:
                cand=[x for x in graph[cur] if x!=prev]
                if not cand:break
                nxt=cand[0];e=edge(cur,nxt)
                if e in seen:break
                path.append(nxt);seen.add(e);prev,cur=cur,nxt
            out.append(path)
    return out

def _perp(p,a,b):
    if a==b:return float(np.hypot(p[0]-a[0],p[1]-a[1]))
    ax,ay=a;bx,by=b;px,py=p
    return abs((by-ay)*px-(bx-ax)*py+bx*ay-by*ax)/float(np.hypot(by-ay,bx-ax))

def rdp(points,eps):
    if len(points)<=2:return points
    ds=[_perp(p,points[0],points[-1]) for p in points[1:-1]]
    if not ds or max(ds)<=eps:return [points[0],points[-1]]
    i=int(np.argmax(ds))+1
    return rdp(points[:i+1],eps)[:-1]+rdp(points[i:],eps)

def path_length(p:Sequence):
    return sum(float(np.linalg.norm(np.asarray(b,float)-np.asarray(a,float))) for a,b in zip(p,p[1:]))

def remove_short(paths:Iterable[list[Point]],minimum):return [p for p in paths if len(p)>=2 and path_length(p)>=minimum]

def unit(v):
    n=float(np.linalg.norm(v));return v/n if n>1e-9 else np.zeros(2)

def chord_u(p):
    if len(p)<=1:return np.zeros(len(p))
    d=np.linalg.norm(np.diff(p,axis=0),axis=1);t=float(d.sum())
    return np.r_[0.0,np.cumsum(d)/t] if t>1e-9 else np.linspace(0,1,len(p))

def eval_cubic(c,t):
    t=np.asarray(t,float);o=1-t
    if t.ndim==0:return o**3*c.p0+3*o**2*t*c.p1+3*o*t**2*c.p2+t**3*c.p3
    return o[:,None]**3*c.p0+3*o[:,None]**2*t[:,None]*c.p1+3*o[:,None]*t[:,None]**2*c.p2+t[:,None]**3*c.p3

def fit_one(p,t0=None,t1=None):
    p0,p3=p[0],p[-1];t0=unit(p[1]-p0) if t0 is None else t0;t1=unit(p[-2]-p3) if t1 is None else t1
    if not np.any(t0):t0=unit(p3-p0)
    if not np.any(t1):t1=unit(p0-p3)
    chord=float(np.linalg.norm(p3-p0));fallback=max(chord/3,1e-3)
    if len(p)==2:return Cubic(p0,p0+fallback*t0,p3+fallback*t1,p3)
    u=chord_u(p);o=1-u;b0=o**3;b1=3*u*o**2;b2=3*u**2*o;b3=u**3
    base=(b0+b1)[:,None]*p0+(b2+b3)[:,None]*p3;rhs=p-base;a1=b1[:,None]*t0;a2=b2[:,None]*t1
    c00=float((a1*a1).sum());c01=float((a1*a2).sum());c11=float((a2*a2).sum());x0=float((a1*rhs).sum());x1=float((a2*rhs).sum());det=c00*c11-c01*c01
    if abs(det)<=1e-12:a0=a_1=fallback
    else:
        a0=(x0*c11-x1*c01)/det;a_1=(c00*x1-c01*x0)/det;limit=max(chord*1.5,fallback)
        if a0<=1e-3 or a0>limit:a0=fallback
        if a_1<=1e-3 or a_1>limit:a_1=fallback
    return Cubic(p0,p0+a0*t0,p3+a_1*t1,p3)

def max_error(p,c):
    e=np.linalg.norm(eval_cubic(c,chord_u(p))-p,axis=1)
    if len(e)<=2:return 0.0,max(1,len(p)//2)
    i=int(np.argmax(e[1:-1]))+1;return float(e[i]),i

def fit_beziers(points,max_err,max_depth=12):
    a=np.asarray(points,float)
    if len(a)<2:return []
    def rec(seg,t0,t1,depth):
        c=fit_one(seg,t0,t1);err,i=max_error(seg,c)
        if err<=max_err or len(seg)<=3 or depth>=max_depth:return [c]
        if len(seg)>=6:i=min(max(i,2),len(seg)-3)
        if i<=0 or i>=len(seg)-1:return [c]
        back=unit(seg[i-1]-seg[i+1]);back=back if np.any(back) else unit(seg[i-1]-seg[i])
        return rec(seg[:i+1],t0,back,depth+1)+rec(seg[i:],-back,t1,depth+1)
    return rec(a,unit(a[1]-a[0]),unit(a[-2]-a[-1]),0)

def smooth_points(points,passes,weight):
    a=np.asarray(points,float).copy();w=min(max(weight,0),.49)
    for _ in range(max(0,passes)):
        old=a.copy();a[1:-1]=(1-2*w)*old[1:-1]+w*(old[:-2]+old[2:]);a[0]=old[0];a[-1]=old[-1]
    return a

def spline_beziers(points,eps,passes,weight,tension):
    a=smooth_points(points,passes,weight);knots=np.asarray(rdp([(int(round(x)),int(round(y))) for x,y in a],eps),float)
    if len(knots)<2:return []
    if len(knots)==2:
        d=(knots[1]-knots[0])/3;return [Cubic(knots[0],knots[0]+d,knots[1]-d,knots[1])]
    t=np.zeros_like(knots);t[0]=tension*(knots[1]-knots[0]);t[-1]=tension*(knots[-1]-knots[-2]);t[1:-1]=tension*.5*(knots[2:]-knots[:-2])
    out=[]
    for i in range(len(knots)-1):
        p0,p3=knots[i],knots[i+1];ch=float(np.linalg.norm(p3-p0))
        if ch<=1e-9:continue
        h0,h1=t[i]/3,t[i+1]/3;limit=.45*ch
        n0,n1=float(np.linalg.norm(h0)),float(np.linalg.norm(h1))
        if n0>limit:h0*=limit/n0
        if n1>limit:h1*=limit/n1
        out.append(Cubic(p0,p0+h0,p3-h1,p3))
    return out

def sample_cubics(cs,steps=16):
    out=[]
    for i,c in enumerate(cs):
        p=eval_cubic(c,np.linspace(0,1,steps));out.append(p if i==0 else p[1:])
    return np.vstack(out) if out else np.empty((0,2))

def sample_polyline(points,step=.75):
    a=np.asarray(points,float);out=[]
    for i,(p,q) in enumerate(zip(a,a[1:])):
        n=max(2,int(np.ceil(np.linalg.norm(q-p)/step))+1);t=np.linspace(0,1,n)[:,None];s=p*(1-t)+q*t;out.append(s if i==0 else s[1:])
    return np.vstack(out) if out else a

def deviation(raw,samples):
    a=np.asarray(raw,float)
    if not len(a) or not len(samples):return []
    return np.min(np.linalg.norm(a[:,None,:]-samples[None,:,:],axis=2),axis=1).tolist()

def fmt(v):
    r=round(float(v),2);return str(int(r)) if r.is_integer() else f"{r:.2f}".rstrip("0").rstrip(".")

def mapped(p,s,ox,oy):
    p=np.asarray(p,float);return np.array([ox+p[0]*s,oy+p[1]*s])

def svg_for(paths,width,height,*,viewbox=512,stroke_width=8,curve_mode="polyline",epsilon=1.35,bezier_error=1.35,linear_short=12,smooth_passes=2,smooth_weight=.18,spline_tension=.7):
    s=min(viewbox/width,viewbox/height);ox=(viewbox-width*s)/2;oy=(viewbox-height*s)/2;elems=[];lc=cc=0;dev=[]
    for raw in paths:
        if curve_mode=="polyline" or path_length(raw)<=linear_short:
            src=rdp(raw,epsilon) if curve_mode=="polyline" else [raw[0],raw[-1]];pts=[mapped(p,s,ox,oy) for p in src];d=f"M {fmt(pts[0][0])} {fmt(pts[0][1])}"
            for p in pts[1:]:d+=f" L {fmt(p[0])} {fmt(p[1])}";lc+=1
            dev+=deviation(raw,sample_polyline(src))
        else:
            if curve_mode=="bezier-fit":cs=fit_beziers(raw,bezier_error)
            elif curve_mode=="spline-bezier":cs=spline_beziers(raw,epsilon,smooth_passes,smooth_weight,spline_tension)
            else:raise ValueError(curve_mode)
            if not cs:continue
            p=mapped(cs[0].p0,s,ox,oy);d=f"M {fmt(p[0])} {fmt(p[1])}"
            for c in cs:
                p1,p2,p3=[mapped(x,s,ox,oy) for x in (c.p1,c.p2,c.p3)];d+=f" C {fmt(p1[0])} {fmt(p1[1])} {fmt(p2[0])} {fmt(p2[1])} {fmt(p3[0])} {fmt(p3[1])}";cc+=1
            dev+=deviation(raw,sample_cubics(cs))
        elems.append(f'    <path d="{d}"/>')
    body="\n".join(elems);svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {viewbox} {viewbox}">\n  <g fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round">\n{body}\n  </g>\n</svg>\n'
    m={"curve_mode":curve_mode,"path_count":len(elems),"L_count":lc,"C_count":cc,"segment_count":lc+cc,"control_point_count":cc*2,"bezier_error_bound_source_px":bezier_error if curve_mode=="bezier-fit" else 0.0,"centerline_deviation_mean_source_px":round(float(np.mean(dev)),4) if dev else 0.0,"centerline_deviation_max_source_px":round(float(np.max(dev)),4) if dev else 0.0}
    return svg,m

def main():
    p=argparse.ArgumentParser();p.add_argument("input",type=Path);p.add_argument("output",type=Path);p.add_argument("--curve-mode",choices=("polyline","bezier-fit","spline-bezier"),default="polyline");p.add_argument("--mask-mode",choices=("auto","green","dark"),default="auto");p.add_argument("--min-green",type=int,default=70);p.add_argument("--dominance",type=int,default=18);p.add_argument("--dark-threshold",type=int,default=180);p.add_argument("--epsilon",type=float,default=1.35);p.add_argument("--min-path",type=float,default=4.0);p.add_argument("--linear-short",type=float,default=12.0);p.add_argument("--bezier-error",type=float,default=1.35);p.add_argument("--smooth-passes",type=int,default=2);p.add_argument("--smooth-weight",type=float,default=.18);p.add_argument("--spline-tension",type=float,default=.7);p.add_argument("--stroke-width",type=int,default=8);p.add_argument("--metrics",type=Path);a=p.parse_args()
    im=Image.open(a.input);mask=semantic_stroke_mask(im,a.mask_mode,a.min_green,a.dominance,a.dark_threshold)
    if not mask.any():raise SystemExit("no semantic stroke pixels found")
    sk=skeletonize(mask);_,graph=build_graph(sk);paths=remove_short(trace_polylines(sk),a.min_path)
    svg,m=svg_for(paths,im.width,im.height,stroke_width=a.stroke_width,curve_mode=a.curve_mode,epsilon=a.epsilon,bezier_error=a.bezier_error,linear_short=a.linear_short,smooth_passes=a.smooth_passes,smooth_weight=a.smooth_weight,spline_tension=a.spline_tension)
    m.update(source_path_count=len(paths),junction_node_count=sum(len(x)>2 for x in graph.values()),endpoint_node_count=sum(len(x)==1 for x in graph.values()),source_width=im.width,source_height=im.height)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(svg,encoding="utf-8")
    if a.metrics:a.metrics.parent.mkdir(parents=True,exist_ok=True);a.metrics.write_text(json.dumps(m,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(" ".join(f"{k}={v}" for k,v in m.items()));return 0
if __name__=="__main__":raise SystemExit(main())
