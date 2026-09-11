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
Remaining gates @ f0ed280          = CLOSED
  1. mid vs old-1.60x pullback     = PASS
  2. THINK pre|mid|diff @512       = PASS
  3. SVG SoT note                  = PASS
     SoT = pinned candidate commit candidates/.../*.svg git tree
     (not HVA evidence commit)

Over-emphasis HOLD                 = CLEARED (prior)
HVA PASS                           = DECLARED / CONSUMED
  HVA authority                    = 0362b17
  Evidence                         = f0ed280
  HVA record                       = b75f096
  scales                           = THINK/LOOK 1.30x · WRITE 1.20x
  Candidate SVG identities         = UNCHANGED

Authorized by prior HVA gate           = HVA PASS determination only
Accepted SVG Materialization Start     = GO / CONSUMED
Accepted SVG Materialization           = COMPLETE (namespaced assets/accepted/new-source-v1)
  authority                            = 0362b17
  materialized commit                  = 4c2ed6f
  paths                                = assets/accepted/new-source-v1/person-*.svg
ACTIVE archive source mutation         = NONE
Human ACTIVE Pin GO                    = GO / CONSUMED
ACTIVE SVG authority                   = assets/accepted/new-source-v1/person-*.svg
  pointer                              = assets/accepted/new-source-v1/active-authority.json
Historical accepted (#114) mutation    = HOLD / NOT MUTATED
candidate SVG mutation                 = HOLD / NOT MUTATED
Eye-scale stacked Merge (#142)         = GO / CONSUMED / COMPLETE @ 6c0070f
ACTIVE pin Merge / Promotion           = GO / CONSUMED (PR #143)
Deploy / Print / Publish               = HOLD
Agent visual substitution for HVA      = PROHIBITED

Human Merge / Promotion GO for ACTIVE pin PR #143 = GO / CONSUMED
Next = Deploy / Print / Publish — remain HOLD unless separately authorized
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

Human Visual Acceptance for these mid-point identities is **DECLARED** below. ACTIVE / materialize / merge remain separate and HOLD.

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

## Human decision points (fresh HVA)

1. @64: eyes remain visible without becoming facial protagonists? — accepted on mid
2. WRITE no longer overpowers face hierarchy? — accepted on mid (1.20x)
3. LOOK weight aligned with THINK? — accepted on mid (1.30x)
4. Gesture contracts intact? — accepted
5. Whole-character acceptance of these mid-point candidate identities? — accepted

## HVA decision

```text
HVA PASS = DECLARED / CONSUMED
candidate = 0362b1720649288db8bb4072bb9fefdba48e5363
evidence  = f0ed28024b8a08512e45dc1dcc2ceefbe1740ad5
scales    = THINK/LOOK 1.30x pre · WRITE 1.20x pre
```

Record: `eye-scale-hva-pass-declaration.json`.

## Explicitly NOT authorized by HVA PASS alone (historical note)

```text
Accepted SVG Materialization  — later authorized separately; COMPLETE
ACTIVE SVG pin                — later authorized by Human ACTIVE Pin GO; CONSUMED
existing HITOKOTO mutation
historical HVA / SVG SHA inheritance
ACTIVE archive PNG mutation   — still HOLD / NONE
backend selection change
ACTIVE pin Merge / Promotion  — HOLD (next separate GO)
Deploy / Print / Publish      — HOLD
```
