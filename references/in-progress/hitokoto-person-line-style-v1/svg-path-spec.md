# SVG Path Specification V1

## 目的

この仕様は、HITOKOTO PERSON LINE STYLE V1の人物線画をSVGとして再現するための実装基準です。

この値は案件固有Pilotの値であり、共通Foundationへ自動昇格しません。

## 1. Canvas

基準viewBoxは次です。

```text
0 0 512 512
```

人物本体は、おおむね次の範囲に収めます。

```text
x = 72–440
y = 56–456
```

外周には十分な余白を残します。

人物を画面端まで広げません。

## 2. Stroke

SVG内部では色を固定しません。

```svg
<g
  fill="none"
  stroke="currentColor"
  stroke-width="8"
  stroke-linecap="round"
  stroke-linejoin="round"
>
```

標準線幅は `8` です。

許容範囲は `7–9` です。

同一人物の中では原則として同じ線幅を使います。

筆圧表現のために線幅をランダム化しません。

利用面の標準色はcurrent Foundation Primaryに従います。

Pilot開始時点のPrimaryは `#234E3F` です。

## 3. Fill

基本は `fill="none"` です。

髪、服、顔、小物を面で塗りません。

目も可能な限り短いstrokeで表現します。

## 4. Path density

人物1体あたりのpath数は次を目安にします。

```text
recommended = 18–36
maximum     = 45
```

45を超える場合は描き込み過多を疑います。

1本の長い輪郭に過剰なアンカーポイントを置きません。

短い線は2–4点程度を目安にします。

長い顔輪郭や髪輪郭でも6–12点程度を目安にします。

自動トレースで発生した細かな点は整理します。

## 5. Curves

曲線はCubic Bézierを基本にします。

完全な円や完全な左右対称形を多用しません。

自然な範囲で左右差を残します。

左右差の目安は次です。

```text
position difference = 3–12px
curve difference    = 2–8px
angle difference    = 2–6deg
```

歪みを目立たせること自体を目的にしません。

## 6. Face contour

顔輪郭は1–2本の大きなopen pathを基本にします。

完全な閉じた楕円にはしません。

耳、髪、首との境界で自然に線を切ります。

## 7. Eyes

目は次のいずれかに限定します。

```text
short vertical line
short diagonal line
small curved line
```

大きさは512px viewBoxに対して概ね `8–14px` にします。

白目と黒目を描き分けません。

大きなアニメ調の目にしません。

## 8. Nose

鼻は1本の短い線を基本にします。

長さは概ね `10–22px` にします。

鼻孔や立体的な鼻梁は描きません。

## 9. Mouth

口は1本の短い曲線を基本にします。

長さは概ね `22–44px` にします。

歯、舌、唇の輪郭は描きません。

話す動作以外では大きく開いた口を使いません。

## 10. Brows

眉は必須ではありません。

使う場合は1–2本の短線にします。

感情を強く説明する記号として使いません。

## 11. Hair

髪は次の2層で表現します。

```text
outer contour
+
2–6 internal strokes
```

毛束を一本ずつ描きません。

ベタ塗りしません。

人物差は髪の外形を中心に作ります。

## 12. Ears

耳は必要な側だけ描いて構いません。

1–2本の曲線で表現します。

耳内部の細かな構造は描きません。

## 13. Neck and shoulders

首は原則2本の線です。

肩は左右それぞれ1本程度を基本にします。

肩線をviewBoxの端まで伸ばしません。

胸上で自然に切ります。

## 14. Hands

手は写実化しません。

指は動作判別に必要な本数だけ示します。

5本すべてを描く必要はありません。

メモを取る動作なら、ペン、親指側の輪郭、2–3本の指線で成立させます。

thinkingでは、手が顎または頬に触れていることと、前腕まで見える大きなジェスチャーを優先します。

lookingでは、髪型差より頭部方向と視線方向で意味を作ります。

## 15. Props

小物は動作を伝えるためにだけ使います。

小物1個あたりのpath数は8–15程度を上限目安にします。

メモ帳なら、外枠、綴じ、数本の紙面線で十分です。

note-takingでは、紙またはメモ帳は大きく単純な形に保ち、斜めのペン先が紙へ向かう関係を明確にします。

小物内部に文字を入れません。

## 16. Open / closed paths

次は原則open pathです。

```text
hair
face
neck
shoulders
mouth
nose
brows
clothes
```

小物の外形など、認識に必要な場合だけclosed pathを使います。

## 17. Layer order

描画順は次を基本にします。

```text
1. back hair
2. neck / shoulders
3. face contour
4. front hair
5. eyes / nose / mouth
6. hands
7. props
8. foreground detail
```

重なりを自然に見せるために必要な場合だけ順序を調整します。

## 18. Semantic neutrality

再利用SVGには、利用文脈を固定する `role`、`aria-label`、`aria-hidden` を埋め込みません。

装飾か意味付きかは利用面で判断します。

必要な意味をSVGだけに依存させません。

## 19. File naming

人物属性ではなく動作を中心に命名します。

```text
person-note-taking.svg
person-thinking.svg
person-looking.svg
person-listening.svg
person-nodding.svg
person-reading.svg
person-speaking.svg
person-watching.svg
person-noticing.svg
person-waiting.svg
```

## 20. Cleanup

最終保存前に次を除去します。

```text
editor metadata
unused groups
unused defs
unnecessary clipPath
unnecessary nested transforms
excessive decimal precision
```

座標精度は原則整数または小数点1桁までで十分です。

## 21. Minimal source form

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <g
    fill="none"
    stroke="currentColor"
    stroke-width="8"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <!-- original paths -->
  </g>
</svg>
```

## 22. Acceptance

```text
[ ] viewBox = 0 0 512 512
[ ] stroke = currentColor
[ ] stroke-width = 7–9
[ ] round cap / join
[ ] fillなしを基本とする
[ ] 45 path以下
[ ] 顔情報量が少ない
[ ] 髪が細密ではない
[ ] 小物が人物より強くない
[ ] 64px程度でも動作が判別できる
[ ] 通常サイズでラベルなしでも「メモ / 考える / 眺める」を区別できる
[ ] 64px相当でも各人物の主要ジェスチャーが最低1つ読める
[ ] 髪型・服装ではなくポーズ、手、小物、頭部方向、視線方向で意味が成立している
[ ] 既存のLine Style Foundationを崩していない
[ ] 必要な意味をイラスト単独に依存していない
```
