# HITOKOTO PERSON LINE STYLE V1

## 目的

このStyle Guideは、「ひとこと返し」で使う人物線画を同じ視覚言語で再現するための案件固有ルールです。

Web、カード、チラシ、ポスター、説明資料で使う補助イラストを対象にします。

人物線画は文章、投稿内容、QR、行動導線より強く見せません。

## Authority

このディレクトリは `references/in-progress/` 配下のPilotです。

現時点では `foundations/*`、`patterns/*`、`prompts/*` を置き換えません。

上位の共通ルールは `foundations/illustration.md`、`foundations/colors.md`、`foundations/accessibility.md`、`prompts/illustration.md` です。

Production SVGの線色は固定色にせず `currentColor` を使います。

利用面の既定色は、その時点のFoundation Primaryに従います。

Pilot開始時点のFoundation Primaryは `#234E3F` です。

参考画像から観察した明るい緑 `#14AE67` は、画風分析の履歴値でありProduction Authorityではありません。

## 見た目

目標は、緑のサインペンで短時間に描いたような、静かで親しみのある人物線画です。

線はほぼ一定幅にします。

線には少しだけ手描きの揺れを残します。

顔は点または短線の目、短い鼻線、小さな口で構成します。

髪は外形と少数の内部線で表現します。

人物差は髪型、眼鏡、帽子、襟、小物、顔の向きで作ります。

塗り、影、グラデーションは使いません。

幼いキャラクター、マスコット、福祉を象徴する記号的人物には寄せません。

## SVG基準

```text
viewBox          = 0 0 512 512
stroke           = currentColor
stroke-width     = 8
allowed width    = 7–9
stroke-linecap   = round
stroke-linejoin  = round
fill             = none
recommended path = 18–36
max path         = 45
```

詳細は `svg-path-spec.md` を参照します。

## Behavior Set V1

```text
01 note-taking  / メモを取る
02 thinking     / 考える
03 looking      / 眺める
04 listening    / 聞く
05 nodding      / うなずく
06 reading      / 読む
07 speaking     / 話す
08 watching     / 見守る
09 noticing     / 気づく
10 waiting      / 待つ
```

動作は説明記号ではなく、視線、姿勢、手、小物の最小構成で示します。

10動作の生成指示は `behavior-prompts.md` にまとめます。

## Pilot SVG

初回は次の3点だけを実装します。

```text
examples/person-note-taking.svg
examples/person-thinking.svg
examples/person-looking.svg
```

この3点で線幅、顔情報量、手、小物、視線、縮小時の判別性を確認します。

残り7点はHuman Visual Review後の別判断です。

## アクセシビリティ

SVG資産自体には、利用文脈に依存する固定のアクセシビリティ意味を埋め込みません。

装飾として使うか、意味のある画像として使うかは利用面で決めます。

意味のある画像として使う場合は、利用面で適切なアクセシブルネームまたは周辺テキストを用意します。

必要な情報を人物線画だけに閉じ込めません。

## 運用

生成AIの出力は、そのまま仕様適合とは扱いません。

SVG化後に `review-checklist.md` で確認します。

迷った場合は情報を足すより減らします。

かわいさより静けさを優先します。

説明記号より人物の姿勢を優先します。

## Gate

```text
Definition / Scope             = LOCKED
Human Implementation Start     = GO / CONSUMED
Pilot implementation           = IN PROGRESS
Human Ready                    = HOLD
Human Visual Acceptance        = HOLD
Remaining 7 SVGs               = HOLD
Notion canonicalization        = HOLD
Merge / Promotion              = HOLD
```
