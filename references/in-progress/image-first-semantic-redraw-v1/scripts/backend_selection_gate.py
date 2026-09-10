#!/usr/bin/env python3
"""Technical-evaluation gate for IMAGE-FIRST production backend selection.

This wrapper does not select or promote a production backend. It executes the
Human-locked candidate order, validates each generated SVG fail-closed, and permits
JOIN-CONTINUITY fallback only when the caller explicitly passes --allow-fallback.
Every attempt and fallback decision is written to JSON for audit.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import math
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable

PRIMARY_MODE = "curvature-aware-source-guided"
FALLBACK_MODE = "curvature-aware-join"
MODE_LABELS = {
    PRIMARY_MODE: "SOURCE-GUIDED",
    FALLBACK_MODE: "JOIN-CONTINUITY",
}
EXPECTED_STYLE = {
    "fill": "none",
    "stroke": "currentColor",
    "stroke-width": "8",
    "stroke-linecap": "round",
    "stroke-linejoin": "round",
}
NONFINITE_RE = re.compile(r"(?i)(?:^|[^a-z])(?:nan|[-+]?inf(?:inity)?)(?:$|[^a-z])")


@dataclass
class Attempt:
    mode: str
    label: str
    ok: bool
    failure_class: str | None = None
    failure_detail: str | None = None
    svg_sha256: str | None = None
    metrics_sha256: str | None = None
    path_count: int | None = None
    source_path_count: int | None = None
    segment_count: int | None = None
    refined_path_count: int | None = None


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def runtime_versions() -> dict[str, str]:
    out = {"python": sys.version.split()[0]}
    for dist, key in (("numpy", "numpy"), ("scikit-image", "scikit-image"), ("Pillow", "Pillow")):
        try:
            out[key] = importlib.metadata.version(dist)
        except importlib.metadata.PackageNotFoundError:
            out[key] = "UNAVAILABLE"
    return out


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _effective_style(el: ET.Element, inherited: dict[str, str]) -> dict[str, str]:
    style = dict(inherited)
    for key in EXPECTED_STYLE:
        if key in el.attrib:
            style[key] = el.attrib[key]
    return style


def validate_candidate(svg: Path, metrics_path: Path) -> tuple[list[str], dict[str, object]]:
    """Return validation errors and parsed metrics. Any error is fail-closed."""
    errors: list[str] = []
    metrics: dict[str, object] = {}
    if not svg.is_file():
        return ["output-svg-missing"], metrics
    if not metrics_path.is_file():
        return ["metrics-json-missing"], metrics

    try:
        metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    except Exception as exc:  # evidence wrapper: classify malformed output, never continue
        return [f"metrics-json-invalid:{type(exc).__name__}"], metrics

    try:
        root = ET.parse(svg).getroot()
    except Exception as exc:
        return [f"svg-xml-invalid:{type(exc).__name__}"], metrics

    if _local(root.tag) != "svg":
        errors.append("root-not-svg")
    if root.attrib.get("viewBox") != "0 0 512 512":
        errors.append("viewBox-contract-failed")

    actual_paths = 0

    def walk(el: ET.Element, inherited: dict[str, str]) -> None:
        nonlocal actual_paths
        style = _effective_style(el, inherited)
        if "transform" in el.attrib:
            errors.append("transform-present")
        if _local(el.tag) in {"clipPath", "mask", "filter", "image"}:
            errors.append(f"forbidden-element:{_local(el.tag)}")
        if _local(el.tag) == "path":
            actual_paths += 1
            d = el.attrib.get("d", "")
            if not d.strip():
                errors.append("path-without-d")
            if NONFINITE_RE.search(d):
                errors.append("nonfinite-path-coordinate")
            for key, expected in EXPECTED_STYLE.items():
                if style.get(key) != expected:
                    errors.append(f"style-contract:{key}")
        for child in el:
            walk(child, style)

    walk(root, {})

    def integer_metric(name: str) -> int | None:
        value = metrics.get(name)
        if isinstance(value, bool) or not isinstance(value, int):
            errors.append(f"metric-invalid:{name}")
            return None
        return value

    path_count = integer_metric("path_count")
    source_path_count = integer_metric("source_path_count")
    segment_count = integer_metric("segment_count")
    refined_count = integer_metric("correction3_refined_path_count")

    if actual_paths <= 0:
        errors.append("no-paths")
    if path_count is not None and path_count != actual_paths:
        errors.append("path-count-vs-svg-mismatch")
    if path_count is not None and source_path_count is not None and path_count != source_path_count:
        errors.append("path-count-vs-source-topology-mismatch")
    if segment_count is not None and segment_count <= 0:
        errors.append("segment-count-nonpositive")
    if refined_count is not None and refined_count < 0:
        errors.append("refined-path-count-negative")

    for name in ("centerline_deviation_mean_source_px", "centerline_deviation_max_source_px"):
        value = metrics.get(name)
        if not isinstance(value, (int, float)) or not math.isfinite(float(value)):
            errors.append(f"metric-nonfinite:{name}")

    return sorted(set(errors)), metrics


def resolve_with_runner(
    runner: Callable[[str], Attempt],
    *,
    allow_fallback: bool,
) -> tuple[str, bool, list[Attempt]]:
    """Pure decision control used by the CLI and unit tests.

    Returns (result, fallback_used, attempts). Result is evidence state only:
    SOURCE-GUIDED, JOIN-CONTINUITY, or HOLD.
    """
    primary = runner(PRIMARY_MODE)
    attempts = [primary]
    if primary.ok:
        return "SOURCE-GUIDED", False, attempts
    if not allow_fallback:
        return "HOLD", False, attempts
    fallback = runner(FALLBACK_MODE)
    attempts.append(fallback)
    if fallback.ok:
        return "JOIN-CONTINUITY", True, attempts
    return "HOLD", True, attempts


def execute_backend(
    mode: str,
    *,
    input_path: Path,
    output_dir: Path,
    vectorizer: Path,
) -> Attempt:
    label = MODE_LABELS.get(mode, mode)
    stem = "source-guided" if mode == PRIMARY_MODE else "join-continuity"
    svg = output_dir / f"{stem}.svg"
    metrics_path = output_dir / f"{stem}.metrics.json"
    output_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable,
        str(vectorizer),
        str(input_path),
        str(svg),
        "--curve-mode",
        mode,
        "--metrics",
        str(metrics_path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "backend returned non-zero").strip()[-1000:]
        return Attempt(mode=mode, label=label, ok=False, failure_class="backend-execution-failed", failure_detail=detail)

    errors, metrics = validate_candidate(svg, metrics_path)
    if errors:
        return Attempt(
            mode=mode,
            label=label,
            ok=False,
            failure_class="candidate-validation-failed",
            failure_detail=";".join(errors),
        )

    return Attempt(
        mode=mode,
        label=label,
        ok=True,
        svg_sha256=sha256_file(svg),
        metrics_sha256=sha256_file(metrics_path),
        path_count=int(metrics["path_count"]),
        source_path_count=int(metrics["source_path_count"]),
        segment_count=int(metrics["segment_count"]),
        refined_path_count=int(metrics["correction3_refined_path_count"]),
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output_dir", type=Path)
    ap.add_argument("--vectorizer", type=Path, default=Path(__file__).with_name("centerline_vectorize.py"))
    ap.add_argument("--allow-fallback", action="store_true", help="explicitly permit JOIN-CONTINUITY after primary failure")
    ap.add_argument("--json", type=Path, default=None)
    args = ap.parse_args()

    input_sha = sha256_file(args.input) if args.input.is_file() else None

    def runner(mode: str) -> Attempt:
        return execute_backend(mode, input_path=args.input, output_dir=args.output_dir, vectorizer=args.vectorizer)

    result, fallback_used, attempts = resolve_with_runner(runner, allow_fallback=args.allow_fallback)
    report = {
        "authority": "TECHNICAL_EVIDENCE_ONLY",
        "input": str(args.input),
        "input_sha256": input_sha,
        "runtime": runtime_versions(),
        "primary": "SOURCE-GUIDED",
        "fallback": "JOIN-CONTINUITY",
        "fallback_allowed": bool(args.allow_fallback),
        "fallback_used": fallback_used,
        "result": result,
        "attempts": [asdict(a) for a in attempts],
        "production_backend_selection": "NOT_AUTHORIZED_BY_THIS_RUNNER",
    }
    text = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    target = args.json or (args.output_dir / "backend-selection-evidence.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if result != "HOLD" else 2


if __name__ == "__main__":
    raise SystemExit(main())
