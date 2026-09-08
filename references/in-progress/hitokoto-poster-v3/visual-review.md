# Visual Review（ドラフト）

判定: PASS WITH CORRECTION（V3.5 Human Visual Acceptance前）

Foundationへの昇格: HOLD。案件ドラフトと方向性だけ残し、共通基盤へは昇格しない。

## Accessibility Baseline

- 本文は13px前後を下回らない。注意書きも12px。
- 主色 `#234E3F` と生成り背景のコントラストは見出し用途として確認済み。
- QRは中央の独立した白いフィールドに置き、クワイエットゾーンを維持する。
- 必要情報は画像内文字だけに閉じ込めていない。

## V3.5 Visual Correction-2

Baseline: `main@f87212b7b42553270b80ca767d16d35642effd96`

Human Definition / Scope Lock: GO
Human Implementation Start: GO
Human Visual Acceptance for this candidate: **NOT DONE**

### Direction synthesis

V3の内容・意味を維持し、後続比較案で良かった整理感だけを取り入れる。

- `日常を、言葉に。` を第一視線にする。
- `気になったことを、ひとことだけ。` と3つの観察例を維持する。
- `周りの人にも知ってほしいこと` や活動紹介・改善提案募集には戻さない。
- QRは中央の独立した白い余白に置き、強い外枠や貼り付け感を避ける。
- 人物は下部右側の補助要素へ下げ、タイトルとQRより弱くする。
- 人物から名札・ストラップ等の職種記号を外し、静かに考えながら小さく書き留める観察者にする。
- `広報部会（仮）の小さな試行` の下に強い黒線は置かない。

### Scope

変更対象は次の3ファイルだけ。

- `poster.html`
- `assets/scene.jpg`
- `visual-review.md`

`content.md`、`assets/qr.png`、Directions、Accepted、Patterns、Prompts、Foundations は変更しない。

### A4 one-page verification

- print engine: WeasyPrint
- print-to-PDF: **1 page**
- PDF page size: **595.276 × 841.89 pt (A4)**
- clipping / fragmentation: rendered PNG readbackで確認されず
- 本文 `13.5px`、例 `12.5px`、注意書き `12px` を維持
- QR本体 `58mm × 58mm` を維持
- QR fieldは `62mm × 62mm` の白背景で、余計な太枠なし

### Visual hierarchy readback

1. 第一視線: `日常を、言葉に。`
2. 第二視線: `気になったことを、ひとことだけ。` → 説明 → 3例
3. 中央行動: `QRからどうぞ` → QR → `ひとことを書く → ひとこと返しを見る`
4. 下部: 安心文 → 最低限の注意 → 小さい観察者イラスト

### Observer readback

- 名札なし
- ストラップなし
- 明確な制服・専門職記号なし
- 小さなメモと考える姿勢
- CTAを指差す／案内するポーズなし
- 人物は下部右側の補助要素で、QRより小さい

### Non-change evidence

- `content.md` baseline blob SHA: `e3796e9956adbdcee155130878cae3aac69baa0d`（変更対象外）
- `assets/qr.png` baseline blob SHA: `a68d1f558c96c4eecb6a7e81cb1e74c5c8cf0a52`（変更対象外）
- QR fixed destination: `https://hitokoto-kaeshi-preview.web.app/poster`
- `周りの人にも知ってほしいこと` / `こんな活動をしている` / `こんな工夫をしている` は掲示本文へ採用しない。

## Remaining gates

- Fresh Implementation / Scope Review: REQUIRED
- Human Ready GO: NOT DONE
- New Human Visual Acceptance: NOT DONE
- Physical A4 / real-device QR validation: NOT DONE
- Print / Post: HOLD
- Deploy / Real Trial Start: HOLD
- Poster Pattern / Prompt / Foundation Promotion: HOLD

V3.5の技術検証PASSだけでは、Human Visual Acceptance、本印刷、正式掲示、Deploy、Real Trial Start、Pattern昇格を許可しない。
