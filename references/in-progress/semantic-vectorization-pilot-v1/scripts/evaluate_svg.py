#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SVG_NS = "http://www.w3.org/2000/svg"
SVG_TAG = f"{{{SVG_NS}}}svg"
GROUP_TAG = f"{{{SVG_NS}}}g"
PATH_TAG = f"{{{SVG_NS}}}path"
EXPECTED = {
    "fill": "none",
    "stroke": "currentColor",
    "stroke-width": "8",
    "stroke-linecap": "round",
    "stroke-linejoin": "round",
}
FORBIDDEN_LOCAL_NAMES = {"clipPath", "mask", "filter"}
COMMAND_RE = re.compile(r"[AaCcHhLlMmQqSsTtVvZz]")
NUMBER_RE = re.compile(r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?")


def lname(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def numeric_bbox_diagonal(path_data: str) -> float | None:
    nums = [float(value) for value in NUMBER_RE.findall(path_data)]
    if len(nums) < 4:
        return None
    xs = nums[0::2]
    ys = nums[1::2]
    if not xs or not ys:
        return None
    return math.hypot(max(xs) - min(xs), max(ys) - min(ys))


def inspect(path: Path) -> dict[str, object]:
    errors: list[str] = []
    style_errors: list[str] = []
    metrics = {
        "path_count": 0,
        "segment_token_count": 0,
        "very_short_path_count": 0,
        "transform_count": 0,
        "semantic_group_count": 0,
        "anonymous_group_count": 0,
    }

    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as exc:
        return {
            "file": str(path),
            "gates": {"G1_SVG_VALID": "FAIL", "G2_STYLE_VALID": "NOT_RUN", "G3_STRUCTURE": "NOT_RUN", "G4_VISUAL": "NOT_MEASURED", "G5_SEMANTIC": "REQUIRES_HUMAN"},
            "overall": "FAIL",
            "errors": [str(exc)],
            "style_errors": [],
            "metrics": metrics,
        }

    if root.tag != SVG_TAG:
        errors.append("root-not-svg")
    if root.attrib.get("viewBox") != "0 0 512 512":
        errors.append(f"viewBox:{root.attrib.get('viewBox')}")

    def walk(element: ET.Element, inherited: dict[str, str]) -> None:
        current = dict(inherited)
        for key in EXPECTED:
            if key in element.attrib:
                current[key] = element.attrib[key]
        if "transform" in element.attrib:
            metrics["transform_count"] += 1
        if lname(element.tag) in FORBIDDEN_LOCAL_NAMES:
            style_errors.append(f"forbidden-element:{lname(element.tag)}")
        for attr in ("clip-path", "mask", "filter"):
            if attr in element.attrib:
                style_errors.append(f"forbidden-attribute:{attr}")

        if element.tag == GROUP_TAG:
            if element.attrib.get("data-part") or element.attrib.get("id"):
                metrics["semantic_group_count"] += 1
            else:
                metrics["anonymous_group_count"] += 1
        elif element.tag == PATH_TAG:
            metrics["path_count"] += 1
            d = element.attrib.get("d", "").strip()
            if not d:
                errors.append("path-without-d")
            commands = COMMAND_RE.findall(d)
            metrics["segment_token_count"] += max(0, len(commands) - 1)
            diagonal = numeric_bbox_diagonal(d)
            if diagonal is not None and diagonal < 16:
                metrics["very_short_path_count"] += 1
            for key, expected in EXPECTED.items():
                if current.get(key) != expected:
                    style_errors.append(f"{key}:expected={expected}:actual={current.get(key)}")

        for child in list(element):
            walk(child, current)

    walk(root, {})
    if metrics["path_count"] == 0:
        errors.append("no-paths")

    g1 = "PASS" if not errors else "FAIL"
    g2 = "PASS" if not style_errors and g1 == "PASS" else "FAIL" if g1 == "PASS" else "NOT_RUN"
    g3 = "REQUIRES_HUMAN" if g2 == "PASS" else "NOT_RUN"
    overall = "FAIL" if "FAIL" in (g1, g2) else "INCOMPLETE"

    return {
        "file": str(path),
        "gates": {
            "G1_SVG_VALID": g1,
            "G2_STYLE_VALID": g2,
            "G3_STRUCTURE": g3,
            "G4_VISUAL": "NOT_MEASURED",
            "G5_SEMANTIC": "REQUIRES_HUMAN",
        },
        "overall": overall,
        "errors": sorted(set(errors)),
        "style_errors": sorted(set(style_errors)),
        "metrics": metrics,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Static evaluation for semantic-vectorization SVG candidates.")
    parser.add_argument("svg", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = inspect(args.svg)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 1 if report["overall"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
