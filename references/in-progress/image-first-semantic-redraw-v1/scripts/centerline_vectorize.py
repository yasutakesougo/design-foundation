#!/usr/bin/env python3
"""IMAGE-FIRST monoline raster -> normalized SVG centerline.

Modes: polyline, bezier-fit, spline-bezier, scale-aware-spline,
curvature-aware-spline, curvature-aware-join, curvature-aware-source-guided.
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

def resample_uniform(points, step=1.0):
    """Arc-length resample a traced topology span without moving endpoints."""
    a=np.asarray(points,float)
    if len(a)<2:return a
    d=np.linalg.norm(np.diff(a,axis=0),axis=1); arc=np.r_[0.0,np.cumsum(d)]; total=float(arc[-1])
    if total<=1e-9:return a[[0,-1]]
    n=max(2,int(np.ceil(total/step))+1); q=np.linspace(0,total,n)
    return np.c_[np.interp(q,arc,a[:,0]),np.interp(q,arc,a[:,1])]

def local_poly_smooth(points,radius=8,*,adaptive=False,min_radius=5,max_radius=13):
    """Local quadratic smoothing that preserves broad curvature better than averaging."""
    a=np.asarray(points,float);n=len(a)
    if n<5:return a.copy()
    broad=np.zeros(n);coarse=np.empty_like(a);rr=max_radius
    for i in range(n):
        lo=max(0,i-rr);hi=min(n,i+rr+1);x=np.arange(lo,hi)-i;deg=min(2,len(x)-1)
        if deg<1:coarse[i]=a[i];continue
        for axis in range(2):coarse[i,axis]=np.polyval(np.polyfit(x,a[lo:hi,axis],deg),0)
    w=max(3,min_radius)
    for i in range(w,n-w):
        v0=coarse[i]-coarse[i-w];v1=coarse[i+w]-coarse[i];n0=np.linalg.norm(v0);n1=np.linalg.norm(v1)
        if n0>1e-9 and n1>1e-9:
            ang=np.arctan2(v0[0]*v1[1]-v0[1]*v1[0],np.dot(v0,v1));broad[i]=abs(float(ang))/(n0+n1)
    nz=broad[broad>0];scale=max(float(np.percentile(nz,75)) if len(nz) else .01,1e-4)
    out=np.empty_like(a)
    for i in range(n):
        if i in (0,n-1):out[i]=a[i];continue
        if adaptive:
            strength=min(1.0,broad[i]/(2.0*scale));r=int(round(max_radius-(max_radius-min_radius)*strength))
        else:r=radius
        r=min(r,i,n-1-i)
        if r<2:out[i]=a[i];continue
        lo=i-r;hi=i+r+1;x=np.arange(lo,hi)-i;deg=min(2,len(x)-1)
        for axis in range(2):out[i,axis]=np.polyval(np.polyfit(x,a[lo:hi,axis],deg),0)
    out[0]=a[0];out[-1]=a[-1];return out

def signed_curvature(points,window=10):
    p=np.asarray(points,float);k=np.zeros(len(p))
    for i in range(window,len(p)-window):
        a=p[i]-p[i-window];b=p[i+window]-p[i];la=np.linalg.norm(a);lb=np.linalg.norm(b)
        if la>1e-9 and lb>1e-9:
            k[i]=float(np.arctan2(a[0]*b[1]-a[1]*b[0],np.dot(a,b)))/(la+lb)
    return k

def rdp_indices(points,eps):
    a=np.asarray(points,float)
    def dist(p,x,y):
        d=y-x;n=float(np.linalg.norm(d))
        if n<=1e-9:return float(np.linalg.norm(p-x))
        return abs(float(d[1]*p[0]-d[0]*p[1]+y[0]*x[1]-y[1]*x[0]))/n
    def rec(lo,hi):
        if hi<=lo+1:return [lo,hi]
        ds=[dist(a[i],a[lo],a[hi]) for i in range(lo+1,hi)]
        if not ds or max(ds)<=eps:return [lo,hi]
        j=lo+1+int(np.argmax(ds));return rec(lo,j)[:-1]+rec(j,hi)
    return rec(0,len(a)-1)

def ensure_max_gap(indices,max_gap):
    out=[indices[0]]
    for a,b in zip(indices,indices[1:]):
        gap=b-a
        if gap>max_gap:
            parts=int(np.ceil(gap/max_gap))
            for q in range(1,parts):out.append(round(a+gap*q/parts))
        out.append(b)
    return sorted(set(out))

def prune_spacing(indices,min_spacing,protected=None):
    protected=set(protected or ());out=[indices[0]]
    for i in indices[1:-1]:
        if i-out[-1]<min_spacing:
            if i in protected and out[-1] not in protected:out[-1]=i
        else:out.append(i)
    if indices[-1]-out[-1]<min_spacing and len(out)>1:out[-1]=indices[-1]
    else:out.append(indices[-1])
    return sorted(set(out))

def hermite_from_reference(reference,knot_indices,tangent_window,tension):
    ref=np.asarray(reference,float);ids=np.asarray(knot_indices,int);pts=ref[ids]
    if len(pts)<2:return []
    tang=[]
    for i in ids:
        lo=max(0,i-tangent_window);hi=min(len(ref)-1,i+tangent_window);v=ref[hi]-ref[lo]
        if i==0:v=ref[hi]-ref[0]
        elif i==len(ref)-1:v=ref[-1]-ref[lo]
        tang.append(unit(v))
    out=[]
    for j in range(len(pts)-1):
        p0,p3=pts[j],pts[j+1];ch=float(np.linalg.norm(p3-p0))
        if ch<=1e-9:continue
        prev=float(np.linalg.norm(pts[j]-pts[j-1])) if j>0 else ch
        nxt=float(np.linalg.norm(pts[j+2]-pts[j+1])) if j+2<len(pts) else ch
        h0=tang[j]*min(.36*ch*tension,.22*(prev+ch)*tension);h1=tang[j+1]*min(.36*ch*tension,.22*(ch+nxt)*tension)
        n0,n1=float(np.linalg.norm(h0)),float(np.linalg.norm(h1));limit=.42*ch
        if n0>limit:h0*=limit/n0
        if n1>limit:h1*=limit/n1
        out.append(Cubic(p0,p0+h0,p3-h1,p3))
    return out

def scale_aware_beziers(points,eps=1.05,min_radius=4,max_radius=10,min_spacing=9,max_gap=30,tangent_window=8,tension=.98):
    """Adaptive local-polynomial smoothing; preserve gradual shape changes without micro-wave."""
    ref=local_poly_smooth(resample_uniform(points,1.0),adaptive=True,min_radius=min_radius,max_radius=max_radius)
    ids=ensure_max_gap(rdp_indices(ref,eps),max_gap);ids=prune_spacing(ids,min_spacing,{0,len(ref)-1})
    return hermite_from_reference(ref,ids,tangent_window,tension)

def curvature_aware_geometry(points,eps=1.15,radius=7,curvature_window=10,min_spacing=12,max_gap=34,quantile=.50,tangent_window=9,tension=.98):
    """Return low-frequency reference, retained knot indices, and baseline curvature-aware cubics."""
    ref=local_poly_smooth(resample_uniform(points,1.0),radius=radius,adaptive=False,min_radius=5,max_radius=max(13,radius))
    n=len(ref);base=set(rdp_indices(ref,eps));k=signed_curvature(ref,curvature_window);mag=np.abs(k)
    valid=mag[curvature_window:n-curvature_window];positive=valid[valid>1e-6];threshold=float(np.quantile(positive,quantile)) if len(positive) else 0.0
    candidates=[]
    for i in range(curvature_window+2,n-curvature_window-2):
        if mag[i]>=threshold and mag[i]>=max(mag[i-2:i],default=0) and mag[i]>=max(mag[i+1:i+3],default=0):candidates.append((float(mag[i]),i))
        if k[i-3]*k[i+3]<0 and max(abs(k[i-3]),abs(k[i+3]))>max(threshold*.5,2e-4):candidates.append((float(max(abs(k[i-3]),abs(k[i+3]))),i))
    selected=[]
    for _,i in sorted(candidates,reverse=True):
        if all(abs(i-j)>=min_spacing for j in selected):selected.append(i)
    ids=ensure_max_gap(sorted(base|set(selected)),max_gap);ids=prune_spacing(ids,min_spacing,set(selected)|{0,n-1})
    return ref,ids,hermite_from_reference(ref,ids,tangent_window,tension)

def curvature_aware_beziers(points,eps=1.15,radius=7,curvature_window=10,min_spacing=12,max_gap=34,quantile=.50,tangent_window=9,tension=.98):
    """Retain low-frequency curvature transitions while rejecting short-period knot noise."""
    return curvature_aware_geometry(points,eps,radius,curvature_window,min_spacing,max_gap,quantile,tangent_window,tension)[2]

def _cross2(a,b): return float(a[0]*b[1]-a[1]*b[0])

def cubic_curvature_start(c):
    d=3.0*(c.p1-c.p0);dd=6.0*(c.p0-2.0*c.p1+c.p2);den=float(np.linalg.norm(d))**3
    return _cross2(d,dd)/den if den>1e-12 else 0.0

def cubic_curvature_end(c):
    d=3.0*(c.p3-c.p2);dd=6.0*(c.p3-2.0*c.p2+c.p1);den=float(np.linalg.norm(d))**3
    return _cross2(d,dd)/den if den>1e-12 else 0.0

def _replace_join_handles(left,right,left_length,right_length):
    p=left.p3;incoming=unit(p-left.p2);outgoing=unit(right.p1-p)
    return Cubic(left.p0,left.p1,p-left_length*incoming,p),Cubic(p,p+right_length*outgoing,right.p2,right.p3)

def refine_join_curvature_continuity(cubics,*,max_scale=.18,min_curvature=2e-4,min_relative_jump=.10):
    """Locally reduce curvature handoff while preserving knots and tangent directions.

    At a same-sign cubic join, curvature is inversely proportional to the square of
    the adjacent handle length when tangent direction and the opposite handle are
    fixed. Apply the minimum log-scale pair that moves both sides toward equal
    curvature, with a narrow bound so broad SOURCE geometry cannot be rewritten.
    """
    out=list(cubics);lo,hi=1.0-max_scale,1.0+max_scale
    for j in range(len(out)-1):
        left,right=out[j],out[j+1];p=left.p3
        kl,kr=cubic_curvature_end(left),cubic_curvature_start(right)
        if kl*kr<=0 or min(abs(kl),abs(kr))<min_curvature:continue
        rel=abs(kl-kr)/(abs(kl)+abs(kr)+1e-12)
        if rel<min_relative_jump:continue
        ratio=np.sqrt(abs(kr/kl));s_left=float(np.clip(1.0/np.sqrt(ratio),lo,hi));s_right=float(np.clip(np.sqrt(ratio),lo,hi))
        hl=float(np.linalg.norm(p-left.p2))*s_left;hr=float(np.linalg.norm(right.p1-p))*s_right
        out[j],out[j+1]=_replace_join_handles(left,right,hl,hr)
    return out

def _three_point_curvature(reference,index,window=9):
    """Signed low-frequency curvature estimate using a wide three-point neighborhood."""
    ref=np.asarray(reference,float);a=ref[max(0,index-window)];b=ref[index];c=ref[min(len(ref)-1,index+window)]
    ab=b-a;bc=c-b;ac=c-a;den=float(np.linalg.norm(ab)*np.linalg.norm(bc)*np.linalg.norm(ac))
    return 2.0*_cross2(ab,bc)/den if den>1e-12 else 0.0

def refine_source_guided_handles(reference,knot_indices,cubics,*,max_scale=.18,blend=.85,target_window=9,min_curvature=2e-4,min_relative_error=.10):
    """Locally tune join handles toward SOURCE low-frequency curvature.

    Knot positions and tangent directions are fixed. Only the two handle magnitudes
    adjacent to a long-contour join may move, and each move is bounded. Near
    inflections or sign disagreement, the join is left untouched to avoid forcing a
    generic arc through SOURCE-specific transitions.
    """
    ref=np.asarray(reference,float);ids=np.asarray(knot_indices,int);out=list(cubics);lo,hi=1.0-max_scale,1.0+max_scale
    for j in range(len(out)-1):
        left,right=out[j],out[j+1];p=left.p3;target=_three_point_curvature(ref,int(ids[j+1]),target_window)
        if abs(target)<min_curvature:continue
        kl,kr=cubic_curvature_end(left),cubic_curvature_start(right)
        hl0=float(np.linalg.norm(p-left.p2));hr0=float(np.linalg.norm(right.p1-p))
        def scale(current):
            if current*target<=0 or abs(current)<min_curvature:return 1.0
            rel=abs(current-target)/(abs(current)+abs(target)+1e-12)
            if rel<min_relative_error:return 1.0
            raw=np.sqrt(abs(current/target));return float(np.clip(1.0+blend*(raw-1.0),lo,hi))
        out[j],out[j+1]=_replace_join_handles(left,right,hl0*scale(kl),hr0*scale(kr))
    return out

def correction3_primary_contour(points,width,height,minimum_long_path=80.0,max_centroid_y=.62,min_vertical_span=.07,min_horizontal_span=.14):
    """Conservative geometry gate for the locked long upper/head contours.

    Correction-3 is not a global smoother. The gate excludes lower shoulders, props,
    and hand/notebook strokes in the portrait fixtures while retaining broad crown,
    temple, cheek/jaw, face-side, and outer-hair spans. Ratios keep the rule scale-aware.
    """
    a=np.asarray(points,float)
    if len(a)<2 or path_length(points)<minimum_long_path:return False
    if float(np.mean(a[:,1]))>max_centroid_y*height:return False
    yspan=float(np.ptp(a[:,1]))/max(float(height),1.0);xspan=float(np.ptp(a[:,0]))/max(float(width),1.0)
    return yspan>=min_vertical_span or xspan>=min_horizontal_span

def curvature_aware_join_beziers(points,enable_refinement=True):
    ref,ids,cubics=curvature_aware_geometry(points)
    if not enable_refinement:return cubics
    return refine_join_curvature_continuity(cubics)

def curvature_aware_source_guided_beziers(points,enable_refinement=True):
    ref,ids,cubics=curvature_aware_geometry(points)
    if not enable_refinement:return cubics
    return refine_source_guided_handles(ref,ids,cubics)

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
    s=min(viewbox/width,viewbox/height);ox=(viewbox-width*s)/2;oy=(viewbox-height*s)/2;elems=[];lc=cc=0;dev=[];refined_indices=[]
    for path_index,raw in enumerate(paths):
        if curve_mode=="polyline" or path_length(raw)<=linear_short:
            src=rdp(raw,epsilon) if curve_mode=="polyline" else [raw[0],raw[-1]];pts=[mapped(p,s,ox,oy) for p in src];d=f"M {fmt(pts[0][0])} {fmt(pts[0][1])}"
            for p in pts[1:]:d+=f" L {fmt(p[0])} {fmt(p[1])}";lc+=1
            dev+=deviation(raw,sample_polyline(src))
        else:
            if curve_mode=="bezier-fit":cs=fit_beziers(raw,bezier_error)
            elif curve_mode=="spline-bezier":cs=spline_beziers(raw,epsilon,smooth_passes,smooth_weight,spline_tension)
            elif curve_mode=="scale-aware-spline":cs=scale_aware_beziers(raw)
            elif curve_mode=="curvature-aware-spline":cs=curvature_aware_beziers(raw)
            elif curve_mode=="curvature-aware-join":
                eligible=correction3_primary_contour(raw,width,height);cs=curvature_aware_join_beziers(raw,eligible)
                if eligible:refined_indices.append(path_index)
            elif curve_mode=="curvature-aware-source-guided":
                eligible=correction3_primary_contour(raw,width,height);cs=curvature_aware_source_guided_beziers(raw,eligible)
                if eligible:refined_indices.append(path_index)
            else:raise ValueError(curve_mode)
            if not cs:continue
            p=mapped(cs[0].p0,s,ox,oy);d=f"M {fmt(p[0])} {fmt(p[1])}"
            for c in cs:
                p1,p2,p3=[mapped(x,s,ox,oy) for x in (c.p1,c.p2,c.p3)];d+=f" C {fmt(p1[0])} {fmt(p1[1])} {fmt(p2[0])} {fmt(p2[1])} {fmt(p3[0])} {fmt(p3[1])}";cc+=1
            dev+=deviation(raw,sample_cubics(cs))
        elems.append(f'    <path d="{d}"/>')
    body="\n".join(elems);svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {viewbox} {viewbox}">\n  <g fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round">\n{body}\n  </g>\n</svg>\n'
    m={"curve_mode":curve_mode,"path_count":len(elems),"L_count":lc,"C_count":cc,"segment_count":lc+cc,"control_point_count":cc*2,"bezier_error_bound_source_px":bezier_error if curve_mode=="bezier-fit" else 0.0,"centerline_deviation_mean_source_px":round(float(np.mean(dev)),4) if dev else 0.0,"centerline_deviation_max_source_px":round(float(np.max(dev)),4) if dev else 0.0,"correction3_refined_path_count":len(refined_indices),"correction3_refined_path_indices":refined_indices}
    return svg,m

def main():
    p=argparse.ArgumentParser();p.add_argument("input",type=Path);p.add_argument("output",type=Path);p.add_argument("--curve-mode",choices=("polyline","bezier-fit","spline-bezier","scale-aware-spline","curvature-aware-spline","curvature-aware-join","curvature-aware-source-guided"),default="polyline");p.add_argument("--mask-mode",choices=("auto","green","dark"),default="auto");p.add_argument("--min-green",type=int,default=70);p.add_argument("--dominance",type=int,default=18);p.add_argument("--dark-threshold",type=int,default=180);p.add_argument("--epsilon",type=float,default=1.35);p.add_argument("--min-path",type=float,default=4.0);p.add_argument("--linear-short",type=float,default=12.0);p.add_argument("--bezier-error",type=float,default=1.35);p.add_argument("--smooth-passes",type=int,default=2);p.add_argument("--smooth-weight",type=float,default=.18);p.add_argument("--spline-tension",type=float,default=.7);p.add_argument("--stroke-width",type=int,default=8);p.add_argument("--metrics",type=Path);a=p.parse_args()
    im=Image.open(a.input);mask=semantic_stroke_mask(im,a.mask_mode,a.min_green,a.dominance,a.dark_threshold)
    if not mask.any():raise SystemExit("no semantic stroke pixels found")
    sk=skeletonize(mask);_,graph=build_graph(sk);paths=remove_short(trace_polylines(sk),a.min_path)
    svg,m=svg_for(paths,im.width,im.height,stroke_width=a.stroke_width,curve_mode=a.curve_mode,epsilon=a.epsilon,bezier_error=a.bezier_error,linear_short=a.linear_short,smooth_passes=a.smooth_passes,smooth_weight=a.smooth_weight,spline_tension=a.spline_tension)
    m.update(source_path_count=len(paths),junction_node_count=sum(len(x)>2 for x in graph.values()),endpoint_node_count=sum(len(x)==1 for x in graph.values()),source_width=im.width,source_height=im.height)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(svg,encoding="utf-8")
    if a.metrics:a.metrics.parent.mkdir(parents=True,exist_ok=True);a.metrics.write_text(json.dumps(m,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(" ".join(f"{k}={v}" for k,v in m.items()));return 0
if __name__=="__main__":raise SystemExit(main())
