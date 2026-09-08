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

## First-glance check

- [x] 最初に `日常を、言葉に。` が見える
- [x] 次に複数のカードへ視線が移る
- [x] 左の `ひとこと` と右の `ひとこと返し` がセットだと分かる
- [x] 矢印が各Pairの関係を補助している
- [x] QRがカード群の次の行動として見える

## Tone check

- [x] カードの位置・幅・角度が完全なグリッドではない
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
- Implementation: Correction-1 APPLIED
- Human Ready: HOLD
- Human Visual Acceptance: NOT DONE
- Physical A4 / real-device QR: NOT DONE
- Print / Post: HOLD
- Deploy / Real Trial: HOLD
- Pattern / Prompt / Foundation promotion: HOLD
