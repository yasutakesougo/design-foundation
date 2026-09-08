# Card Wall V1｜Human Visual Review

## Review target

Direction C｜リアル・雑さ重視。

大学生協の「ひとことカード」のように、掲示された複数の紙を眺める感覚を参照します。

評価する中心は、**「ひとこと → ひとこと返し」の関係が一目で伝わるか**です。

## Correction-1

初回プレビューでは、関係性は明確でしたが、4組が均等な2列グリッドに見え、実際の掲示板としては少し整いすぎていました。

Correction-1では次を調整しました。

- 各Pairの横位置と幅を少しずつ変え、完全な整列を崩す
- カードごとの傾きを少し強める
- `ひとこと → ひとこと返し` の左右関係と矢印は維持する
- CTAの説明量を減らし、左に行動文、右にQRを置く
- 安心・注意はCTA本体から分離した細い紙片にまとめる
- 人物や追加イラストは入れない

Correction-1は、**雑さを足しても往復の読みやすさを失わない**ことを狙った調整です。

## Correction-2

Correction-1へのフィードバックを受け、生活感と文字組をさらに調整しました。

- `ひとこと返し` 側をPairごとに約1.2〜2.3mm下げ、あとから返しが貼られたような時間差を出す
- Pairごとの横位置・幅・カード角度のばらつきは維持する
- CTAは文節の途中で割れないよう、1行固定と明示改行を組み合わせる
- `正解は、ありません。` は1行で見せる
- CTAの文字サイズ・字間をわずかに抑え、カード群より主張しすぎないようにする
- QR枠は弱い破線へ変更し、行動導線としては維持しつつカード群との競合を減らす

### 記名表現について

実在の氏名に見える署名を混ぜる案は採用していません。

掲示面では `氏名など個人がわかる情報は書かないでください` と案内しているため、例示カードへ記名を入れると入力ルールと矛盾するためです。

生活感は、署名ではなく位置・角度・紙色・返信側の段差で表現します。

## Correction-3

Correction-3では、情報構造とコピーを固定したまま、「デザインされたカードUI」より「実際のコルクボードに少しずつ紙が貼られた状態」へ一段寄せました。

### Texture treatment

実装は **CSS-only** です。

candidate-local assetは追加していません。

コルク面は、暖かい茶系を基調に複数の `radial-gradient`、弱い `repeating-linear-gradient`、内側の陰影を重ねています。

粒状感と濃淡は文字やカードより前に出ない強さへ抑えています。

紙は生成りを中心に、薄いグリーン、黄み、低コントラストの方眼を混在させています。

紙ごとに回転、影、紙色、留め方を少し変えています。

外部texture URL、第三者写真、大学生協の実物カード画像、ロゴ、固有装飾は使用していません。

### Pin / tape treatment

留め方はPairごとに変えています。

- Pair 1: note = push pin / reply = short masking tape
- Pair 2: note = masking tape / reply = push pin
- Pair 3: note = push pin + slightly lifted shadow / reply = masking tape
- Pair 4: note = one-sided tape / reply = small push pin

push pinとtapeはCSSの疑似要素だけで描画しています。

### Reply Y offsets

`ひとこと返し` 側だけを次の量だけ下げています。

- Pair 1: `5px`
- Pair 2: `10px`
- Pair 3: `7px`
- Pair 4: `12px`

左右の対応関係と中央の矢印は維持しています。

### CTA

CTAは一枚の紙として維持し、カード群より強くならないようにしています。

`QRからどうぞ`、`ひとことを書く → ひとこと返しを見る`、補足文の優先順位は変更していません。

QR周囲は白地と独立余白を維持しています。

注意文は縮小せず、line-heightと上下余白をわずかに増やしています。

`広報部会（仮）` は下端との距離を確保し、注意文との圧迫感を減らしています。

### Font fallback

remote fontは使用していません。

日本語本文は既存の安全なfallback chainを維持しています。

```text
"Hiragino Kaku Gothic ProN", "Yu Gothic", "Noto Sans JP", Meiryo, sans-serif
```

矢印だけにローカルのhandwritten系fallbackを使い、本文レイアウトはその有無に依存しません。

readabilityをhandwriting characterより優先しています。

### Browser / print renderer

Browser renderingを最終Human Visual Review用surfaceとします。

BrowserとChromium print-to-PDFの両方で、カード配置、reply段差、紙色、tape/pin、主要なshadowとtextureは維持されました。

print rendererでは細かなshadowと粒状感がbrowser screenshotより少し均されて見えますが、情報階層やpair mappingへ影響する差は確認していません。

ローカル検証環境ではrepositoryのbinary QR assetを直接mountできないため、browser screenshot / print-to-PDFのレイアウト確認時だけ、同じdestinationから生成した同寸法のローカルQRをdata URIとして差し込みました。

repository側のQR asset参照とblobは変更しておらず、実機QR確認は後続Physical Validationのままです。

## First-glance check

- [x] 最初に `日常を、言葉に。` が見える
- [x] 次に複数のカードへ視線が移る
- [x] 左の `ひとこと` と右の `ひとこと返し` がセットだと分かる
- [x] 矢印が各Pairの関係を補助している
- [x] QRがカード群の次の行動として見える

## Tone check

- [x] コルク面が単色・平坦に見えない
- [x] 紙色・影・留め方に小さな差があり、同一UI部品の反復に見えにくい
- [x] 返し側の段差があり、あとから応答が添えられた関係を示している
- [x] texture / pin / tapeが本文より前へ出ていない
- [x] 雑貨屋・文化祭・かわいい寄せ書き方向へ寄せていない
- [x] 人物・キャラクター・追加装飾を主役にしていない
- [ ] Human Visual Acceptanceは未実施

## Reply check

見るポイントは、返しが説明、評価、正解、本人の意味の確定に見えないことです。

少し続きを考えたくなる余白が残っているかを確認します。

違和感があれば、どのPairのどの言葉が気になるかをそのまま記録します。

### Pair 1

`今日は、いつもの声かけに少し間があった。`

→ `その「間」、ちょっと気になりますね。`

### Pair 2

`言葉はなかったけど、何度もこちらを見ていた。`

→ `見ていた先に、何かあったのかもしれません。`

### Pair 3

`声をかける順番を変えたら、少し表情が違った。`

→ `順番にも、何かありそうですね。`

### Pair 4

`自販機の前で、しばらく立ち止まっていた。`

→ `何を見ていたんでしょうね。`

## Correction-3 verification evidence

### Scope / content integrity

- Starting HEAD: `f645902386b48add3cb4e636af452732147cc21b`
- `content.md` before blob: `6e9e6fa168976ed0f28882b783ae986d826ba1e5`
- `content.md` after blob: `6e9e6fa168976ed0f28882b783ae986d826ba1e5`
- `content.md`: **byte-for-byte unchanged**
- Added candidate-local assets: none

### QR integrity

- QR reference remains `../hitokoto-poster-v3/assets/qr.png`
- QR asset blob remains `a68d1f558c96c4eecb6a7e81cb1e74c5c8cf0a52`
- QR destination remains `https://hitokoto-kaeshi-preview.web.app/poster`
- Real-device QR validation: NOT DONE

### Browser visual verification

- Cork is not visually flat: PASS
- Paper has physical variation: PASS
- Four exchanges remain traceable: PASS
- Reply time offsets remain readable: PASS
- Texture remains subordinate: PASS
- Adult / calm tone maintained: PASS
- CTA remains secondary to card exchange: PASS
- Unnatural Japanese mid-word wrapping observed: none

Browser Visual Review: **PASS**

### A4 print-to-PDF

- Renderer: Chromium / Skia PDF
- Page count: **1**
- Page size: A4, approximately `595 × 842 pt`
- clipping: **none observed**
- fragmentation: **none observed**
- overflow: **none observed**
- missing text: **none observed**
- QR quiet-zone layout: maintained

A4 print-to-PDF: **PASS**

## Accessibility / print checks before Ready

- [x] A4縦 `210mm × 297mm` のprint CSSを維持している
- [x] Correction-3のprint-to-PDFは1ページ
- [x] Correction-3のPDF page sizeはA4 `595 × 842 pt` 相当
- [x] Correction-3のレンダーでクリッピングは見られない
- [x] CTAの `QRからどうぞ` と行動文に不自然な途中改行は見られない
- [x] QR周囲に独立した余白がある
- [ ] カード本文の実寸A4可読性はPhysical Validationで確認する
- [ ] 実機QR確認は未実施

## Scope check

- [x] Correction-3の変更対象は `poster.html` と `visual-review.md` のみ
- [x] `content.md` は未変更
- [x] `hitokoto-poster-v3/*` は未変更
- [x] `accepted/*` は未変更
- [x] `patterns/*` は未変更
- [x] `prompts/*` は未変更
- [x] `foundations/*` は未変更
- [x] `review/*` は未変更

## Current gate

- Human Direction Selection: C / CONFIRMED
- Correction-3 Human Definition / Scope Lock: SATISFIED
- Correction-3 Human Implementation Start: CONSUMED / APPLIED
- Implementation: Correction-3 APPLIED + browser / local A4 render verified
- Human Ready: NOT CONSUMED / HOLD
- Human Visual Acceptance: NOT DONE
- Physical A4 / real-device QR: NOT DONE
- Merge: HOLD
- Print / Post: HOLD
- Deploy / Real Trial: HOLD
- Accepted Reference / Pattern / Prompt / Foundation promotion: HOLD
