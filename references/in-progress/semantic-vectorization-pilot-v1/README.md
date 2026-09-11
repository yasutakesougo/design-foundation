# SEMANTIC-VECTORIZATION-PILOT-V1

## Status

```text
Definition / Scope          = LOCKED / CONSUMED
Fresh Definition Review    = PASS / CONSUMED
Human Implementation Start = GO / CONSUMED
Implementation             = IN PROGRESS
Merge / Promotion          = HOLD
```

## Purpose

This Pilot evaluates whether simple person-line illustrations can be reconstructed from raster inputs into editable SVG without losing gesture meaning.

The target is not generic image vectorization.

The target is a controlled semantic line-art pipeline for the current adult-facing person illustration style.

## Fixed fixture source

Implementation evidence is pinned to the current `HITOKOTO-PERSON-LINE-STYLE-V1` PR fixture source.

```text
Source PR   = #71
Source HEAD = 4acdefca152dd3f4fd1c69424b3f4f79f9b78004
```

The original fixture SVGs are never mutated by this Pilot.

Copies under `fixtures/source-svg/` are treated as immutable local ground truth.

## Initial implementation file set

```text
references/in-progress/semantic-vectorization-pilot-v1/
├─ README.md
├─ fixture-contract.md
├─ evaluation-contract.md
├─ fixtures/
│  ├─ manifest.json
│  └─ source-svg/
│     ├─ person-note-taking.svg
│     ├─ person-thinking.svg
│     └─ person-looking.svg
├─ scripts/
│  ├─ validate_fixture.py
│  ├─ normalize_svg.py
│  ├─ evaluate_svg.py
│  └─ run_baseline.py
└─ results/
   └─ README.md
```

No repository-level dependency file, lockfile, CI file, Foundation, Pattern, Prompt, or production SVG is changed.

## Pipeline

```text
canonical SVG fixture
→ deterministic raster render
→ centerline backend
→ SVG normalization
→ structural / visual evaluation
→ Semantic Gesture Check
```

The first comparison requires two centerline families.

```text
Backend A = AutoTrace centerline
Backend B = skeletonization + polyline tracing
```

The scripts intentionally keep these tools optional and local.

They do not install or download executables.

## Responsibility split

```text
vision model      = semantic parts / relations / gesture judgment
image processing  = image-space evidence
geometry code     = centerline / polyline / Bézier reconstruction
normalizer        = deterministic SVG style contract
human review      = final visual and semantic acceptance
```

The first baseline does not authorize a VLM to invent final SVG path coordinates.

## Normalized SVG contract

Generated candidates must converge on this shared structure where applicable.

```text
viewBox          = 0 0 512 512
fill             = none
stroke           = currentColor
stroke-width     = 8
stroke-linecap   = round
stroke-linejoin  = round
```

Semantic groups may remain when they improve editability.

Exporter-only groups and unsupported paint structures should be removed or rejected where safe.

## Evaluation gates

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

A semantic failure cannot be overridden by a high visual-similarity score.

## Local dependency boundary

This Pilot may use already-installed local tools when available.

Expected optional tools include:

```text
autotrace
rsvg-convert or another deterministic SVG rasterizer
Python image / morphology libraries
skeleton-tracing compatible executable or adapter
```

The baseline runner detects missing tools and reports `SKIP` rather than installing dependencies.

Repository-wide dependency changes remain outside the locked scope.

## Current boundary

```text
existing 3 source SVG mutation = FORBIDDEN
remaining 7 person SVGs        = HOLD
foundations/*                   = HOLD
patterns/*                      = HOLD
prompts/*                       = HOLD
runtime / Canva / Notion        = HOLD
CI mutation                     = HOLD
Merge / Promotion               = HOLD
```

The next gate after implementation evidence is a Fresh Implementation / Scope Review.
