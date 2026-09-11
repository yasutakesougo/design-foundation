# IMAGE-FIRST semantic redraw prompt v1

Use this prompt only for the semantic-redraw stage. The generated image is an intermediate raster, not an accepted SVG asset.

## Prompt template

> Redraw the supplied simple person illustration as clean SVG-friendly monoline art while preserving the intended gesture: **{{GESTURE}}**.
>
> Semantic cues that must remain unmistakable: **{{REQUIRED_CUES}}**.
>
> Use one deep-green line color on a plain light background. Use visually uniform stroke weight, rounded line caps, rounded joins, smooth curves, no shading, no gradients, no textures, no decorative background, and no text. Keep the figure mature, simple, quiet, and not overly cute. Reduce incidental detail when it competes with the gesture. Do not add scene objects unless they are required by the semantic cues.
>
> Optimize the redraw for later centerline vectorization: prefer separated, continuous strokes; avoid fuzzy brush edges, dense cross-hatching, tiny decorative marks, filled black regions, and near-touching parallel lines that could merge during skeletonization.
>
> The gesture must remain understandable without a filename or caption and must still read when the result is reduced to small icon size.

## Gesture contracts used in the pilot

### THINK

`hand touching chin or cheek + visible forearm + readable thinking pose`

### LOOK

`modest head turn + both eyes visibly open + lateral gaze in the same direction + face direction supports gaze`

### WRITE

`notepad/paper + one long diagonal pen + writing hand + pen tip visibly meets paper`

## Negative constraints

- no text labels
- no UI or poster composition
- no photographic rendering
- no filled silhouette treatment
- no multiple line colors
- no eye closure for LOOK
- no ambiguous stray short mark standing in for the WRITE pen

## Human boundary

The image stage may clarify semantics, but it cannot consume Human Semantic Gesture Review. A generated redraw that looks attractive but weakens the required gesture is a failure.
