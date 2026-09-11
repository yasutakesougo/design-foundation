# IMAGE-FIRST-SEMANTIC-REDRAW-V1 — New Source Generation / Revalidation Evidence

## Authority

```text
Definition / Scope          = #121 / Human LOCKED
Fresh Definition Review     = #122 / PASS
New Source Selection        = #123 / GO / CONSUMED
Implementation              = #128 / Start GO / CONSUMED
New Source Archival         = ACTIVE
main retained ref           = 1abc391be2f526065b7e537901772481fe0595a2
Backend technical authority = 33b1de0949cfe434e6ee8d3424a5b0ba068aedd5
Implementation base         = 9c89366cb13d0643567308c962fbacce9967031f
Vectorizer blob SHA-1       = 43aadc02c72356af4e526713e85799e44e230f95
```

`9c89366...` contains the exact reviewed backend code plus the reviewed archive-only merge. It is not substituted for the historical Fresh Technical Review authority at exact `33b1de...`.

## Source

```text
archive path = references/in-progress/image-first-semantic-redraw-v1/archive/new-source-v1/source/redraw-sheet-think-look-write.png
Git blob      = c823556c5b4d6a8ce19ccf9c42c2c8480c2b24ad
PNG / RGB     = 2172 x 724 / 1,019,570 bytes
SHA-256       = e6ffa84ca72eb3ed3d6f27a69a53dcf4f4049a56cbc428b5a05b9d4afb5e7fcd
```

Locked splitter replay:

```text
THINK = 4feaf887cc138ff69e7063de26e64de81cce906505063e6772f3c6c17af41782
LOOK  = 1b304876815aa091ac5063bbd1693621fc53bab7643463d5f4b89aa314098cea
WRITE = 70b8b3a71526e81bf3d5202d848bfd1ff9832942ed03fc96eead6cfc54cc557c
```

## Backend / fallback

```text
selected backend       = SOURCE-GUIDED
actual backend         = SOURCE-GUIDED
fallback allowed       = false
fallback used          = false
primary failure reason = null
```

JOIN-CONTINUITY remains explicit-only fallback. It was not used in this run.

## Concrete generation parameters

```text
curve_mode      = curvature-aware-source-guided
mask_mode       = auto
min_green       = 70
dominance       = 18
dark_threshold  = 180
epsilon         = 1.35
min_path        = 4.0
linear_short    = 12.0
bezier_error    = 1.35
smooth_passes   = 2
smooth_weight   = 0.18
spline_tension  = 0.7
stroke_width    = 8
viewBox         = 0 0 512 512
```

## Runtime

```text
Python       = 3.13.5
NumPy        = 2.3.5
scikit-image = 0.26.0
Pillow       = 12.3.0
Platform     = Linux x86_64
Inkscape     = 1.4 / review rendering only
```

Cross-runtime byte determinism remains **NOT PROVEN**.

## Candidate outputs

```text
THINK SVG   = 01b5efbcdf7c4ba723074d87ed6ac9a15918f1ed9663c0774c88cec30d5f3de7
THINK metric= adcb9e9e66c05bc011501c29aaf685dd71bdc7f2ff13c3d6f07146afcf76123f
paths       = 66
validator   = PASS
5/5 same-runtime SVG bytes    = IDENTICAL
5/5 same-runtime metric bytes = IDENTICAL

LOOK SVG    = e3e68536b2122dbe35f18d15a93ad46f2c45150969ebca6a4d6522b0a5f7a5bb
LOOK metric = 38d9cc9549e1a2bb9c8ad18ebd1279d99817fc0c965dfa11d33a62aa4e36029d
paths       = 43
validator   = PASS
5/5 same-runtime SVG bytes    = IDENTICAL
5/5 same-runtime metric bytes = IDENTICAL

WRITE SVG   = 1a14ae867e2861f4684b85456f282246a68520c2c4834479cfdfe8cbe49e4e0c
WRITE metric= ae9351530b15c154555fccb2cc0bcbe3ed0702b695f5233a24cc46e82a298801
paths       = 66
validator   = PASS
5/5 same-runtime SVG bytes    = IDENTICAL
5/5 same-runtime metric bytes = IDENTICAL
```

WRITE is materialized as candidate filename `person-note-taking.svg`; the semantic mapping remains `WRITE -> person-note-taking`.

## Acceptance boundary

These are **new-source candidate outputs only**.

```text
Historical HVA inheritance       = PROHIBITED / NOT USED
Historical SVG SHA inheritance   = PROHIBITED / NOT USED
Human Visual Acceptance          = NOT STARTED
Accepted SVG Materialization     = HOLD / NOT AUTHORIZED
Existing HITOKOTO asset mutation = NONE
Consumer reference switching     = NONE
Merge to main                    = NOT AUTHORIZED
```

A later Human Visual Acceptance must review the new candidate bytes independently.
