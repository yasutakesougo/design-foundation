#!/usr/bin/env python3
"""Create deterministic mild input variants for backend robustness evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output_dir", type=Path)
    args = ap.parse_args()
    image = Image.open(args.input).convert("RGB")
    w, h = image.size
    args.output_dir.mkdir(parents=True, exist_ok=True)
    variants = {
        "reencode": image.copy(),
        "brightnessplus3pct": ImageEnhance.Brightness(image).enhance(1.03),
        "resample98": image.resize((round(w * .98), round(h * .98)), Image.Resampling.LANCZOS).resize((w, h), Image.Resampling.LANCZOS),
        "blur0.35": image.filter(ImageFilter.GaussianBlur(.35)),
    }
    manifest = {
        "source": {"path": str(args.input), "sha256": sha256(args.input), "size": [w, h]},
        "variants": {},
    }
    for name, variant in variants.items():
        path = args.output_dir / f"{name}.png"
        if name == "reencode":
            variant.save(path, compress_level=9, optimize=True)
        else:
            variant.save(path)
        manifest["variants"][name] = {"path": str(path), "sha256": sha256(path), "size": list(variant.size)}
    target = args.output_dir / "manifest.json"
    target.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
