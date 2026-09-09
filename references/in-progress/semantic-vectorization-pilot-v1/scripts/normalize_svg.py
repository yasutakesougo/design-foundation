#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)
SVG_TAG = f"{{{SVG_NS}}}svg"
GROUP_TAG = f"{{{SVG_NS}}}g"
PATH_TAG = f"{{{SVG_NS}}}path"
FORBIDDEN_TAGS = {
    f"{{{SVG_NS}}}clipPath",
    f"{{{SVG_NS}}}mask",
    f"{{{SVG_NS}}}filter",
}
STYLE = {
    "fill": "none",
    "stroke": "currentColor",
    "stroke-width": "8",
    "stroke-linecap": "round",
    "stroke-linejoin": "round",
}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def semantic_group_name(element: ET.Element) -> str | None:
    value = element.attrib.get("data-part") or element.attrib.get("id")
    if not value:
        return None
    value = value.strip()
    return value or None


def assert_supported(element: ET.Element) -> None:
    if element.tag in FORBIDDEN_TAGS:
        raise ValueError(f"forbidden element: {local_name(element.tag)}")
    for attr in ("transform", "clip-path", "mask", "filter"):
        if attr in element.attrib:
            raise ValueError(f"unsupported attribute {attr} on {local_name(element.tag)}")
    for child in list(element):
        assert_supported(child)


def copy_paths(source: ET.Element, target: ET.Element) -> int:
    count = 0
    for child in list(source):
        if child.tag == PATH_TAG:
            d = child.attrib.get("d", "").strip()
            if not d:
                continue
            ET.SubElement(target, PATH_TAG, {"d": d})
            count += 1
        elif child.tag == GROUP_TAG:
            name = semantic_group_name(child)
            if name:
                out_group = ET.SubElement(target, GROUP_TAG, {"data-part": name})
                child_count = copy_paths(child, out_group)
                if child_count == 0:
                    target.remove(out_group)
                count += child_count
            else:
                count += copy_paths(child, target)
        else:
            count += copy_paths(child, target)
    return count


def normalize(input_path: Path, output_path: Path) -> int:
    root = ET.parse(input_path).getroot()
    if root.tag != SVG_TAG:
        raise ValueError("root element must be svg")
    assert_supported(root)

    out_root = ET.Element(SVG_TAG, {"viewBox": "0 0 512 512"})
    style_group = ET.SubElement(out_root, GROUP_TAG, STYLE)
    path_count = copy_paths(root, style_group)
    if path_count == 0:
        raise ValueError("no path data found")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    tree = ET.ElementTree(out_root)
    ET.indent(tree, space="  ")
    tree.write(output_path, encoding="utf-8", xml_declaration=False)
    return path_count


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize line-art SVG into the Pilot style contract.")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        count = normalize(args.input, args.output)
    except (ET.ParseError, ValueError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: wrote {count} paths to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
