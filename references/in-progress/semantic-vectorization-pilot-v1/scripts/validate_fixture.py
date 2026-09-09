#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SVG_NS = "http://www.w3.org/2000/svg"
PATH_TAG = f"{{{SVG_NS}}}path"
GROUP_TAG = f"{{{SVG_NS}}}g"
EXPECTED = {
    "fill": "none",
    "stroke": "currentColor",
    "stroke-width": "8",
    "stroke-linecap": "round",
    "stroke-linejoin": "round",
}


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def walk(element: ET.Element, inherited: dict[str, str], errors: list[str], stats: dict[str, int]) -> None:
    current = dict(inherited)
    for key in EXPECTED:
        if key in element.attrib:
            current[key] = element.attrib[key]

    if element.tag == GROUP_TAG:
        stats["group_count"] += 1
    if element.tag == PATH_TAG:
        stats["path_count"] += 1
        if not element.attrib.get("d", "").strip():
            errors.append("path-without-d")
        for key, expected in EXPECTED.items():
            actual = current.get(key)
            if actual != expected:
                errors.append(f"style:{key}:expected={expected}:actual={actual}")

    for child in list(element):
        walk(child, current, errors, stats)


def validate_one(path: Path, source_blob_sha: str) -> dict[str, object]:
    data = path.read_bytes()
    errors: list[str] = []
    stats = {"path_count": 0, "group_count": 0}
    blob_sha = git_blob_sha(data)

    if blob_sha != source_blob_sha:
        errors.append(f"blob-sha-mismatch:expected={source_blob_sha}:actual={blob_sha}")

    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        return {
            "file": str(path),
            "status": "FAIL",
            "blob_sha": blob_sha,
            "errors": [f"xml-parse:{exc}"],
            **stats,
        }

    if root.tag != f"{{{SVG_NS}}}svg":
        errors.append(f"root-not-svg:{root.tag}")
    if root.attrib.get("viewBox") != "0 0 512 512":
        errors.append(f"viewBox:{root.attrib.get('viewBox')}")

    walk(root, {}, errors, stats)
    if stats["path_count"] == 0:
        errors.append("no-paths")

    return {
        "file": str(path),
        "status": "PASS" if not errors else "FAIL",
        "blob_sha": blob_sha,
        "errors": sorted(set(errors)),
        **stats,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate pinned semantic-vectorization fixtures.")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "fixtures" / "manifest.json",
    )
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    fixture_root = args.manifest.parent
    reports = [
        validate_one(fixture_root / item["file"], item["source_blob_sha"])
        for item in manifest["fixtures"]
    ]
    overall = "PASS" if all(item["status"] == "PASS" for item in reports) else "FAIL"
    output = {
        "pilot": manifest["pilot"],
        "source_head_sha": manifest["source"]["head_sha"],
        "status": overall,
        "fixtures": reports,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
