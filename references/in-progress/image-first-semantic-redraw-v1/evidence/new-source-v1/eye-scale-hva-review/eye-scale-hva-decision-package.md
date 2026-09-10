# EYE-SCALE-CORRECTION-V1 — Human Visual Acceptance Review Package

## Authority

```text
Definition PR = #135
Definition HEAD = 1e3591ca9c10eea6187192b5dc2cec87f785d1ac
Human Definition / Scope Lock = GO / CONSUMED
Human Implementation Start = GO / CONSUMED
Implementation PR = #142
Authorized pre-correction HEAD = fe037894ffad4eeb1e79dd6442214923afe8f3d5
Prior 1.60x candidate HEAD = 2eba5b1d4258e342e3c0f4547cda9d602291a1ea
Fresh Implementation Review (1.60x) = PASS
```

## Gate status for this package

```text
Over-emphasis HOLD = CLEARED (mid-point candidates @ 0362b17)
  THINK/LOOK = 1.30x pre — OK
  WRITE      = 1.20x pre — OK (extra pullback justified)
HVA PASS = NOT DECLARED
ACTIVE / materialize / merge = HOLD
HVA Evidence Completion = READY
Deploy / Print / Publish = HOLD
ACTIVE source mutation = NONE
Agent visual substitution for HVA = PROHIBITED
```

## Prior Over-emphasis HOLD (cleared on mid)

```text
Over-emphasis at @64 (WRITE severe, LOOK moderate); eye weight exceeds facial stroke hierarchy. Reduce scale toward mid-point between pre and current corrected.
```

Cleared against mid-point candidates `0362b17` / package `98374f6` after Human review: hierarchy break no longer holds at THINK/LOOK 1.30x and WRITE 1.20x.

## Remediation applied in this revision (candidate only)

```text
basis = pre geometry at fe037894...
THINK / LOOK target = 1.30x pre   (mid-point between 1.00 and 1.60)
WRITE target         = 1.20x pre   (one step back from mid-point)
LOOK / WRITE aligned toward THINK visual weight intent
stroke-width = 8 unchanged
non-eye geometry = unchanged
ACTIVE archive = unchanged
```

Exact machine record: `eye-scale-midpoint-revision.json`.

This revision creates **new candidate identities**. It does not declare Fresh HVA PASS.

## Why earlier HVA evidence commits left 1.60x SVG bytes unchanged

Evidence-only commits must not rewrite the pinned Implementation candidate under review. Changing SVG bytes inside an evidence commit would silently create a new identity. The mid-point reduction below is an explicit candidate revision after HOLD guidance, recorded separately from the 1.60x Implementation HEAD.

## Corrected candidate identities (mid-point revision)

```text
THINK = candidates/new-source-v1/person-thinking.svg
LOOK  = candidates/new-source-v1/person-looking.svg
WRITE = candidates/new-source-v1/person-note-taking.svg
```

Exact SHA-256 values are in `eye-scale-hva-review-manifest.json`.

## Review materials

```text
*-pre-512.png / *-corrected-512.png
*-pre-64.png / *-corrected-64.png
*-pre-vs-corrected-512.png
*-pre-corrected-diff-512.png
*-eye-crop-pre-corrected-diff-512.png
*-explicit-64-pre-vs-corrected-native.png
*-explicit-64-pre-vs-corrected-nearest4x.png
all-roles-explicit-64-pre-vs-corrected-nearest4x.png
eye-scale-corrected-triptych-512.png
eye-scale-midpoint-revision.json
eye-scale-lr-parity.json   # prior 1.60x measurement retained for audit
```

## Human decision points (fresh HVA, still required)

1. @64: eyes remain visible without becoming facial protagonists?
2. WRITE no longer overpowers face hierarchy?
3. LOOK weight aligned with THINK?
4. Gesture contracts intact?
5. Whole-character acceptance of these mid-point candidate identities?

## Decision options

```text
PASS / GO  — accept these exact mid-point candidate SVG identities
CORRECTION — do not accept; state the visual concern
```

## Explicitly NOT authorized

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
