# Card Wall V1｜Human Visual Review

## Current review target

`CARD-WALL-V1 Correction-4` の Human Visual Review 対象です。

Human-selected direction は **Direction B / light handmade + realistic paper texture** です。

Correction-3 の Human Visual Acceptance は Exact HEAD `9a32701e06b2468f6dcd9484ca53f5b707b6a122` に対する historical evidence のみであり、Correction-4 には継承しません。

評価の中心は、次の順序が崩れていないことです。

1. `日常を、言葉に。`
2. 4組の `ひとこと → ひとこと返し`
3. CTA + real QR
4. reassurance / caution
5. supporting illustration / decoration

## Content authority

`content.md` は Correction-4 でも正本です。

Correction-4 実装では `content.md` を変更しません。

掲示面の必要文言は HTML text として維持します。

生成ビジュアルに含まれていた追加の吹き出し文、説明文、AI生成QR・文字は production copy として採用しません。

QR asset / destination も変更しません。

固定 destination:

`https://hitokoto-kaeshi-preview.web.app/poster`

Repository QR reference:

`../hitokoto-poster-v3/assets/qr.png`

## Correction-1〜3 の位置づけ

Correction-1〜2 は、カードの整列を崩しながら左右の往復を維持する方向を確認した履歴です。

Correction-3 は、コルク、木枠、紙、留め方を強く物理表現へ寄せた候補でした。

Correction-3 は browser / print-to-PDF 上では成立していましたが、Physical Validation review 中に Human が visual result を却下しました。

そのため Correction-4 は、往復構造と内容 authority を残しつつ、全面コルク・木枠・重い茶色・過剰な material simulation を廃止します。

## Correction-4 implementation

### Page / background

- A4 portrait `210mm × 297mm` を維持
- bright warm off-white / pale neutral base
- full cork background を削除
- wooden frame を削除
- large dark field を使用しない
- pale mint / pale blue / pale coral の低優先度 background accents のみ使用

### Primary palette

- deep green を title / labels / arrows / CTA emphasis の主色に使用
- cards は off-white / very pale green / very pale blue
- yellow は title / CTA の marker treatment に限定
- orange / coral は背景の低優先度 accent に限定

### Title

- `日常を、言葉に。` を first-glance focal point として維持
- title 周囲の余白を拡大
- `正解は、ありません。` は独立した小さな paper note として維持
- side note は title より強くしない

### Four exchanges

4組はすべて explicit left-to-right pair のままです。

`ひとこと → ひとこと返し`

- pair mapping を変更しない
- reply 側だけを少し下げ、あとから返しが加わった時間差を残す
- rotation / offset は小さくする
- paper texture は軽くする
- shadow は Correction-3 より弱くする
- cards は高コントラストを維持する

### Tape / pins

留め具は全カードへ付けません。

Correction-4 では main card field 全体で4箇所だけです。

- Pair 1 note: short tape
- Pair 2 reply: small pin
- Pair 3 note: short tape
- Pair 4 reply: small pin

装飾が文字と競合する場合は、装飾を先に削除します。

### Person illustrations

人物線画は2箇所です。

- page edge に限定
- central reading path の外側
- deep-green line art
- adult / workplace tone
- 観察する、メモを見る、やりとりする程度の場面
- disability / welfare stereotype を使わない
- mascot / kawaii / chibi treatment を使わない
- real-person likeness を使わない

人物線画は `poster.html` 内の original inline SVG です。

外部 proprietary illustration は使用していません。

人物線画を除いても情報構造は成立します。

### CTA / QR

CTA は strong card / boxed UI にしません。

- thin divider + whitespace で本文から分離
- action text は左
- real repository QR は右
- CTA は title + exchanges より subordinate
- long URL は掲示面に載せない
- QR 周囲は白地の quiet zone を確保
- QR quiet zone 内へ decoration を入れない
- `QRからどうぞ` は1行固定

### Footer / caution

Correction-3 より caution readability を優先します。

- caution を薄い細帯へ圧縮しない
- authoritative caution text を維持
- line-height を確保
- fit 問題を文字縮小で解決しない
- `広報部会（仮）` を明確に読める状態で残す

## Verification evidence

### Scope / content integrity

Correction-3 Exact HEAD `9a32701e06b2468f6dcd9484ca53f5b707b6a122` から Correction-4 実装で変更した repository paths は次の2件だけです。

- `references/in-progress/hitokoto-poster-card-wall-v1/poster.html`
- `references/in-progress/hitokoto-poster-card-wall-v1/visual-review.md`

`content.md` blob remains:

`6e9e6fa168976ed0f28882b783ae986d826ba1e5`

QR asset blob remains:

`a68d1f558c96c4eecb6a7e81cb1e74c5c8cf0a52`

Static HTML inspection:

- required authoritative poster strings: PASS
- four `.pair` groups: PASS / 4
- person illustration placements: PASS / 2
- repository QR reference unchanged: PASS
- long URL absent from poster surface: PASS
- full cork token absent: PASS
- wooden frame token absent: PASS
- remote font import absent: PASS

### A4 fixed-layout render

Local A4 verification renderer: WeasyPrint + rendered PNG inspection.

Same-size local placeholder was used only for the QR image pixels because repository binary download is not available in the local renderer sandbox. The HTML QR reference and repository QR blob were separately verified unchanged.

Result:

- page count: **1**
- page size: **A4 / 595.276 × 841.89 pt**
- clipping observed: **none**
- fragmentation observed: **none**
- visible overflow observed: **none**
- title first-glance visibility: **PASS**
- four pair mappings: **PASS**
- CTA hierarchy: **PASS**
- `QRからどうぞ` line stability after refinement: **PASS**
- caution/footer visible and uncompressed: **PASS**
- figures remain outside main reading path: **PASS**

### Chromium browser renderer

A browser verification attempt was made with the available local Chromium binary.

The Chromium process does not complete even for a minimal local HTML file in this execution environment and repeatedly stalls on the environment runtime/DBus layer.

Therefore:

- browser visual verification for Correction-4: **BLOCKED BY EXECUTION ENVIRONMENT**
- this is not recorded as a design PASS or FAIL
- A4 fixed-layout evidence above remains valid but does not silently substitute for the locked browser verification requirement

## Accessibility / print conditions

- [x] A4 portrait 1 page in fixed-layout renderer
- [x] clipping none observed
- [x] fragmentation none observed
- [x] overflow none observed
- [x] title immediately visible
- [x] all 4 pair mappings unambiguous
- [x] card text visible/readable in A4 render
- [x] CTA readable but secondary
- [x] caution visible and not compressed in A4 render
- [x] QR quiet zone preserved in layout
- [x] no awkward Japanese line break observed in A4 render
- [x] no remote font dependency
- [ ] Chromium/browser verification — BLOCKED BY EXECUTION ENVIRONMENT

Physical Validation では別途、実寸A4可読性と real-device QR read を確認します。

## Exact implementation scope

Correction-4 で変更可能なのは次だけです。

- `references/in-progress/hitokoto-poster-card-wall-v1/poster.html`
- `references/in-progress/hitokoto-poster-card-wall-v1/visual-review.md`
- optional candidate-local `assets/*` only if required

今回、candidate-local asset は追加していません。

次は変更しません。

- `content.md`
- `hitokoto-poster-v3/*`
- `accepted/*`
- `patterns/*`
- `prompts/*`
- `foundations/*`
- `review/*`
- shared asset library / reusable style layer

## Gate state

- Correction-4 Human Direction Selection: **B / CONFIRMED**
- Direction B refined visual: **ACCEPTED AS DIRECTION ONLY**
- Fresh Independent Definition / Scope Review: **PASS**
- Human Definition / Scope Lock: **GO / CONSUMED / LOCKED**
- Human Implementation Start: **GO / CONSUMED**
- Correction-4 implementation: **APPLIED**
- A4 fixed-layout verification: **PASS**
- Chromium/browser verification: **BLOCKED BY EXECUTION ENVIRONMENT**
- Human Ready: **HOLD — browser evidence not complete**
- Human Visual Acceptance: **NOT DONE**
- Physical A4 / real-device QR: **NOT DONE**
- Merge: **HOLD**
- Print / Post: **HOLD**
- Deploy / Real Trial: **HOLD**
- Accepted / Pattern / Prompt / Foundation promotion: **HOLD**

Implementation Start は Merge / Print / Post / Deploy / Real Trial / Promotion を許可しません。
