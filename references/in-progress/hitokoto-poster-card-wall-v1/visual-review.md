# Card Wall V1｜Human Visual Review

## Current review target

`CARD-WALL-V1 Correction-6 — Illustrated Warmth / Participation Emphasis` の Human Visual Review 対象です。

Baseline exact HEAD:

`7258ead4c311d24c19b7f90b42f41f25b7f2cea9`

Human-selected direction:

- warmer / more approachable
- handwritten / illustrated liveliness
- lower psychological barrier to writing
- lived-in `ひとこと → ひとこと返し` feeling
- natural gaze guidance
- stronger CTA discovery

The supplied illustrated reference is **Design DNA / visual-direction evidence only**. Reference-only speech-bubble copy and generated QR pixels are not production content.

## Content authority — HARD LOCK

`content.md` remains authoritative and unchanged.

Content blob:

`6e9e6fa168976ed0f28882b783ae986d826ba1e5`

Repository QR blob:

`a68d1f558c96c4eecb6a7e81cb1e74c5c8cf0a52`

Repository QR reference:

`../hitokoto-poster-v3/assets/qr.png`

Fixed destination:

`https://hitokoto-kaeshi-preview.web.app/poster`

The following remain unchanged:

- `日常を、言葉に。`
- `気になったことを、ひとことだけ。`
- `正解は、ありません。`
- all four `ひとこと → ひとこと返し` pairs
- CTA wording
- reassurance / caution wording
- `広報部会（仮）`

## Correction-6 implementation

### Illustrated warmth

- three original inline line-art human placements plus one plant line-art accent
- scenes suggest noticing / thinking / responding without adding copy
- adult / workplace tone
- no mascot, chibi, real-person likeness, or disability stereotype
- illustration remains outside the primary reading hierarchy

### Handwritten / handmade energy

- stronger yellow marker treatment for title and CTA
- restrained hand-drawn accent strokes / dots / pale blobs
- card rotations and offsets increased modestly from Correction-5
- four tape-like attachment details use pale coral / blue / mint / yellow
- no full cork, wooden frame, or scrapbook treatment

### Exchange-board liveliness

- all four left-to-right mappings remain explicit
- semantic priority remains equal across the four examples
- card positions / paper tones / rotations vary more than Correction-5
- arrows remain central and unambiguous

### Participation-focused CTA

- CTA receives a warmer yellow-to-pale-mint field
- `QRからどうぞ` gets stronger marker emphasis
- QR display increases modestly to `31mm`
- white QR quiet zone remains clear
- CTA remains subordinate to title + exchange field

### Color / hierarchy

- deep green remains the anchor
- pale mint / blue / coral / warm yellow accents are more visible than Correction-5
- title remains first-glance focal point
- four exchanges remain the main body
- CTA is clearly discoverable without overtaking the exchanges

## Static verification

- required authoritative strings: **PASS**
- four `.pair` groups: **PASS / 4**
- repository QR reference unchanged: **PASS**
- long URL absent from poster surface: **PASS**
- reference-only speech-bubble copy absent: **PASS**
- remote font import: **none**
- title / CTA / caution strings: **PASS**

## A4 fixed-layout verification

Renderer: `WeasyPrint + rendered PNG inspection`

Result:

- page count: **1**
- page size: **A4 / 595.276 × 841.89 pt**
- clipping observed: **none**
- fragmentation observed: **none**
- visible overflow observed: **none**
- title first-glance hierarchy: **PASS**
- four pair mappings: **PASS**
- card text readability: **PASS**
- CTA discovery / hierarchy: **PASS**
- caution/footer readability: **PASS**
- QR quiet zone in layout: **PASS**
- awkward Japanese line break: **none observed**
- illustration does not obscure copy: **PASS**

No fresh Chromium PASS is claimed for Correction-6. Browser evidence remains supplementary under Issue #31 when the execution environment blocks it.

## Human visual questions

1. Correction-5より温かく、参加しやすく見えるか。
2. `きれいすぎて書きにくい` 感が下がったか。
3. 4組がシステムUIではなく、やりとりの掲示に見えるか。
4. 人物や手描きアクセントが視線誘導として自然か。
5. CTAが見つけやすく、押しつけがましくないか。
6. 大人向け / 職場向けの範囲に留まっているか。
7. 賑やかでも情報が読みやすいか。
8. 幼い / 装飾過多 / AIポスターっぽい方向へ振れていないか。

## Physical Validation

Still separate and not consumed:

- real A4 physical readability
- real-device QR scan
- destination readback

## Exact implementation scope

Correction-6 changes are limited to:

- `references/in-progress/hitokoto-poster-card-wall-v1/poster.html`
- `references/in-progress/hitokoto-poster-card-wall-v1/visual-review.md`

The following remain unchanged / out of scope:

- `content.md`
- `hitokoto-poster-v3/assets/qr.png`
- Accepted / Pattern / Prompt / Foundation content
- Print / Post / Deploy / Real Trial

## Gate state

- Correction-5: **SUPERSEDED CANDIDATE / historical evidence only**
- Correction-6 Definition / Scope: **GO / CONSUMED / LOCKED**
- Independent Definition / Scope Review: **PASS**
- Human Implementation Start: **GO / CONSUMED**
- Correction-6 implementation: **APPLIED**
- Static scope/content verification: **PASS**
- A4 fixed-layout verification: **PASS**
- Browser verification: **SUPPLEMENTARY / NO FRESH PASS CLAIMED**
- Correction-6 Human Ready: **REQUIRED / NOT YET CONSUMED**
- Human Visual Acceptance: **NOT DONE**
- Physical A4 / real-device QR: **NOT DONE**
- Merge / Print / Post / Deploy / Promotion: **HOLD**
