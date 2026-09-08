# Card Wall V1｜Human Visual Review

## Review target

Direction C｜リアル・雑さ重視。

大学生協の「ひとことカード」のように、掲示された複数の紙を眺める感覚を参照します。

評価する中心は、**「ひとこと → ひとこと返し」の関係が一目で伝わるか**です。

## First-glance check

- [ ] 最初に `日常を、言葉に。` が見える
- [ ] 次に複数のカードへ視線が移る
- [ ] 左の `ひとこと` と右の `ひとこと返し` がセットだと分かる
- [ ] 矢印が説明記号ではなく自然な往復として見える
- [ ] QRがカード群の次の行動として見える

## Tone check

- [ ] 実際に掲示されているような生活感がある
- [ ] きれいに整いすぎていない
- [ ] 雑然としすぎて読みにくくなっていない
- [ ] 楽しそうだが、幼い寄せ書きには見えない
- [ ] 福祉の啓発ポスターや広報ネタ募集には見えない
- [ ] 人物・キャラクターが主役になっていない

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

- [ ] A4縦で1ページに収まる
- [ ] カード本文が実寸A4で読める
- [ ] 注意書きを縮小しすぎていない
- [ ] QR周囲に十分な余白がある
- [ ] 実機QR確認はまだ実施しない

## Scope check

- [ ] 変更は新規4ファイルだけ
- [ ] `hitokoto-poster-v3/*` は未変更
- [ ] `accepted/*` は未変更
- [ ] `patterns/*` は未変更
- [ ] `prompts/*` は未変更
- [ ] `foundations/*` は未変更

## Current gate

- Human Direction Selection: C / CONFIRMED
- Implementation: STARTED
- Human Ready: HOLD
- Human Visual Acceptance: NOT DONE
- Physical A4 / real-device QR: NOT DONE
- Print / Post: HOLD
- Deploy / Real Trial: HOLD
- Pattern / Prompt / Foundation promotion: HOLD
