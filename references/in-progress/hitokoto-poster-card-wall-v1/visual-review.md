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
- `word-break: keep-all` と文節単位の `inline-block` をCTAへ入れ、不自然な途中改行を減らす
- `正解は、ありません。` は1行で見せる
- CTAの文字サイズ・字間をわずかに抑え、カード群より主張しすぎないようにする
- QR枠は弱い破線へ変更し、行動導線としては維持しつつカード群との競合を減らす

### 記名表現について

実在の氏名に見える署名を混ぜる案は採用していません。

掲示面では `氏名など個人がわかる情報は書かないでください` と案内しているため、例示カードへ記名を入れると入力ルールと矛盾するためです。

生活感は、署名ではなく位置・角度・紙色・返信側の段差で表現します。

## First-glance check

- [x] 最初に `日常を、言葉に。` が見える
- [x] 次に複数のカードへ視線が移る
- [x] 左の `ひとこと` と右の `ひとこと返し` がセットだと分かる
- [x] 矢印が各Pairの関係を補助している
- [x] QRがカード群の次の行動として見える

## Tone check

- [x] カードの位置・幅・角度が完全なグリッドではない
- [x] 返し側に小さな段差があり、同時配置ではなく応答として見える
- [x] 雑然としすぎず、4組の対応関係は追える
- [x] 人物・キャラクターが主役になっていない
- [ ] 実際の掲示として十分な「生活感」があるかはHuman Visual Reviewで確認する
- [ ] 楽しそうだが、幼い寄せ書きに見えないかはHuman Visual Reviewで確認する
- [ ] 福祉の啓発ポスターや広報ネタ募集に見えないかはHuman Visual Reviewで確認する

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

## Accessibility / print checks before Ready

- [x] A4縦 `210mm × 297mm` のprint CSSを維持している
- [x] Correction-1のローカルprint-to-PDFは1ページ
- [x] Correction-1のレンダーでクリッピングは見られない
- [x] QR周囲に独立した余白がある
- [ ] Correction-2のprint-to-PDF / clipping再確認
- [ ] カード本文の実寸A4可読性は未確認
- [ ] 実機QR確認は未実施

## Scope check

- [x] 変更対象は独立候補フォルダ内だけ
- [x] `hitokoto-poster-v3/*` は未変更
- [x] `accepted/*` は未変更
- [x] `patterns/*` は未変更
- [x] `prompts/*` は未変更
- [x] `foundations/*` は未変更

## Current gate

- Human Direction Selection: C / CONFIRMED
- Implementation: Correction-2 APPLIED
- Human Ready: HOLD
- Human Visual Acceptance: NOT DONE
- Physical A4 / real-device QR: NOT DONE
- Print / Post: HOLD
- Deploy / Real Trial: HOLD
- Pattern / Prompt / Foundation promotion: HOLD
