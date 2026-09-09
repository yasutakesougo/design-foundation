# Evaluation Contract

## Gate model

Every reconstructed candidate is evaluated by hard gates.

```text
G1 SVG VALID
↓
G2 STYLE VALID
↓
G3 STRUCTURE ACCEPTABLE
↓
G4 VISUAL ACCEPTABLE
↓
G5 SEMANTIC GESTURE PASS
↓
Candidate PASS
```

No averaged score may turn a mandatory gate failure into PASS.

## G1 — SVG validity

PASS requires all of the following.

```text
XML parse succeeds
root element is svg
viewBox is present
at least one path is present
candidate can be handed to the configured renderer
```

## G2 — Style validity

The normalized candidate must satisfy:

```text
viewBox          = 0 0 512 512
fill             = none
stroke           = currentColor
stroke-width     = 8
stroke-linecap   = round
stroke-linejoin  = round
```

Hard-coded paint colors, filters, masks, or clip paths are rejected unless a later scope explicitly allows them.

## G3 — Structural acceptability

Record at minimum:

```text
path_count
segment_token_count
very_short_path_count
transform_count
semantic_group_count
anonymous_group_count
```

The Pilot does not define one universal numeric threshold for editability.

The evidence must make fragmentation and giant-path collapse visible for Human review.

A candidate should remain repairable by changing a meaningful component without rebuilding the full figure.

## G4 — Visual acceptability

When a deterministic rasterizer and image metric implementation are available, record:

```text
512px raster difference
64px raster difference
SSIM where available
optional LPIPS where explicitly configured
```

If a metric is unavailable, report `NOT_MEASURED` rather than inventing a score.

Visual similarity alone never produces overall PASS.

## G5 — Semantic Gesture Check

The semantic cue checklist is mandatory.

```text
WRITE = paper + pen + writing interaction
THINK = hand-to-face + visible forearm
LOOK  = head direction + lateral gaze + face direction
```

Automation may assist this check, but Human-reviewable 512px and 64px evidence remains required before Human Visual Acceptance.

The initial implementation records semantic status as one of:

```text
PASS
FAIL
REQUIRES_HUMAN
```

A future vision-model judge must not overwrite Human review authority.

## Overall result

```text
mandatory gate FAIL          → FAIL
mandatory gate not measured  → INCOMPLETE
all mandatory gates PASS     → PASS candidate for Human review
```

`INCOMPLETE` is not a failure hidden as success.

It means the implementation or local environment did not produce enough evidence for the next gate.

## Backend comparison

Both initial backends must use the same pinned fixtures and report the same fields.

```text
A = autotrace-centerline
B = skeleton-polyline
```

No backend becomes default until evidence is compared.

## Preprocessing comparison

Where implemented, preprocessing variants are labeled rather than silently applied.

```text
raw-denoise
light-open-close
morphology-variant
```

Any variant that merges a high-risk semantic junction is rejected even when a raster metric improves.

High-risk junctions include:

```text
hand ↔ face
pen ↔ paper
arm ↔ torso
hair ↔ hand
```
