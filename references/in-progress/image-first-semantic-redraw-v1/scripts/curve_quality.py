#!/usr/bin/env python3
"""Static curve-quality metrics and optional magnified render helper.

This evaluator is intentionally narrow: it understands normalized SVG paths emitted
by centerline_vectorize.py (`M`, `L`, `C`). It does not decide Human acceptance.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np

TOKEN_RE = re.compile(r"[MLC]|[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?")


def _unit(v: np.ndarray) -> np.ndarray:
    n = float(np.linalg.norm(v))
    return v / n if n > 1e-9 else np.zeros(2, dtype=float)


def _angle_deg(a: np.ndarray, b: np.ndarray) -> float:
    ua, ub = _unit(a), _unit(b)
    if not np.any(ua) or not np.any(ub):
        return 0.0
    dot = float(np.clip(np.dot(ua, ub), -1.0, 1.0))
    return math.degrees(math.acos(dot))


def parse_segments(d: str):
    tokens = TOKEN_RE.findall(d)
    i = 0
    cur = np.zeros(2, dtype=float)
    start = None
    segments = []
    while i < len(tokens):
        cmd = tokens[i]
        i += 1
        if cmd == "M":
            cur = np.array([float(tokens[i]), float(tokens[i + 1])]); i += 2
            if start is None:
                start = cur.copy()
        elif cmd == "L":
            end = np.array([float(tokens[i]), float(tokens[i + 1])]); i += 2
            segments.append(("L", (cur.copy(), end.copy())))
            cur = end
        elif cmd == "C":
            p1 = np.array([float(tokens[i]), float(tokens[i + 1])]); i += 2
            p2 = np.array([float(tokens[i]), float(tokens[i + 1])]); i += 2
            end = np.array([float(tokens[i]), float(tokens[i + 1])]); i += 2
            segments.append(("C", (cur.copy(), p1, p2, end.copy())))
            cur = end
        else:
            raise ValueError(f"unsupported SVG path token: {cmd}")
    if start is None:
        start = cur.copy()
    return segments, start, cur


def path_tangent_metrics(segments):
    angles = []
    for prev, nxt in zip(segments, segments[1:]):
        a = prev[1][1] - prev[1][0] if prev[0] == "L" else prev[1][3] - prev[1][2]
        b = nxt[1][1] - nxt[1][0]
        angles.append(_angle_deg(a, b))
    return angles


def svg_metrics(path: Path):
    root = ET.parse(path).getroot()
    paths = [e for e in root.iter() if e.tag.rsplit("}", 1)[-1] == "path"]
    l_count = c_count = 0
    angles = []
    endpoints = []
    for e in paths:
        segs, start, end = parse_segments(e.attrib.get("d", ""))
        l_count += sum(1 for kind, _ in segs if kind == "L")
        c_count += sum(1 for kind, _ in segs if kind == "C")
        angles.extend(path_tangent_metrics(segs))
        endpoints.append([start.tolist(), end.tolist()])
    arr = np.asarray(angles, dtype=float)
    return {
        "file": str(path),
        "path_count": len(paths),
        "L_count": l_count,
        "C_count": c_count,
        "segment_count": l_count + c_count,
        "control_point_count": c_count * 2,
        "internal_join_count": int(len(arr)),
        "join_angle_mean_deg": round(float(arr.mean()), 4) if len(arr) else 0.0,
        "join_angle_p95_deg": round(float(np.percentile(arr, 95)), 4) if len(arr) else 0.0,
        "join_angle_max_deg": round(float(arr.max()), 4) if len(arr) else 0.0,
        "joins_over_10deg": int(np.sum(arr > 10.0)) if len(arr) else 0,
        "joins_over_20deg": int(np.sum(arr > 20.0)) if len(arr) else 0,
        "endpoints": endpoints,
    }


def endpoint_drift(reference, candidate):
    a = reference["endpoints"]
    b = candidate["endpoints"]
    if not isinstance(a, list) or not isinstance(b, list) or len(a) != len(b):
        return {"endpoint_pair_count": 0, "endpoint_drift_max": float("inf"), "endpoint_drift_mean": float("inf")}
    distances = []
    for pa, pb in zip(a, b):
        aa = np.asarray(pa, dtype=float)
        bb = np.asarray(pb, dtype=float)
        distances.extend(np.linalg.norm(aa - bb, axis=1).tolist())
    return {
        "endpoint_pair_count": len(distances),
        "endpoint_drift_max": round(max(distances, default=0.0), 4),
        "endpoint_drift_mean": round(float(np.mean(distances)) if distances else 0.0, 4),
    }


def render(svg: Path, out_dir: Path):
    exe = shutil.which("inkscape")
    if exe is None:
        return ["SKIP: inkscape unavailable"]
    out_dir.mkdir(parents=True, exist_ok=True)
    outputs = []
    for size in (64, 512, 2048):
        target = out_dir / f"{svg.stem}-{size}.png"
        subprocess.run(
            [exe, str(svg), "--export-type=png", f"--export-filename={target}", "-w", str(size), "-h", str(size)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        outputs.append(str(target))
    return outputs


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("reference", type=Path, help="polyline baseline SVG")
    p.add_argument("candidates", type=Path, nargs="+")
    p.add_argument("--json", type=Path, default=None)
    p.add_argument("--render-dir", type=Path, default=None)
    args = p.parse_args()

    ref = svg_metrics(args.reference)
    result = {"reference": ref, "candidates": []}
    for path in args.candidates:
        m = svg_metrics(path)
        m.update(endpoint_drift(ref, m))
        if args.render_dir:
            m["renders"] = render(path, args.render_dir / path.stem)
        result["candidates"].append(m)
    ref.pop("endpoints", None)
    for m in result["candidates"]:
        m.pop("endpoints", None)

    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
