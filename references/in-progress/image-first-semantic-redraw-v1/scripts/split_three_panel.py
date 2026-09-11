#!/usr/bin/env python3
"""Split the locked 3:1 THINK / LOOK / WRITE redraw sheet into three panels.

This helper is intentionally narrow: it exists to reproduce the pilot evidence
shape, not as a general-purpose image cropper.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image

NAMES = ("person-thinking", "person-looking", "person-writing")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output_dir", type=Path)
    args = ap.parse_args()

    image = Image.open(args.input).convert("RGB")
    if image.width < image.height * 2.5:
        raise SystemExit("expected a wide 3-panel redraw sheet")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    bounds = [round(image.width * i / 3) for i in range(4)]
    for i, name in enumerate(NAMES):
        panel = image.crop((bounds[i], 0, bounds[i + 1], image.height))
        out = args.output_dir / f"{name}.png"
        panel.save(out)
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
