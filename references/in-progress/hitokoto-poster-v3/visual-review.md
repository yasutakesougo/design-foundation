# Visual Review（V3.5候補）

判定: PASS WITH CORRECTION（新しいHuman Visual Acceptance前）

V3 VISUAL-CORRECTION-2: Implementation中。旧Issue #10のHuman Visual Acceptanceは `main@f87212b7b42553270b80ca767d16d35642effd96` に対する履歴であり、このV3.5候補には継承しない。

Foundationへの昇格: HOLD。案件ドラフトとDirectionの範囲に留め、Pattern / Prompt / Foundationへは昇格しない。

## Correction-2の狙い

3枚目の「日常の小さな気づきを拾う」内容を正本として維持し、比較案で得られた整理感だけを取り入れる。

- `日常を、言葉に。` を最初に見る場所にする。
- `気になったことを、ひとことだけ。` と3つの観察例を維持する。
- QRを中央の独立した行動入口にする。
- 「周りの人にも知ってほしいこと」「こんな活動をしている」「こんな工夫をしている」へは戻さない。
- 人物は説明・案内・返答をする人ではなく、静かな観察者として弱く添える。

## Accessibility Baseline

- 本文は13px前後、注意書きは12pxを維持する。
- 主色 `#234E3F` と生成り背景を継続する。
- QRは `58mm × 58mm` を維持し、白い独立フィールドでクワイエットゾーンを確保する。
- 必要情報は画像内文字だけに閉じ込めない。
- 印刷用のために本文・注意書きを縮小していない。

## V3 VISUAL-CORRECTION-2 実装確認

Baseline: `main@f87212b7b42553270b80ca767d16d35642effd96`

変更対象は次の3ファイルだけ。

- `poster.html`
- `assets/scene.jpg`
- `visual-review.md`

### 1. 上部

- `広報部会（仮）の小さな試行` の下に強い黒線を置かない。
- タイトルを中央に独立させ、最初の視線を `日常を、言葉に。` に固定する。
- 装飾を増やさず、余白で階層を作る。

### 2. 観察例

- Content Lockの3例をそのまま維持する。
- 3例を一つの静かなパネルにまとめ、読み順を整理する。
- PR・活動紹介・改善提案募集に見えるコピーへ差し替えない。

### 3. QR

- `QRからどうぞ` → QR → `ひとことを書く → ひとこと返しを見る` の順に整理する。
- QR周辺に強い外枠を置かない。
- 白い独立フィールドに置き、貼り付けたような見え方を避ける。
- `assets/qr.png` と固定destinationは変更しない。

### 4. Observer figure

- 名札・ストラップなし。
- 専門職制服・案内ポーズなし。
- 小さなメモとペン程度に留める。
- 正面から誘導せず、少し考えながら書き留める姿勢。
- タイトルとQRより明確に小さく・弱く扱う。

## Local print evidence

- renderer: **WeasyPrint 68.0**
- print-to-PDF: **1 page**
- page size: **595.276 × 841.89 pt (A4)**
- raster readback: **1 page / clipping・fragmentationは目視で確認されず**
- QR: 中央の独立フィールド、`58mm × 58mm` を維持
- 本文 / 注意書き: 縮小なし
- Chromium CLIはこの実行環境でDBus関連待ちにより終了せず、今回の技術証拠には採用していない。実寸印刷と実機QR読取は後続Human/Physical Gateで確認する。

## Non-change evidence

Correction-2はbase treeから3パスだけを置き換える。

- `content.md` baseline blob SHA: `e3796e9956adbdcee155130878cae3aac69baa0d` — unchanged
- `assets/qr.png` baseline blob SHA: `a68d1f558c96c4eecb6a7e81cb1e74c5c8cf0a52` — unchanged
- QR fixed destination: `https://hitokoto-kaeshi-preview.web.app/poster` — unchanged
- `references/directions/*` — unchanged
- `patterns/*` / `prompts/*` / `foundations/*` — unchanged

## Gate State

- Human Definition / Scope Lock: GO / CONSUMED
- Human Implementation Start: GO / CONSUMED
- Implementation: candidate prepared
- Fresh Implementation / Scope Review: REQUIRED
- Human Ready: NOT DONE
- Human Visual Acceptance for V3.5: NOT DONE
- Physical A4 / real-device QR validation: NOT DONE
- Print / Post: HOLD
- Deploy / Real Trial Start: HOLD
- Poster Pattern / Prompt / Foundation Promotion: HOLD

技術確認PASSだけでは、Human Ready、Human Visual Acceptance、本印刷、正式掲示、Deploy、Real Trial Start、Pattern昇格を許可しない。
