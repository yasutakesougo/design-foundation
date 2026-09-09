#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable

from evaluate_svg import inspect
from normalize_svg import normalize

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def command_version(executable: str) -> str:
    for flag in ("--version", "-version", "-v"):
        try:
            proc = subprocess.run([executable, flag], check=False, text=True, capture_output=True, timeout=10)
        except Exception:
            continue
        text = (proc.stdout or proc.stderr).strip().splitlines()
        if text:
            return text[0][:300]
    return "UNKNOWN"


def rasterize_inkscape(inkscape: str, source: Path, target: Path, size: int) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        inkscape,
        str(source),
        "--export-type=png",
        f"--export-filename={target}",
        f"--export-width={size}",
        f"--export-height={size}",
        "--export-background=white",
        "--export-background-opacity=1",
    ]
    subprocess.run(cmd, check=True, text=True, capture_output=True)


def run_autotrace(autotrace: str, source_png: Path, raw_svg: Path) -> tuple[str, str]:
    cmd = [
        autotrace,
        str(source_png),
        "-centerline",
        "-output-format",
        "svg",
        "-output-file",
        str(raw_svg),
    ]
    proc = subprocess.run(cmd, check=False, text=True, capture_output=True)
    if proc.returncode != 0 or not raw_svg.exists():
        message = (proc.stderr or proc.stdout or f"exit={proc.returncode}").strip()
        return "FAIL", message[:500]
    return "PASS", "autotrace centerline completed"


def load_binary(source_png: Path, variant: str):
    import numpy as np
    from PIL import Image, ImageFilter
    from skimage.morphology import closing, disk, opening

    image = Image.open(source_png).convert("L")
    if variant == "raw-denoise":
        image = image.filter(ImageFilter.MedianFilter(size=3))
    gray = np.asarray(image)
    binary = gray < 220

    if variant == "light-open-close":
        binary = opening(binary, disk(1))
        binary = closing(binary, disk(1))
    elif variant == "morphology-variant":
        binary = closing(binary, disk(1))
    return binary


def neighbors(point: tuple[int, int], pixels: set[tuple[int, int]]) -> list[tuple[int, int]]:
    y, x = point
    result = []
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == 0 and dx == 0:
                continue
            q = (y + dy, x + dx)
            if q in pixels:
                result.append(q)
    return result


def edge_key(a: tuple[int, int], b: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    return (a, b) if a <= b else (b, a)


def trace_skeleton_polylines(skeleton) -> list[list[tuple[int, int]]]:
    import numpy as np

    ys, xs = np.nonzero(skeleton)
    pixels = set(zip(ys.tolist(), xs.tolist()))
    if not pixels:
        return []

    degree = {p: len(neighbors(p, pixels)) for p in pixels}
    nodes = {p for p, d in degree.items() if d != 2}
    visited_edges: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    lines: list[list[tuple[int, int]]] = []

    def follow(start: tuple[int, int], nxt: tuple[int, int]) -> list[tuple[int, int]]:
        line = [start, nxt]
        prev, cur = start, nxt
        visited_edges.add(edge_key(prev, cur))
        while cur not in nodes:
            options = [q for q in neighbors(cur, pixels) if q != prev and edge_key(cur, q) not in visited_edges]
            if not options:
                break
            q = options[0]
            line.append(q)
            visited_edges.add(edge_key(cur, q))
            prev, cur = cur, q
        return line

    for start in sorted(nodes):
        for nxt in sorted(neighbors(start, pixels)):
            if edge_key(start, nxt) not in visited_edges:
                lines.append(follow(start, nxt))

    for start in sorted(pixels):
        for nxt in sorted(neighbors(start, pixels)):
            if edge_key(start, nxt) in visited_edges:
                continue
            line = [start, nxt]
            visited_edges.add(edge_key(start, nxt))
            prev, cur = start, nxt
            while True:
                options = [q for q in neighbors(cur, pixels) if q != prev and edge_key(cur, q) not in visited_edges]
                if not options:
                    break
                q = options[0]
                line.append(q)
                visited_edges.add(edge_key(cur, q))
                prev, cur = cur, q
                if cur == start:
                    break
            lines.append(line)

    return [line for line in lines if len(line) >= 2]


def simplify_polyline(line: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if len(line) <= 2:
        return line
    out = [line[0]]
    prev_dir = None
    for i in range(1, len(line)):
        y0, x0 = line[i - 1]
        y1, x1 = line[i]
        direction = (max(-1, min(1, y1 - y0)), max(-1, min(1, x1 - x0)))
        if prev_dir is not None and direction != prev_dir:
            out.append(line[i - 1])
        prev_dir = direction
    out.append(line[-1])
    deduped = [out[0]]
    for point in out[1:]:
        if point != deduped[-1]:
            deduped.append(point)
    return deduped


def write_polyline_svg(lines: Iterable[list[tuple[int, int]]], target: Path) -> int:
    root = ET.Element(f"{{{SVG_NS}}}svg", {"viewBox": "0 0 512 512"})
    group = ET.SubElement(root, f"{{{SVG_NS}}}g", {
        "fill": "none",
        "stroke": "currentColor",
        "stroke-width": "8",
        "stroke-linecap": "round",
        "stroke-linejoin": "round",
    })
    count = 0
    for raw in lines:
        line = simplify_polyline(raw)
        if len(line) < 2:
            continue
        y0, x0 = line[0]
        commands = [f"M{x0} {y0}"]
        commands.extend(f"L{x} {y}" for y, x in line[1:])
        ET.SubElement(group, f"{{{SVG_NS}}}path", {"d": " ".join(commands)})
        count += 1
    if count == 0:
        raise ValueError("skeleton produced no polylines")
    target.parent.mkdir(parents=True, exist_ok=True)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(target, encoding="utf-8", xml_declaration=False)
    return count


def run_skeleton(source_png: Path, raw_svg: Path, variant: str) -> tuple[str, str]:
    try:
        from skimage.morphology import skeletonize
    except ImportError as exc:
        return "SKIP", f"scikit-image unavailable: {exc}"
    try:
        binary = load_binary(source_png, variant)
        skeleton = skeletonize(binary)
        lines = trace_skeleton_polylines(skeleton)
        count = write_polyline_svg(lines, raw_svg)
    except Exception as exc:
        return "FAIL", str(exc)
    return "PASS", f"skeleton/polyline completed: {count} raw paths"


def ssim_score(reference_png: Path, candidate_png: Path) -> float | None:
    try:
        import numpy as np
        from PIL import Image
        from skimage.metrics import structural_similarity
    except ImportError:
        return None
    ref = np.asarray(Image.open(reference_png).convert("L"))
    cand = np.asarray(Image.open(candidate_png).convert("L"))
    if ref.shape != cand.shape:
        return None
    return float(structural_similarity(ref, cand, data_range=255))


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the semantic-vectorization baseline without installing dependencies.")
    parser.add_argument("--workdir", type=Path, default=Path("semantic-vectorization-baseline-out"))
    args = parser.parse_args()

    pilot_root = Path(__file__).resolve().parents[1]
    manifest = json.loads((pilot_root / "fixtures" / "manifest.json").read_text(encoding="utf-8"))
    args.workdir.mkdir(parents=True, exist_ok=True)

    inkscape = shutil.which("inkscape")
    autotrace = shutil.which("autotrace")
    environment = {
        "inkscape": {"path": inkscape, "version": command_version(inkscape) if inkscape else None},
        "autotrace": {"path": autotrace, "version": command_version(autotrace) if autotrace else None},
    }

    report: dict[str, object] = {
        "pilot": manifest["pilot"],
        "fixture_source_head": manifest["source"]["head_sha"],
        "environment": environment,
        "fixtures": [],
    }

    if not inkscape:
        report["status"] = "INCOMPLETE"
        report["reason"] = "No deterministic rasterizer found. Expected inkscape."
        (args.workdir / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 2

    for fixture in manifest["fixtures"]:
        fixture_dir = args.workdir / fixture["id"]
        fixture_dir.mkdir(parents=True, exist_ok=True)
        source_svg = pilot_root / "fixtures" / fixture["file"]
        ref_512 = fixture_dir / "reference-512.png"
        ref_64 = fixture_dir / "reference-64.png"
        rasterize_inkscape(inkscape, source_svg, ref_512, 512)
        rasterize_inkscape(inkscape, source_svg, ref_64, 64)

        fixture_report: dict[str, object] = {
            "id": fixture["id"],
            "semantic_label": fixture["semantic_label"],
            "required_cues": fixture["required_cues"],
            "backends": [],
        }

        auto_entry: dict[str, object] = {"backend": "autotrace-centerline", "variant": "raw-denoise"}
        if not autotrace:
            auto_entry.update({"execution": "SKIP", "reason": "autotrace executable not found; installation is outside Pilot authority"})
        else:
            raw_svg = fixture_dir / "autotrace-raw.svg"
            normalized_svg = fixture_dir / "autotrace-normalized.svg"
            status, detail = run_autotrace(autotrace, ref_512, raw_svg)
            auto_entry.update({"execution": status, "detail": detail})
            if status == "PASS":
                try:
                    normalize(raw_svg, normalized_svg)
                    candidate_512 = fixture_dir / "autotrace-512.png"
                    candidate_64 = fixture_dir / "autotrace-64.png"
                    rasterize_inkscape(inkscape, normalized_svg, candidate_512, 512)
                    rasterize_inkscape(inkscape, normalized_svg, candidate_64, 64)
                    auto_entry["static_evaluation"] = inspect(normalized_svg)
                    auto_entry["visual"] = {
                        "ssim_512": ssim_score(ref_512, candidate_512),
                        "ssim_64": ssim_score(ref_64, candidate_64),
                    }
                except Exception as exc:
                    auto_entry.update({"execution": "FAIL", "detail": f"normalization/evaluation: {exc}"})
        fixture_report["backends"].append(auto_entry)

        for variant in ("raw-denoise", "light-open-close", "morphology-variant"):
            entry: dict[str, object] = {"backend": "skeleton-polyline", "variant": variant}
            raw_svg = fixture_dir / f"skeleton-{variant}-raw.svg"
            normalized_svg = fixture_dir / f"skeleton-{variant}-normalized.svg"
            status, detail = run_skeleton(ref_512, raw_svg, variant)
            entry.update({"execution": status, "detail": detail})
            if status == "PASS":
                try:
                    normalize(raw_svg, normalized_svg)
                    candidate_512 = fixture_dir / f"skeleton-{variant}-512.png"
                    candidate_64 = fixture_dir / f"skeleton-{variant}-64.png"
                    rasterize_inkscape(inkscape, normalized_svg, candidate_512, 512)
                    rasterize_inkscape(inkscape, normalized_svg, candidate_64, 64)
                    entry["static_evaluation"] = inspect(normalized_svg)
                    entry["visual"] = {
                        "ssim_512": ssim_score(ref_512, candidate_512),
                        "ssim_64": ssim_score(ref_64, candidate_64),
                    }
                    entry["semantic"] = {
                        "status": "REQUIRES_HUMAN",
                        "required_cues": fixture["required_cues"],
                    }
                except Exception as exc:
                    entry.update({"execution": "FAIL", "detail": f"normalization/evaluation: {exc}"})
            fixture_report["backends"].append(entry)

        report["fixtures"].append(fixture_report)

    all_entries = [entry for fixture in report["fixtures"] for entry in fixture["backends"]]
    report["status"] = "INCOMPLETE" if any(entry.get("execution") == "SKIP" for entry in all_entries) else "EVIDENCE_READY"
    report["human_gate"] = "Semantic Gesture Check and Human Visual Acceptance remain required"
    report_path = args.workdir / "report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
