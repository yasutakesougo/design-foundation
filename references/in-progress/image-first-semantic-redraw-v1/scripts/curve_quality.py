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
from typing import Iterable

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


def parse_segments(d: str) -> tuple[list[tuple[str, tuple[np.ndarray, ...]]], np.ndarray, np.ndarray]:
    tokens = TOKEN_RE.findall(d)
    i = 0
    cur = np.zeros(2, dtype=float)
    start = None
    segments: list[tuple[str, tuple[np.ndarray, ...]]] = []
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


def path_tangent_metrics(segments: list[tuple[str, tuple[np.ndarray, ...]]]) -> list[float]:
    angles: list[float] = []
    for prev, nxt in zip(segments, segments[1:]):
        if prev[0] == "L":
            a = prev[1][1] - prev[1][0]
        else:
            a = prev[1][3] - prev[1][2]
        if nxt[0] == "L":
            b = nxt[1][1] - nxt[1][0]
        else:
            b = nxt[1][1] - nxt[1][0]
        angles.append(_angle_deg(a, b))
    return angles


def _cross2(a: np.ndarray, b: np.ndarray) -> float:
    return float(a[0] * b[1] - a[1] * b[0])


def _cubic_curvature_start(pts: tuple[np.ndarray, ...]) -> float:
    p0, p1, p2, _ = pts
    d = 3.0 * (p1 - p0)
    dd = 6.0 * (p0 - 2.0 * p1 + p2)
    den = float(np.linalg.norm(d)) ** 3
    return _cross2(d, dd) / den if den > 1e-12 else 0.0


def _cubic_curvature_end(pts: tuple[np.ndarray, ...]) -> float:
    _, p1, p2, p3 = pts
    d = 3.0 * (p3 - p2)
    dd = 6.0 * (p3 - 2.0 * p2 + p1)
    den = float(np.linalg.norm(d)) ** 3
    return _cross2(d, dd) / den if den > 1e-12 else 0.0


def _major_contour_join_metrics(segments: list[tuple[str, tuple[np.ndarray, ...]]], viewbox: float = 512.0) -> dict[str, list[float] | int]:
    """Curvature-handoff evidence for locked long upper/head contours only.

    Same-sign joins measure handoff between continuing bends. Opposite-sign joins are
    counted separately because forcing equal curvature across a true SOURCE inflection
    would be incorrect. Evidence only; Human Visual Acceptance remains authoritative.
    """
    sampled = _sample_path(segments)
    if len(sampled) < 2:
        return {"same_sign_abs": [], "same_sign_rel": [], "opposite_sign_count": 0}
    arc = float(np.linalg.norm(np.diff(sampled, axis=0), axis=1).sum())
    mean_y = float(np.mean(sampled[:, 1]))
    xspan = float(np.ptp(sampled[:, 0])); yspan = float(np.ptp(sampled[:, 1]))
    if arc < 56.0 or mean_y > .62 * viewbox or not (yspan >= .07 * viewbox or xspan >= .14 * viewbox):
        return {"same_sign_abs": [], "same_sign_rel": [], "opposite_sign_count": 0}
    same_abs: list[float] = []; same_rel: list[float] = []; opposite = 0
    for left, right in zip(segments, segments[1:]):
        if left[0] != "C" or right[0] != "C":
            continue
        kl = _cubic_curvature_end(left[1]); kr = _cubic_curvature_start(right[1])
        if kl * kr <= 0:
            opposite += 1
            continue
        same_abs.append(abs(kl - kr))
        same_rel.append(abs(kl - kr) / (abs(kl) + abs(kr) + 1e-12))
    return {"same_sign_abs": same_abs, "same_sign_rel": same_rel, "opposite_sign_count": opposite}


def svg_metrics(path: Path) -> dict[str, object]:
    root = ET.parse(path).getroot()
    paths = [e for e in root.iter() if e.tag.rsplit("}", 1)[-1] == "path"]
    l_count = c_count = 0
    angles: list[float] = []
    curvature_jumps: list[float] = []
    relative_curvature_jumps: list[float] = []
    opposite_sign_join_count = 0
    endpoints: list[list[list[float]]] = []
    for e in paths:
        segs, start, end = parse_segments(e.attrib.get("d", ""))
        l_count += sum(1 for kind, _ in segs if kind == "L")
        c_count += sum(1 for kind, _ in segs if kind == "C")
        angles.extend(path_tangent_metrics(segs))
        jm = _major_contour_join_metrics(segs)
        curvature_jumps.extend(jm["same_sign_abs"])
        relative_curvature_jumps.extend(jm["same_sign_rel"])
        opposite_sign_join_count += int(jm["opposite_sign_count"])
        endpoints.append([start.tolist(), end.tolist()])
    arr = np.asarray(angles, dtype=float)
    cj = np.asarray(curvature_jumps, dtype=float)
    rj = np.asarray(relative_curvature_jumps, dtype=float)
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
        "major_contour_curvature_join_count": int(len(cj)),
        "major_contour_curvature_jump_mean": round(float(cj.mean()), 6) if len(cj) else 0.0,
        "major_contour_curvature_jump_p95": round(float(np.percentile(cj, 95)), 6) if len(cj) else 0.0,
        "major_contour_curvature_jump_max": round(float(cj.max()), 6) if len(cj) else 0.0,
        "major_contour_relative_curvature_jump_mean": round(float(rj.mean()), 6) if len(rj) else 0.0,
        "major_contour_relative_curvature_jump_p95": round(float(np.percentile(rj, 95)), 6) if len(rj) else 0.0,
        "major_contour_opposite_sign_join_count": opposite_sign_join_count,
        "endpoints": endpoints,
    }


def endpoint_drift(reference: dict[str, object], candidate: dict[str, object]) -> dict[str, float | int]:
    a = reference["endpoints"]
    b = candidate["endpoints"]
    if not isinstance(a, list) or not isinstance(b, list) or len(a) != len(b):
        return {"endpoint_pair_count": 0, "endpoint_drift_max": float("inf"), "endpoint_drift_mean": float("inf")}
    distances: list[float] = []
    for pa, pb in zip(a, b):
        aa = np.asarray(pa, dtype=float)
        bb = np.asarray(pb, dtype=float)
        distances.extend(np.linalg.norm(aa - bb, axis=1).tolist())
    return {
        "endpoint_pair_count": len(distances),
        "endpoint_drift_max": round(max(distances, default=0.0), 4),
        "endpoint_drift_mean": round(float(np.mean(distances)) if distances else 0.0, 4),
    }


def _sample_segment(segment: tuple[str, tuple[np.ndarray, ...]], steps: int = 24) -> np.ndarray:
    kind, pts = segment
    t = np.linspace(0.0, 1.0, steps)[:, None]
    if kind == "L":
        a, b = pts
        return a * (1.0 - t) + b * t
    p0, p1, p2, p3 = pts
    u = 1.0 - t
    return u**3 * p0 + 3 * u**2 * t * p1 + 3 * u * t**2 * p2 + t**3 * p3


def _sample_path(segments: list[tuple[str, tuple[np.ndarray, ...]]]) -> np.ndarray:
    chunks = []
    for i, seg in enumerate(segments):
        part = _sample_segment(seg)
        chunks.append(part if i == 0 else part[1:])
    return np.vstack(chunks) if chunks else np.empty((0, 2), dtype=float)


def _resample_n(points: np.ndarray, n: int) -> np.ndarray:
    a = np.asarray(points, dtype=float)
    if len(a) < 2:
        return a
    d = np.linalg.norm(np.diff(a, axis=0), axis=1)
    arc = np.r_[0.0, np.cumsum(d)]
    total = float(arc[-1])
    if total <= 1e-9:
        return np.repeat(a[:1], n, axis=0)
    q = np.linspace(0.0, total, n)
    return np.c_[np.interp(q, arc, a[:, 0]), np.interp(q, arc, a[:, 1])]


def _signed_curvature(points: np.ndarray, window: int = 2) -> np.ndarray:
    p = np.asarray(points, dtype=float)
    out = np.zeros(len(p), dtype=float)
    for i in range(window, len(p) - window):
        a = p[i] - p[i - window]
        b = p[i + window] - p[i]
        la, lb = float(np.linalg.norm(a)), float(np.linalg.norm(b))
        if la > 1e-9 and lb > 1e-9:
            angle = math.atan2(a[0] * b[1] - a[1] * b[0], float(np.dot(a, b)))
            out[i] = angle / ((la + lb) / 2.0)
    return out


def _moving_average(values: np.ndarray, radius: int = 5) -> np.ndarray:
    v = np.asarray(values, dtype=float)
    if radius <= 0 or len(v) == 0:
        return v.copy()
    out = np.empty_like(v)
    for i in range(len(v)):
        lo, hi = max(0, i - radius), min(len(v), i + radius + 1)
        out[i] = float(np.mean(v[lo:hi]))
    return out


def _sign_changes(values: np.ndarray, epsilon: float = 1e-4) -> int:
    last = 0
    count = 0
    for value in values:
        sign = 0 if abs(float(value)) < epsilon else (1 if value > 0 else -1)
        if sign == 0:
            continue
        if last and sign != last:
            count += 1
        last = sign
    return count


def _extrema_count(values: np.ndarray) -> int:
    a = np.abs(np.asarray(values, dtype=float))
    return sum(bool(a[i] > a[i - 1] and a[i] >= a[i + 1]) for i in range(1, len(a) - 1))


def curvature_character(svg: Path, source_raster: Path, minimum_long_path: float = 35.0) -> dict[str, object]:
    """Compare SVG curve character to a low-frequency proxy of the SOURCE centerline.

    The SOURCE proxy is intentionally local-polynomial-smoothed skeleton geometry. It is
    supporting evidence only; Human Visual Acceptance remains authoritative.
    """
    from PIL import Image
    from skimage.morphology import skeletonize
    import centerline_vectorize as cv

    image = Image.open(source_raster)
    mask = cv.semantic_stroke_mask(image, "auto", 70, 18, 180)
    raw_paths = cv.remove_short(cv.trace_polylines(skeletonize(mask)), 4.0)
    root = ET.parse(svg).getroot()
    svg_paths = [e for e in root.iter() if e.tag.rsplit("}", 1)[-1] == "path"]
    if len(raw_paths) != len(svg_paths):
        return {"status": "SKIP", "reason": "source/SVG path-count mismatch"}

    scale = 512.0 / max(image.width, image.height)
    weighted = []
    source_sign_total = candidate_sign_total = 0
    source_extrema_total = candidate_extrema_total = 0
    for raw, element in zip(raw_paths, svg_paths):
        raw_len = cv.path_length(raw) * scale
        if raw_len < minimum_long_path:
            continue
        source = np.asarray(raw, dtype=float) * scale
        segments, _, _ = parse_segments(element.attrib.get("d", ""))
        candidate = _sample_path(segments)
        if len(candidate) < 2:
            continue
        n = max(48, int(round(raw_len / 1.5)))
        source = _resample_n(source, n)
        spacing = max(raw_len / max(n - 1, 1), 0.2)
        radius = min(16, max(5, int(round(12.0 / spacing))))
        reference = cv.local_poly_smooth(source, radius=radius, adaptive=False)
        candidate = _resample_n(candidate, n)
        k_ref = _signed_curvature(reference, 2)
        k_cand = _signed_curvature(candidate, 2)
        low_ref = _moving_average(k_ref, 8)
        low_cand = _moving_average(k_cand, 8)
        hi_ref = k_ref - low_ref
        hi_cand = k_cand - low_cand
        core = slice(8, -8) if n > 16 else slice(None)
        ref_std = float(np.std(low_ref[core]))
        item = {
            "weight": raw_len,
            "low_frequency_curvature_rmse": float(np.sqrt(np.mean((low_cand[core] - low_ref[core]) ** 2))),
            "high_frequency_curvature_rms": float(np.sqrt(np.mean(hi_cand[core] ** 2))),
            "source_high_frequency_curvature_rms": float(np.sqrt(np.mean(hi_ref[core] ** 2))),
            "low_frequency_curvature_std_ratio": float(np.std(low_cand[core])) / (ref_std + 1e-9),
            "geometry_rms_to_source_lowpass": float(np.sqrt(np.mean(np.linalg.norm(candidate - reference, axis=1) ** 2))),
            "low_frequency_curvature_derivative_rmse": float(np.sqrt(np.mean((np.diff(low_cand[core]) - np.diff(low_ref[core])) ** 2))) if len(low_ref[core]) > 1 else 0.0,
        }
        weighted.append(item)
        source_sign_total += _sign_changes(low_ref[core])
        candidate_sign_total += _sign_changes(low_cand[core])
        source_extrema_total += _extrema_count(low_ref[core])
        candidate_extrema_total += _extrema_count(low_cand[core])

    if not weighted:
        return {"status": "SKIP", "reason": "no long paths"}
    total = sum(float(x["weight"]) for x in weighted)
    def avg(key: str) -> float:
        return sum(float(x[key]) * float(x["weight"]) for x in weighted) / total
    return {
        "status": "EVIDENCE_ONLY",
        "long_path_count": len(weighted),
        "low_frequency_curvature_rmse": round(avg("low_frequency_curvature_rmse"), 6),
        "high_frequency_curvature_rms": round(avg("high_frequency_curvature_rms"), 6),
        "source_high_frequency_curvature_rms": round(avg("source_high_frequency_curvature_rms"), 6),
        "low_frequency_curvature_std_ratio": round(avg("low_frequency_curvature_std_ratio"), 4),
        "geometry_rms_to_source_lowpass": round(avg("geometry_rms_to_source_lowpass"), 4),
        "low_frequency_curvature_derivative_rmse": round(avg("low_frequency_curvature_derivative_rmse"), 6),
        "source_broad_sign_changes": source_sign_total,
        "candidate_broad_sign_changes": candidate_sign_total,
        "broad_sign_change_delta": abs(candidate_sign_total - source_sign_total),
        "source_broad_curvature_extrema": source_extrema_total,
        "candidate_broad_curvature_extrema": candidate_extrema_total,
        "broad_curvature_extrema_delta": abs(candidate_extrema_total - source_extrema_total),
        "interpretation": "supporting metric only; lower high-frequency RMS is not sufficient if low-frequency SOURCE character is lost",
    }


def render(svg: Path, out_dir: Path) -> list[str]:
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
    p.add_argument("--source-raster", type=Path, default=None, help="optional SOURCE raster for scale-separated curvature evidence")
    args = p.parse_args()

    ref = svg_metrics(args.reference)
    if args.source_raster:
        ref["curvature_character"] = curvature_character(args.reference, args.source_raster)
    result: dict[str, object] = {"reference": ref, "candidates": []}
    for path in args.candidates:
        m = svg_metrics(path)
        m.update(endpoint_drift(ref, m))
        if args.render_dir:
            m["renders"] = render(path, args.render_dir / path.stem)
        if args.source_raster:
            m["curvature_character"] = curvature_character(path, args.source_raster)
        result["candidates"].append(m)
    ref.pop("endpoints", None)
    for m in result["candidates"]:
        if isinstance(m, dict):
            m.pop("endpoints", None)

    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())