# Local proof evidence

This file records the pre-repository proof that motivated IMAGE-FIRST-SEMANTIC-REDRAW-V1. It is evidence, not an automatic production asset promotion.

## Pipeline exercised

```text
reference line-art sheet
→ ChatGPT image semantic redraw
→ green semantic-stroke mask
→ skeletonize
→ polyline graph trace
→ RDP simplification
→ normalized currentColor SVG
→ 512px / 64px render review
```

## Semantic redraw target

Three figures were deliberately rendered together so that gesture differentiation could be judged in one sheet:

```text
THINK = hand-to-chin / cheek
LOOK  = modest head turn + visibly open lateral gaze
WRITE = notepad + long diagonal pen + writing hand + pen-paper contact
```

## Initial observed SVG path counts

```text
THINK = 63
LOOK  = 47
WRITE = 67
combined = 177
```

These values demonstrate that semantic cleanup can improve legibility before vectorization, but they do not demonstrate optimal editability. The hand-authored fixtures remain materially more compact.

## Interpretation

```text
semantic readability         = strong candidate
centerline conversion        = viable
style normalization          = viable
small-scale render retention = viable candidate
structural compactness       = unresolved optimization problem
Human Semantic Review        = required
```

No backend or production asset is selected by this evidence.
