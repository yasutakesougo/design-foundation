#!/usr/bin/env python3
"""Convert a clean monoline redraw raster into normalized centerline SVG.

This intentionally assumes the image-generation stage has already simplified the
illustration. It is not a general photo vectorizer.

Optional local dependencies (not repository-managed):
    pillow
    numpy
    scikit-image
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import numpy as np
from PIL import Image
from skimage.morphology import skeletonize

Point = tuple[int, int]

NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1),
]


def semantic_stroke_mask(
    image: Image.Image,
    *,
    mode: str = "auto",
    min_green: int = 70,
    dominance: int = 18,
    dark_threshold: int = 180,
) -> np.ndarray:
    """Extract a clean monoline stroke from a light background.

    `green` selects the deep-green semantic redraw used in the proof. `dark`
    supports an equivalent black-on-white intermediate. `auto` accepts either
    while still rejecting a plain light background.
    """
    rgb = np.asarray(image.convert("RGB"), dtype=np.int32)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    green = (g >= min_green) & ((g - r) >= dominance) & ((g - b) >= dominance)
    luminance = (299 * r + 587 * g + 114 * b) / 1000.0
    dark = luminance <= dark_threshold
    if mode == "green":
        return green
    if mode == "dark":
        return dark
    if mode == "auto":
        return green | dark
    raise ValueError(f"unsupported mask mode: {mode}")


def build_graph(skel: np.ndarray) -> tuple[set[Point], dict[Point, list[Point]]]:
    ys, xs = np.nonzero(skel)
    nodes: set[Point] = {(int(x), int(y)) for x, y in zip(xs, ys)}
    graph: dict[Point, list[Point]] = {}
    for x, y in nodes:
        adjacent: list[Point] = []
        for dx, dy in NEIGHBORS:
            q = (x + dx, y + dy)
            if q in nodes:
                adjacent.append(q)
        graph[(x, y)] = adjacent
    return nodes, graph


def edge(a: Point, b: Point) -> tuple[Point, Point]:
    return (a, b) if a <= b else (b, a)


def trace_polylines(skel: np.ndarray) -> list[list[Point]]:
    nodes, graph = build_graph(skel)
    if not nodes:
        return []

    visited: set[tuple[Point, Point]] = set()
    key_nodes = sorted(p for p in nodes if len(graph[p]) != 2)
    paths: list[list[Point]] = []

    def walk(start: Point, nxt: Point) -> list[Point]:
        path = [start, nxt]
        visited.add(edge(start, nxt))
        prev, cur = start, nxt
        while len(graph[cur]) == 2:
            candidates = [q for q in graph[cur] if q != prev]
            if not candidates:
                break
            q = candidates[0]
            e = edge(cur, q)
            if e in visited:
                break
            path.append(q)
            visited.add(e)
            prev, cur = cur, q
        return path

    for p in key_nodes:
        for q in sorted(graph[p]):
            if edge(p, q) not in visited:
                paths.append(walk(p, q))

    for p in sorted(nodes):
        for q in sorted(graph[p]):
            if edge(p, q) in visited:
                continue
            loop = [p, q]
            visited.add(edge(p, q))
            prev, cur = p, q
            while True:
                candidates = [n for n in graph[cur] if n != prev]
                if not candidates:
                    break
                nxt = candidates[0]
                e = edge(cur, nxt)
                if e in visited:
                    break
                loop.append(nxt)
                visited.add(e)
                prev, cur = cur, nxt
            paths.append(loop)
    return paths


def _perpendicular_distance(p: Point, a: Point, b: Point) -> float:
    if a == b:
        return float(np.hypot(p[0] - a[0], p[1] - a[1]))
    ax, ay = a
    bx, by = b
    px, py = p
    num = abs((by - ay) * px - (bx - ax) * py + bx * ay - by * ax)
    den = float(np.hypot(by - ay, bx - ax))
    return num / den


def rdp(points: list[Point], epsilon: float) -> list[Point]:
    if len(points) <= 2:
        return points
    a, b = points[0], points[-1]
    distances = [_perpendicular_distance(p, a, b) for p in points[1:-1]]
    if not distances:
        return [a, b]
    max_i = int(np.argmax(distances))
    max_d = distances[max_i]
    if max_d <= epsilon:
        return [a, b]
    split = max_i + 1
    left = rdp(points[: split + 1], epsilon)
    right = rdp(points[split:], epsilon)
    return left[:-1] + right


def remove_short(paths: Iterable[list[Point]], min_pixels: float) -> list[list[Point]]:
    kept: list[list[Point]] = []
    for path in paths:
        if len(path) < 2:
            continue
        length = sum(float(np.hypot(b[0] - a[0], b[1] - a[1])) for a, b in zip(path, path[1:]))
        if length >= min_pixels:
            kept.append(path)
    return kept


def svg_for(paths: list[list[Point]], width: int, height: int, *, viewbox: int = 512, stroke_width: int = 8) -> str:
    scale = min(viewbox / width, viewbox / height)
    ox = (viewbox - width * scale) / 2.0
    oy = (viewbox - height * scale) / 2.0

    def fmt(v: float) -> str:
        rounded = round(v, 2)
        return str(int(rounded)) if rounded.is_integer() else f"{rounded:.2f}".rstrip("0").rstrip(".")

    elems: list[str] = []
    for path in paths:
        pts = [(ox + x * scale, oy + y * scale) for x, y in path]
        d = "M " + " L ".join(f"{fmt(x)} {fmt(y)}" for x, y in pts)
        elems.append(f'    <path d="{d}"/>')

    body = "\n".join(elems)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {viewbox} {viewbox}">\n'
        f'  <g fill="none" stroke="currentColor" stroke-width="{stroke_width}" '
        'stroke-linecap="round" stroke-linejoin="round">\n'
        f'{body}\n'
        '  </g>\n'
        '</svg>\n'
    )


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path)
    p.add_argument("output", type=Path)
    p.add_argument("--mask-mode", choices=("auto", "green", "dark"), default="auto")
    p.add_argument("--min-green", type=int, default=70)
    p.add_argument("--dominance", type=int, default=18)
    p.add_argument("--dark-threshold", type=int, default=180)
    p.add_argument("--epsilon", type=float, default=1.35, help="RDP simplification in source pixels")
    p.add_argument("--min-path", type=float, default=4.0, help="drop traced fragments shorter than this source-pixel length")
    p.add_argument("--stroke-width", type=int, default=8)
    args = p.parse_args()

    image = Image.open(args.input)
    mask = semantic_stroke_mask(
        image,
        mode=args.mask_mode,
        min_green=args.min_green,
        dominance=args.dominance,
        dark_threshold=args.dark_threshold,
    )
    if not mask.any():
        raise SystemExit("no semantic stroke pixels found")
    skel = skeletonize(mask)
    paths = trace_polylines(skel)
    paths = remove_short(paths, args.min_path)
    paths = [rdp(path, args.epsilon) for path in paths]
    paths = [path for path in paths if len(path) >= 2]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(svg_for(paths, image.width, image.height, stroke_width=args.stroke_width), encoding="utf-8")
    print(f"paths={len(paths)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
