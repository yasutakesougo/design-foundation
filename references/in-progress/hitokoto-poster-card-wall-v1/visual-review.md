# Card Wall V1｜Human Visual Review

## Current review target

`CARD-WALL-V1 Correction-7 — Scene Illustration / Typography / Rhythm Density Refinement` の Human Visual Review 対象です。

Baseline exact HEAD:

`1caf22d5ea74b70ffc4f12e619d43b637d4bc03e`

Human feedback translated into this correction:

- 人物が未完成なピクトグラムのように見える
- 画面がまださっぱりしすぎる
- フォントの大きさと間の取り方にもう一段リズムが必要

Correction-7 は、**場面イラスト・文字サイズ階層・余白リズム**だけを調整します。

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

## Correction-7 implementation

### Scene illustration refinement

Correction-6 の抽象的な線画人物を、意味が読める3場面へ置き換えました。

1. 上部左: メモを手にした大人
2. 右中段: 掲示カードへ身体を寄せて読む大人
3. CTA左: 2人が1枚のメモを一緒に見る場面

各場面は、視線・手・持ち物・姿勢を読み取れるようにし、髪・服・紙に淡い面色を加えています。

- adult / workplace tone
- no real-person likeness
- no disability stereotype
- no mascot / chibi treatment
- illustration remains subordinate to title / exchanges / CTA

### Decorative density cleanup

- Correction-6 の複数ドット群・放射アクセント・単独植物を削減
- 装飾の埋め草を減らし、3つの意味のある場面を視覚アンカーに変更
- 補助アクセントは小さなdot clusterと2本の曲線アクセントのみ

### Typography hierarchy

- title: `46px → 50px`（約8.7%増）
- lead: `17px → 17.6px`
- card body: `13.4px → 14.25px`（約6.3%増）
- card label: `9.6px → 10.2px`
- CTA title: `22.5px → 23px`
- caution / footer size: **縮小なし / 9.9px維持**
- remote web font: **none**

### Spacing rhythm

Correction-6 の均一な縦間隔を、次の3段階へ整理しました。

1. hero → exchanges: 広めの間を確保 (`margin-bottom: 5mm`)
2. exchange field: 4組を `gap: 2mm` のcompact rhythmへ
3. exchanges → CTA: `5.5mm` の明確なsection break

4組は一つのまとまりとして見えつつ、CTAとは明確に分かれる構成です。

### CTA composition

- CTAの強さはCorrection-6を維持
- 左に2人の場面イラストを組み込み、`書く → 見る` の人の気配を補助
- CTA本文とQRの可読性は維持
- QR display size: `31mm` 維持
- quiet zone維持

## Static verification

- required authoritative strings: **PASS**
- four `.pair` groups: **PASS / 4**
- repository QR reference unchanged: **PASS**
- long URL absent from poster surface: **PASS**
- new speech-bubble copy: **none**
- remote font import: **none**
- title / CTA / caution strings: **PASS**
- illustration scenes: **3**

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
- larger card text readability: **PASS**
- scene illustrations avoid primary reading path: **PASS**
- CTA discovery / hierarchy: **PASS**
- caution/footer readability: **PASS**
- QR quiet zone in layout: **PASS**
- awkward Japanese line break: **none observed**

No fresh Chromium PASS is claimed for Correction-7. Browser evidence remains supplementary under Issue #31 when the execution environment blocks it.

## Human visual questions

1. 人物が未完成ピクトではなく、意味のある小場面に見えるか。
2. 視線・手・持ち物の関係がA4サイズでも読めるか。
3. 人の気配が増えた一方、幼くなっていないか。
4. `日常を、言葉に。` が第一焦点として十分強いか。
5. 4組の文字が以前より読みやすく、主役として見えるか。
6. 4組の段間がつながりを生み、詰まりすぎていないか。
7. title / exchange field / CTA の間に明確なリズムがあるか。
8. さっぱりしすぎる印象が改善したか。
9. CTAが引き続き見つけやすいか。
10. 装飾過多 / 子ども向け / AIポスターっぽい方向へ振れていないか。

## Physical Validation

Still separate and not consumed:

- real A4 physical readability
- real-device QR scan
- destination readback

## Exact implementation scope

Correction-7 changes are limited to:

- `references/in-progress/hitokoto-poster-card-wall-v1/poster.html`
- `references/in-progress/hitokoto-poster-card-wall-v1/visual-review.md`

The following remain unchanged / out of scope:

- `content.md`
- `hitokoto-poster-v3/assets/qr.png`
- Accepted / Pattern / Prompt / Foundation content
- Print / Post / Deploy / Real Trial

## Gate state

- Correction-6: **SUPERSEDED CANDIDATE / historical evidence only**
- Correction-7 Definition / Scope: **GO / CONSUMED / LOCKED**
- Independent Definition / Scope Review: **PASS**
- Human Implementation Start: **GO / CONSUMED**
- Correction-7 implementation: **APPLIED**
- Static scope/content verification: **PASS**
- A4 fixed-layout verification: **PASS**
- Browser verification: **SUPPLEMENTARY / NO FRESH PASS CLAIMED**
- Correction-7 Human Ready: **REQUIRED / NOT YET CONSUMED**
- Human Visual Acceptance: **NOT DONE**
- Physical A4 / real-device QR: **NOT DONE**
- Merge / Print / Post / Deploy / Promotion: **HOLD**
