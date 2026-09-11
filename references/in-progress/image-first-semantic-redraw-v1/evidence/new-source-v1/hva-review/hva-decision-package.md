# IMAGE-FIRST-SEMANTIC-REDRAW-V1 — New Source Human Visual Acceptance Package

## Gate

```text
Human Visual Acceptance Start GO = GO / CONSUMED
PR = #129
Authorized candidate HEAD = fe037894ffad4eeb1e79dd6442214923afe8f3d5
Fresh Implementation Review = PASS
Human Visual Acceptance declaration = NOT DECLARED / AWAITING HUMAN DECISION
```

This package opens Human Visual Acceptance for the exact new-source candidate bytes only. It does not declare acceptance.

## Exact candidates under review

```text
THINK = candidates/new-source-v1/person-thinking.svg
      SHA-256 = 01b5efbcdf7c4ba723074d87ed6ac9a15918f1ed9663c0774c88cec30d5f3de7

LOOK  = candidates/new-source-v1/person-looking.svg
      SHA-256 = e3e68536b2122dbe35f18d15a93ad46f2c45150969ebca6a4d6522b0a5f7a5bb

WRITE = candidates/new-source-v1/person-note-taking.svg
      SHA-256 = 1a14ae867e2861f4684b85456f282246a68520c2c4834479cfdfe8cbe49e4e0c
```

```text
backend = SOURCE-GUIDED
fallback_used = false
validator = 3/3 PASS
Historical HVA inheritance = PROHIBITED
Historical accepted SVG SHA inheritance = PROHIBITED
```

## Preconditions already satisfied

```text
Definition / Scope #121 = Human LOCKED
Fresh Definition Review #122 = PASS
New Source Selection #123 = GO / CONSUMED
New Source Archival Authority = ACTIVE
Generation / Revalidation Implementation #128 = Start GO / CONSUMED
Fresh Generation / Revalidation Implementation Review = PASS
ACTIVE source + locked splitter identity = MATCH
```

## Review materials in this directory

```text
*-512.png                              candidate render @ 512
*-64.png                               candidate render @ 64
*-source-panel-512.png                 ACTIVE source panel @ 512
*-source-vs-candidate-512.png          source | candidate comparison
new-source-v1-candidates-triptych-512.png
new-source-v1-candidates-triptych-64-nearest4x.png
hva-review-manifest.json
```

Render helper = `scripts/render_review.py` via Inkscape (review-only).

## Human visual decision points

Per Definition #121 Visual revalidation contract, review each role and the set as a whole:

1. Semantic gesture readability for THINK / LOOK / WRITE
2. Source fidelity
3. Line / curve smoothness
4. Long-contour continuity
5. Endpoint / stroke consistency
6. Practical 64px appearance
7. Whole-character acceptance

Historical HVA may be comparison evidence only and must not be inherited.

## Decision

Human Visual Acceptance may be either:

```text
PASS / GO     — accept these exact candidate SVG identities
CORRECTION    — do not accept; state the visual concern and return to correction scope
```

## Explicitly NOT authorized by this package or by HVA Start GO

```text
Accepted SVG Materialization
replacement/mutation of historical accepted SVGs
existing HITOKOTO asset mutation
consumer reference switching
structural compaction
Foundation / Pattern promotion
Merge / Promotion
Deploy / Print / Publish
```

Even if Human Visual Acceptance later = PASS, Accepted SVG Materialization and Merge remain separate gates.
