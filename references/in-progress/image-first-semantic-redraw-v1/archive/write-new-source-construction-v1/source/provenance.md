# WRITE-NEW-SOURCE-CONSTRUCTION-V1 — Candidate B Provenance

## Candidate identity

```text
workstream = WRITE-NEW-SOURCE-CONSTRUCTION-V1
candidate = Candidate B
attempt = 2
status = HUMAN-REVIEWED CANDIDATE / NON-AUTHORITATIVE
format / mode / size = PNG / RGB / 2172 x 724
candidate source SHA-256 = 880372c667632ff35eafd059ce93652293a359abf1bf3799f7c4638e7e8a07b1
bytes = 941179
expected Git blob SHA-1 = 26960783f79506d2556c633c759d26659387765f
```

## Deterministic panel split

```text
THINK = x[0:724], y[0:724]
LOOK  = x[724:1448], y[0:724]
WRITE = x[1448:2172], y[0:724]

THINK SHA-256 = 63e7ea65121a2a6afff036dfa27df03cd3217cccf34fa5aef35687e5a4ba7eb0
LOOK  SHA-256 = fdb3f6fe5c06f70d2f403347de7558828f0353d9657be573829dc7ca1d266f2b
WRITE SHA-256 = 4e10857690e8f5ae4d45265494ecda63deed3187954295f1f8451f1d597428e6
```

## Review derivatives

512px and 64px evidence were produced from each exact 724 x 724 panel using Pillow LANCZOS with no crop or other image correction.

```text
THINK 512 SHA-256 = 88b676ad99d9d6702240d0440c8328f895e3e1b037b19f221d5f0cc2ff16a1c4
THINK  64 SHA-256 = 3cd28844d8cec90e5c5a330e7a274490f7f7143140fa9ff2cd11ce2104ebf4e8

LOOK 512 SHA-256 = e12fd88cfdf165da1c180da21cede922f7d0af2051b8137ccfad74b1799326d1
LOOK  64 SHA-256 = e8bf7e90faa35c3351f276f75f258890c6216899ee6db2cd513d8af8a563d4bf

WRITE 512 SHA-256 = dda689832095f19bfebbceb64dcf0236967982fa8b8a440fa01e40407d78a4fe
WRITE  64 SHA-256 = 1f913afc7799b7a79385b7f98d10e8199df56eeec5015f957ed70b2e4255ec5a
```

## Generation evidence

```text
runtime-visible generation id = b235a6d0-66f8-4e7b-9e13-85515a71c8e7
parent generation id = null
```

Generation instruction used for Candidate B:

> A clean, white triptych in a flat minimalist vector style features three evenly spaced green line-art characters with no text, shading, or extra objects. From left to right: a smiling young man thoughtfully touching his chin, a cheerful young man gazing upward with idea-like accent marks, and a calm young woman taking notes in a spiral notebook with a pen, all rendered in consistent strokes with ample whitespace.

Reference context: the current active green triptych was used as the visual/style baseline in the locked workstream. Candidate B is an independently generated candidate and is not claimed to inherit active-source pixels.

## Style guardrail evidence

```text
representative green median ≈ RGB (5, 143, 79)
median hue distance from active baseline ≈ 0.00489 <= 0.015 = PASS

median stroke width:
THINK = 12.65 px = PASS
LOOK  = 12.65 px = PASS
WRITE = 12.65 px = PASS

ink density:
THINK = 0.07476 = PASS
LOOK  = 0.07917 = PASS
WRITE = 0.10123 = PASS

whole-sheet near-white coverage = 0.90615 >= 0.85 = PASS
```

Metrics are guardrails only and do not replace Human semantic/family acceptance.

## Semantic / Human review evidence

```text
Candidate B Agent Preflight = PASS / REVIEW-CLEARED
#202 preflight record = comment 5634576743

THINK semantics = PASS
LOOK semantics = PASS
WRITE semantics = PASS
64px survival = PASS
Illustration family = PASS

Fresh Human Semantic / Family Review = PASS / CONSUMED
#202 Human PASS record = comment 5634700189
```

WRITE continues to inherit the locked #190 semantic principle:

```text
stable writing plane
→ wrist / hand mechanics
→ pen control
→ pen-to-paper contact
→ writing trajectory
```

## Active authority remains unchanged before adoption

```text
current active source workstream = #128
current active source SHA-256 = e6ffa84ca72eb3ed3d6f27a69a53dcf4f4049a56cbc428b5a05b9d4afb5e7fcd
current active source status = ACTIVE / UNCHANGED
Candidate B status = NON-AUTHORITATIVE until explicit Source Adoption / Revalidation Human GO
```

## Current-Main Reconciliation

```text
old baseline = 1508ea20875147f9ad92230501121a71631e9650
current main = 938883f009bc09fb566f3c49cb03aca0b0168d91
delta        = DESIGN-FOUNDATION-CONSISTENCY-CORRECTION-V1 (#205)
verdict      = RECONCILED / new blocker = 0

Definition / locked scope semantics = still valid
candidate archive target paths      = still valid
#128 source authority               = unchanged
references/accepted relocation conflict = 0
```

## Scoped repository destination

```text
branch = cursor/write-new-source-candidate-b-materialization-a4d9
base main = 938883f009bc09fb566f3c49cb03aca0b0168d91
Lifecycle-Issue = #202
Blocker-Review = #207

references/in-progress/image-first-semantic-redraw-v1/archive/write-new-source-construction-v1/source/redraw-sheet-think-look-write.png
references/in-progress/image-first-semantic-redraw-v1/archive/write-new-source-construction-v1/source/provenance.md
```

Only these two ADD-only paths are authorized for candidate materialization in this slice.

Exact Candidate B PNG bytes were delivered via the Human-supplied materialization package and copied without regenerate / recompress / convert.

## Adoption boundary

This provenance record does not adopt Candidate B.

Source authority may change only after exact repository bytes are read back, the candidate SHA-256 and panel identities are verified, the two-file-only boundary is confirmed, and the explicit Source Adoption / Revalidation Human Gate is consumed.
