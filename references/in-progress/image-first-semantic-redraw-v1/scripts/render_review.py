#!/usr/bin/env python3
"""Render a normalized SVG at the two Human review scales using Inkscape."""
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("svg", type=Path)
    ap.add_argument("output_dir", type=Path)
    args = ap.parse_args()

    exe = shutil.which("inkscape")
    if not exe:
        raise SystemExit("inkscape not found; render review is SKIP, not PASS")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for size in (512, 64):
        out = args.output_dir / f"{args.svg.stem}-{size}.png"
        subprocess.run([
            exe, str(args.svg),
            f"--export-filename={out}",
            f"--export-width={size}",
            f"--export-height={size}",
        ], check=True)
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
