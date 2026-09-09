# Review Checklist V1

## 目的

このチェックリストは、HITOKOTO PERSON LINE STYLE V1のSVGがシリーズとして成立しているか確認するために使います。

自動チェックだけでHuman Visual Reviewを代替しません。

## 1. Scope

```text
[ ] 変更はlocked scope内だけか
[ ] foundations/* を変更していないか
[ ] patterns/* を変更していないか
[ ] prompts/illustration.md を変更していないか
[ ] current CARD-WALL productionを変更していないか
[ ] -hitokoto-kaeshi-front runtime/UIを変更していないか
[ ] 残り7 SVGを無断で追加していないか
```

## 2. SVG structure

```text
[ ] viewBox="0 0 512 512"
[ ] stroke="currentColor"
[ ] stroke-widthが7–9
[ ] stroke-linecap="round"
[ ] stroke-linejoin="round"
[ ] fill="none" を基本にしている
[ ] path数が45以下
[ ] editor metadataがない
[ ] 不要なdefs / clipPath / nested transformがない
[ ] 過剰な小数点精度がない
```

## 3. Composition

```text
[ ] 人物本体が概ねx=72–440に収まる
[ ] 人物本体が概ねy=56–456に収まる
[ ] 外周に十分な余白がある
[ ] 肩や小物がviewBox端へ接触していない
[ ] 胸上の構図として読める
```

## 4. Face

```text
[ ] 目は点または短線レベルか
[ ] 鼻は短い1本線レベルか
[ ] 口は小さな曲線か
[ ] 白目 / 黒目 / 唇 / 歯などを描き込んでいないか
[ ] 表情が強すぎないか
[ ] 左右完全対称になっていないか
```

## 5. Hair / clothing

```text
[ ] 髪は外形 + 2–6本程度の内部線か
[ ] 毛束を細かく描き込んでいないか
[ ] 髪をベタ塗りしていないか
[ ] 服の柄や襟が人物より目立っていないか
[ ] 幼児向けキャラクターの記号へ寄っていないか
```

## 6. Hands / props

```text
[ ] 指を必要以上に描き込んでいないか
[ ] 手が写実的すぎないか
[ ] 小物は動作判別に必要なものだけか
[ ] 小物内に文字がないか
[ ] 小物が人物より目立っていないか
```

## 7. Behavior readability

```text
[ ] 64px程度でも動作差が読めるか
[ ] 通常サイズでラベルなしでも「メモ / 考える / 眺める」を区別できるか
[ ] 64px相当でも各人物の主要ジェスチャーが最低1つ識別できるか
[ ] note-takingはメモ動作が読めるか
[ ] note-takingは紙、斜めペン、書く手の少なくとも1つが明確に読めるか
[ ] thinkingは手・視線で考える状態が読めるか
[ ] thinkingは顎または頬に触れる手と前腕が読めるか
[ ] lookingは横向きの視線で眺める状態が読めるか
[ ] lookingは横向き頭部と横視線が読めるか
[ ] 髪型・服装ではなく、ポーズ、手、小物、頭部方向、視線方向で意味が成立しているか
[ ] 電球 / 疑問符 / 感嘆符 / 時計などの説明記号に頼っていないか
```

64px判定はシリーズ品質の確認です。

必要な意味をイラストだけに依存させる許可ではありません。

## 8. Series consistency

3点を横並びで確認します。

```text
[ ] 線幅が揃って見えるか
[ ] 顔の情報量が揃っているか
[ ] 髪の密度が揃っているか
[ ] 肩・服の簡略化レベルが揃っているか
[ ] 表情の温度が揃っているか
[ ] 余白量が極端に違わないか
[ ] 線色、線幅、丸い線端、余白量、顔の簡潔さを大きく変えずにLine Style Foundationを維持しているか
[ ] 3点とも同じ制作者のシリーズに見えるか
```

## 9. Tone

```text
[ ] 幼く見えないか
[ ] かわいさが主役になっていないか
[ ] マスコット化していないか
[ ] 福祉・医療・介護を記号化していないか
[ ] 教材イラストのように説明過多ではないか
[ ] 企業素材のように整いすぎていないか
[ ] ラフすぎて未完成ピクトに見えないか
```

## 10. Color authority

```text
[ ] SVGに#14AE67をProduction色として固定していないか
[ ] SVGはcurrentColorを使っているか
[ ] 利用面の色はcurrent Foundation authorityに従えるか
```

## 11. Accessibility boundary

```text
[ ] reusable SVGに固定aria-labelを埋めていないか
[ ] reusable SVGにrole="img" + aria-hidden="true"の矛盾した固定指定がないか
[ ] decorative / meaningfulの判断を利用面へ残しているか
[ ] 必要な意味をイラスト単独へ閉じ込めていないか
```

## 12. Human Visual Review questions

1. 3点は同じシリーズに見えるか。
2. 参考画像の軽さは残りつつ、コピーではなく独自の線画になっているか。
3. かわいすぎず、大人向けの補助イラストとして使えるか。
4. 小さく置いても、メモ・考える・眺めるの違いがわかるか。
5. 人物が文章やQRより強くなりそうな要素はないか。
6. 次の7動作を同じ規則で増やせそうか。

## 13. Gate result

Human Visual Review前は次を維持します。

```text
Human Ready               = HOLD until fresh implementation review
Human Visual Acceptance   = HOLD
Remaining 7 SVGs          = HOLD
Notion concise mirror     = HOLD
Merge / Promotion         = HOLD
```
