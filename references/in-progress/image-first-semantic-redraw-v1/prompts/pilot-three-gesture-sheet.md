# Pilot three-gesture semantic-redraw prompt

This is the concrete prompt shape used for the initial IMAGE-FIRST pilot. The image output is intermediate evidence; it is not itself an SVG asset or a deterministic build artifact.

> Create a clean SVG-friendly redraw of the supplied simple person illustrations. Preserve the overall order and meaning of the three figures: left = thinking with a hand resting against the cheek/chin, center = looking to the side with a modest head turn and clearly open eyes showing lateral gaze, right = writing while holding a notepad with one hand and a clearly visible long diagonal pen making contact with the paper.
>
> Redraw them as crisp, minimalist vector-style line art that looks easy to convert into clean SVG paths. Use a single deep green stroke color only, with no fills, visually uniform stroke width, rounded line caps, rounded line joins, simple smooth curves, and minimal but clear facial features. Keep the design quiet, modern, mature, and uncluttered. Make the gesture cues unambiguous, especially the writing action and the sideways gaze.
>
> Present the three figures side by side with ample spacing on a plain light background and no text or decorative elements.

## Expected order

```text
panel 1 = THINK
panel 2 = LOOK
panel 3 = WRITE
```

## Important limitation

Image generation is not deterministic. Reproduction means preserving the prompt contract and evaluation procedure, not expecting pixel-identical redraws from repeated generations.
