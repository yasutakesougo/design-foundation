#!/usr/bin/env python3
"""Fail-closed static style/structure check for IMAGE-FIRST candidate SVGs."""
from __future__ import annotations

import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path

EXPECTED = {
    "fill": "none",
    "stroke": "currentColor",
    "stroke-width": "8",
    "stroke-linecap": "round",
    "stroke-linejoin": "round",
}
FORBIDDEN = {"clipPath", "mask", "filter", "image"}


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("svg", type=Path)
    args = ap.parse_args()

    errors: list[str] = []
    root = ET.parse(args.svg).getroot()
    if local(root.tag) != "svg":
        errors.append("root-not-svg")
    if root.attrib.get("viewBox") != "0 0 512 512":
        errors.append(f"viewBox={root.attrib.get('viewBox')!r}")

    paths = 0
    transforms = 0

    def walk(el: ET.Element, style: dict[str, str]) -> None:
        nonlocal paths, transforms
        current = dict(style)
        for key in EXPECTED:
            if key in el.attrib:
                current[key] = el.attrib[key]
        if "transform" in el.attrib:
            transforms += 1
        if local(el.tag) in FORBIDDEN:
            errors.append(f"forbidden-element:{local(el.tag)}")
        if local(el.tag) == "path":
            paths += 1
            if not el.attrib.get("d", "").strip():
                errors.append("path-without-d")
            for key, val in EXPECTED.items():
                if current.get(key) != val:
                    errors.append(f"style:{key}={current.get(key)!r}")
        for child in el:
            walk(child, current)

    walk(root, {})
    if paths == 0:
        errors.append("no-paths")
    if transforms:
        errors.append(f"transform-count={transforms}")

    report = {
        "file": str(args.svg),
        "path_count": paths,
        "transform_count": transforms,
        "style_valid": not errors,
        "errors": sorted(set(errors)),
        "human_semantic_review": "REQUIRED",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
