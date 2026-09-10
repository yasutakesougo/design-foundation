# EYE-SCALE-CORRECTION-V1 — Human Visual Acceptance Review Package

## Authority

```text
Definition PR = #135
Definition HEAD = 1e3591ca9c10eea6187192b5dc2cec87f785d1ac
Human Definition / Scope Lock = GO / CONSUMED
Human Implementation Start = GO / CONSUMED
Implementation PR = #142
Implementation HEAD = 2eba5b1d4258e342e3c0f4547cda9d602291a1ea
Authorized pre-correction HEAD = fe037894ffad4eeb1e79dd6442214923afe8f3d5
Fresh Implementation Review = PASS
```

## Gate status for this package

```text
512px review materials = READY
64px review materials = READY
Human Visual Acceptance PASS = NOT DECLARED / HOLD
Accepted SVG Materialization = HOLD
Merge / Promotion = HOLD
Deploy / Print / Publish = HOLD
Agent visual substitution for HVA = PROHIBITED
```

This package prepares fresh HVA materials only. It does not declare HVA PASS/CORRECTION.

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
eye-scale-corrected-triptych-512.png
eye-scale-corrected-triptych-64-nearest4x.png
```

## Human decision points

1. Are THINK / LOOK / WRITE eye marks sufficiently readable at 512px?
2. Do corrected eye marks remain practically detectable at 64px?
3. Does LOOK retain both-eyes-open lateral gaze after enlargement?
4. Are non-eye gesture cues still intact (hand/face, head turn, pen/paper)?
5. Does eye scale remain quiet / adult monoline rather than oversized cartoon eyes?
6. Whole-character acceptance of the corrected candidate set?

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
```
