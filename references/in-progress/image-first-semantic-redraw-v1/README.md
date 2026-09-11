# IMAGE-FIRST-SEMANTIC-REDRAW-V1

Status: in-progress implementation candidate under Issue #86 / Review #87.

## Purpose

This lane uses image generation as a **semantic preprocessor** before classical centerline vectorization. It is intended for simple person line-art where direct tracing can preserve ambiguous gesture cues too faithfully.

```text
source reference
→ ChatGPT image semantic redraw
→ clean monoline raster
→ centerline extraction
→ SVG normalization
→ static structural/style evaluation
→ 512px / 64px render review
→ Human Semantic Gesture Review
```

Image generation is not treated as a vector backend and is not sufficient authority for a production-ready SVG.

## Repository scope

This implementation is self-contained under this directory. It does not modify PR #78, PR #84, existing fixture SVGs, Foundation, Pattern, Prompt promotion locations, CI, package files, or lockfiles.

## Files

- `prompts/semantic-redraw-v1.md` — reproducible redraw instruction template and semantic constraints.
- `prompts/pilot-three-gesture-sheet.md` — concrete three-panel pilot prompt shape.
- `fixtures/gesture-contracts.json` — machine-readable THINK / LOOK / WRITE semantic cues.
- `scripts/split_three_panel.py` — narrow 3:1 THINK / LOOK / WRITE sheet splitter.
- `scripts/centerline_vectorize.py` — monoline raster → skeleton/polyline → normalized SVG.
- `scripts/validate_svg.py` — fail-closed static style/structure checks.
- `scripts/render_review.py` — deterministic 512px / 64px Inkscape render helper.
- `evidence/local-proof.md` — initial proof result and interpretation.
- `evidence/implementation-replay.md` — replay evidence from the implementation candidate scripts.

## Local dependencies

The repository does not install or pin these dependencies in this pilot. A local execution environment needs:

```text
Python 3
Pillow
NumPy
scikit-image
Inkscape (only for render_review.py)
```

Missing local tooling must be reported as SKIP / unavailable, never silently counted as PASS.

## Example flow

```bash
python scripts/split_three_panel.py redraw-sheet.png panels/
python scripts/centerline_vectorize.py panels/person-thinking.png candidate-thinking.svg
python scripts/validate_svg.py candidate-thinking.svg
python scripts/render_review.py candidate-thinking.svg review-output/
```

Then review the 512px and 64px renders against the applicable semantic contract. Human semantic acceptance is a separate gate.

## SVG output contract

```text
viewBox          = 0 0 512 512
fill             = none
stroke           = currentColor
stroke-width     = 8
stroke-linecap   = round
stroke-linejoin  = round
```

No raster embedding, filter, mask, clipPath, gradients, or hard-coded paint colors are intended in normalized output.

## Gate model

```text
I1 Image semantic adequacy   = Human/visual evidence required
I2 SVG style validity        = static validator
I3 Structural editability    = metrics + Human review
I4 Render retention          = 512px + 64px
I5 Human Semantic Review     = mandatory
```

Any semantic failure is overall failure regardless of pixel similarity.

## Non-goals

This implementation does not authorize:

- replacing production/person assets
- re-pinning PR #78 fixtures
- replacing PR #84 candidates
- selecting a vector backend winner
- merging or promoting the lane
- CI/repository-wide dependency changes
