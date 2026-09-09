# Card Wall V1｜Human Visual Review

## Current review target

`CARD-WALL-V1 Correction-5 — Visual Hierarchy / Warmth Refinement` の Human Visual Review 対象です。

Baseline exact HEAD:

`0e795a15e5d4dc8d44bad24999cc9009655c8122`

Human feedback:

> 方向性は良いけど、メリハリが無いデザインで素っ気ない印象

Correction-5 は Direction B を維持し、**視覚的な強弱と温度感だけ**を調整します。

評価順序は次のままです。

1. `日常を、言葉に。`
2. 4組の `ひとこと → ひとこと返し`
3. CTA + real QR
4. reassurance / caution
5. supporting illustration / decoration

## Content authority — HARD LOCK

`content.md` は正本のままです。

Content blob:

`6e9e6fa168976ed0f28882b783ae986d826ba1e5`

Repository QR blob:

`a68d1f558c96c4eecb6a7e81cb1e74c5c8cf0a52`

Repository QR reference:

`../hitokoto-poster-v3/assets/qr.png`

Fixed destination:

`https://hitokoto-kaeshi-preview.web.app/poster`

4組の例、CTA文言、reassurance / caution、`広報部会（仮）` は変更していません。

## Correction-5 implementation

### Title hierarchy

- title size: `38px → 42px`
- title markerを少し太く・強く調整
- side note `正解は、ありません。` は少し小さくして従属関係を明確化

### Exchange-card rhythm

- 4組の意味上の優先順位は変更しない
- pair幅 / 左位置を少しずつ変え、均一感を弱める
- paper tone / shadow / rotation / reply offsetを小さく変化させる
- text size / 4組の内容は変更しない

### Relational warmth / people

- 人物線画は2箇所のまま
- 右上人物を `18mm → 22mm` に拡大し、存在感を少し上げる
- 左下人物は補助的なまま
- mascot / kawaii / chibi / stereotype は使用しない

### CTA emphasis

- strong boxed card UIには戻さない
- pale mint系の薄い帯を追加
- `QRからどうぞ` を少し強くする
- QR display size: `28mm → 30mm`
- white quiet zoneを維持

### Accent contrast

- yellow / mint / pale blue / coralを少しだけ強める
- decorative categoriesは追加しない
- full cork / wooden frameは使用しない

## Static verification

- required authoritative strings: **PASS**
- four `.pair` groups: **PASS / 4**
- repository QR reference unchanged: **PASS**
- long URL absent from poster surface: **PASS**
- remote font dependency: **none**
- title / CTA / caution strings: **PASS**

## A4 fixed-layout verification

Renderer: `WeasyPrint + rendered PNG inspection`

Local renderer uses a same-destination / same-layout-size QR image only for render pixels. Repository QR reference and QR blob are separately verified unchanged.

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

No fresh Chromium PASS is claimed for Correction-5. Browser evidence remains supplementary under Issue #31 when the execution environment blocks it.

## Physical Validation

Still separate and not consumed:

- real A4 physical readability
- real-device QR scan
- destination readback

## Exact implementation scope

Correction-5 changes are limited to:

- `references/in-progress/hitokoto-poster-card-wall-v1/poster.html`
- `references/in-progress/hitokoto-poster-card-wall-v1/visual-review.md`

The following remain unchanged / out of scope:

- `content.md`
- `hitokoto-poster-v3/assets/qr.png`
- Accepted / Pattern / Prompt / Foundation content
- Print / Post / Deploy / Real Trial

## Gate state

- Correction-5 Definition / Scope: **GO / CONSUMED / LOCKED**
- Independent Definition / Scope Review: **PASS**
- Human Implementation Start: **GO / CONSUMED**
- Correction-5 implementation: **APPLIED**
- Static scope/content verification: **PASS**
- A4 fixed-layout verification: **PASS**
- Browser verification: **SUPPLEMENTARY / NO FRESH PASS CLAIMED**
- Fresh Implementation / Scope Review: **PASS at exact HEAD `0f1908575faba477cb285185fcc328c6c0596911`**
- Correction-5 Human Ready: **REQUIRED / NEXT HUMAN GATE**
- Human Visual Acceptance: **NOT DONE**
- Physical A4 / real-device QR: **NOT DONE**
- Merge / Print / Post / Deploy / Promotion: **HOLD**
