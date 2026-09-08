# Visual Review（ドラフト）

判定: PASS WITH CORRECTION（Human Visual Acceptance前）

PR #7 Human Ready: GO。チラシの Human Visual Acceptance とは別ゲート。Scope Review PASS 後に GO する。

Foundationへの昇格: HOLD。案件ドラフトと方向性だけ残し、共通基盤へは昇格しない。

## Accessibility Baseline

- 本文は13px前後を下回らない。注意書きも12px。
- 主色 `#234E3F` と生成り背景のコントラストは見出し用途として確認済み。
- QRは中央に分離し、クワイエットゾーンあり。
- 必要情報は画像内文字だけに閉じ込めていない。

## 5項目

1. 最初に見る場所は「日常を、言葉に。」。QRは中央の行動入口。
2. V3本文は短い。運用説明・手順図・詳細安全説明は載せていない。
3. イラストは1場面。観察者として右上に添え、QRより強くしない。
4. 色はFoundationの深い緑と生成り。手書き感は紙と水彩で出している。
5. CuteGuideCharacter と OperationalPromiseOnPrint は避ける。未確定の匿名・保存日数は書いていない。

## V3 POST-MERGE-CORRECTION-1 技術検証

Baseline: `main@6790d260d71d897efa3f6a25e5019ba388159151`

Correction scopeは `poster.html` とこの `visual-review.md` の2ファイルだけ。本文、QR asset / destination、scene asset、Direction / Pattern / Foundation は変更しない。

### A4 one-page

- Headless Chromium: `Chromium 144.0.7559.96`
- print-to-PDF: **1 page**
- PDF page size: **594.96 × 841.92 pt (A4)**
- 印刷時 `.sheet`: `297mm`
- 印刷時 `.inner`: `271mm`
- DOM fit check: `.inner scrollHeight <= clientHeight` / `.sheet scrollHeight <= clientHeight`
- clipping / fragmentation: ローカルHeadless検証では確認されず
- 本文フォントサイズ、注意書きサイズ、QR `58mm × 58mm` は縮小していない

### HOLD banner contrast

- emphasis color: `#A35F32`
- background: `#FFFFFF`
- contrast ratio: **約 4.95:1**
- `foundations/accessibility.md` の通常デジタル文字目標 `4.5:1` 以上を満たす
- banner wordingは変更していない

### Non-change evidence

- `content.md` blob SHA: `e3796e9956adbdcee155130878cae3aac69baa0d`（baselineと同一）
- `assets/qr.png` blob SHA: `a68d1f558c96c4eecb6a7e81cb1e74c5c8cf0a52`（baselineと同一）
- `assets/scene.jpg` blob SHA: `a28efee74983c05ff496e29c0eec87e6ac5280c8`（baselineと同一）

## 残っているHuman / Physical確認

- 人物イラストの採用可否。方向性案であり、名称決定ではない。
- **Human Visual Acceptance: NOT DONE**
- **実寸印刷での本文サイズ確認: NOT DONE**
- **物理A4印刷からの実機QR読取: NOT DONE**
- Deploy / Real Trial Start: HOLD
- Print / Post: HOLD
- Poster Pattern / Prompt / Foundation Promotion: HOLD

Correction-1の技術検証PASSだけでは、Human Visual Acceptance、本印刷、正式掲示、Deploy、Real Trial Start、Pattern昇格を許可しない。
