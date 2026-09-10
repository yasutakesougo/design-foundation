# EYE-SCALE-CORRECTION-V1 — Human Visual Acceptance Review Package

## Authority

```text
Definition PR = #135
Definition HEAD = 1e3591ca9c10eea6187192b5dc2cec87f785d1ac
Human Definition / Scope Lock = GO / CONSUMED
Human Implementation Start = GO / CONSUMED
Implementation PR = #142
Implementation candidate HEAD = 2eba5b1d4258e342e3c0f4547cda9d602291a1ea
Authorized pre-correction HEAD = fe037894ffad4eeb1e79dd6442214923afe8f3d5
Fresh Implementation Review = PASS
```

## Gate status for this package

```text
HVA Evidence Completion = IN PACKAGE
512px review materials = READY
64px review materials = READY
LOOK pre | corrected | diff = READY
WRITE pre | corrected | diff = READY
explicit @64 pre vs corrected THINK/LOOK/WRITE = READY
L/R eye scale parity verification = PASS (measurement)
Human Visual Acceptance PASS = NOT DECLARED / HOLD
Accepted SVG Materialization = HOLD
Merge / Promotion = HOLD
Deploy / Print / Publish = HOLD
ACTIVE source mutation = NONE
Agent visual substitution for HVA = PROHIBITED
```

This package prepares / completes fresh HVA evidence only. It does not declare HVA PASS or CORRECTION.

## Why this HVA package leaves candidate SVG bytes unchanged

```text
Implementation candidate identities were fixed at:
2eba5b1d4258e342e3c0f4547cda9d602291a1ea
```

The HVA package commits are **ADD-only review evidence** (renders, diffs, manifests, decision notes). They must not rewrite the SVG candidates under review, because:

1. Fresh HVA must judge the exact implementation candidate bytes already reviewed.
2. Changing SVG bytes inside an “HVA evidence” commit would create a new candidate identity and invalidate the Implementation HEAD pin.
3. Materialization / acceptance remain separate later gates; evidence completion is not materialization.

```text
candidates/new-source-v1/*.svg SHA-256 at package time
= identical to Implementation candidate HEAD 2eba5b1...
ACTIVE archive source bytes = untouched
```

## Corrected candidate identities

```text
THINK = candidates/new-source-v1/person-thinking.svg
LOOK  = candidates/new-source-v1/person-looking.svg
WRITE = candidates/new-source-v1/person-note-taking.svg
```

Exact SHA-256 values are recorded in `eye-scale-hva-review-manifest.json`.

Pre-correction identities at `fe037894...` remain comparison references only and are not acceptance authorities.

## Review materials

```text
*-pre-512.png / *-corrected-512.png
*-pre-64.png / *-corrected-64.png
*-pre-vs-corrected-512.png
*-pre-vs-corrected-64-nearest4x.png
*-eye-crop-pre-vs-corrected-512.png
*-pre-corrected-diff-512.png
*-eye-crop-pre-corrected-diff-512.png
*-explicit-64-pre-vs-corrected-native.png
*-explicit-64-pre-vs-corrected-nearest4x.png
all-roles-explicit-64-pre-vs-corrected-nearest4x.png
eye-scale-corrected-triptych-512.png
eye-scale-corrected-triptych-64-nearest4x.png
eye-scale-lr-parity.json
```

Required completion items:

```text
LOOK  pre | corrected | diff  = person-looking-*-pre-corrected-diff-512.png
WRITE pre | corrected | diff  = person-note-taking-*-pre-corrected-diff-512.png
explicit @64 THINK/LOOK/WRITE = *-explicit-64-pre-vs-corrected-*.png
```

## L/R eye scale parity verification

Measured on the exact eye paths recorded in the implementation evidence, comparing bbox-diagonal span pre → corrected:

```text
THINK left/right span ratios ≈ 1.600545 / 1.599830 ; rel_diff ≈ 0.000447
LOOK  near/far  span ratios ≈ 1.601131 / 1.600686 ; rel_diff ≈ 0.000278
WRITE left/right span ratios ≈ 1.599717 / 1.599681 ; rel_diff ≈ 0.000023
target scale ≈ 1.60
parity threshold = rel_diff <= 0.05
overall L/R parity measurement = PASS
```

Machine-readable detail: `eye-scale-lr-parity.json`.

This measurement is evidence for Human review. It is not an HVA PASS declaration.

## Human decision points

1. Are THINK / LOOK / WRITE eye marks sufficiently readable at 512px?
2. Do corrected eye marks remain practically detectable at explicit 64px?
3. Does LOOK retain both-eyes-open lateral gaze after enlargement?
4. Are non-eye gesture cues still intact (hand/face, head turn, pen/paper)?
5. Does eye scale remain quiet / adult monoline rather than oversized cartoon eyes?
6. Is L/R eye scale parity visually acceptable for each role?
7. Whole-character acceptance of the corrected candidate set?

## Decision options

```text
PASS / GO  — accept these exact corrected candidate SVG identities
CORRECTION — do not accept; state the visual concern
```

## Explicitly NOT authorized by this package

```text
Accepted SVG Materialization
existing HITOKOTO mutation
historical HVA / SVG SHA inheritance
ACTIVE archive mutation
backend selection change
Merge / Promotion
Deploy / Print / Publish
automatic / inferred Fresh HVA PASS
```
