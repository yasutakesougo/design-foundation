# ひとこと掲示 Card Wall V1（Direction C）

- Medium: A4縦 掲示
- Status: Human Direction C selected / implementation draft
- Issue: #23 `HITOKOTO-POSTER-CARD-WALL-V1`
- Date: 2026-09-08
- Human Ready: HOLD
- Human Visual Acceptance: NOT DONE
- Print / Post: HOLD
- Deploy / Real Trial: HOLD

このフォルダは、大学生協の「ひとことカード」のような掲示感をDesign DNAとして参照した独立候補です。

実物の固有フォーマット、ロゴ、カード様式は複製しません。

この候補では、カードの数そのものより、**「ひとこと → ひとこと返し」**の往復が一目で分かることを優先します。

既存 `hitokoto-poster-v3` は変更しません。

## Visual direction

- 実際の掲示板に紙が貼られているようなコルクボード感
- 左を「ひとこと」、右を「ひとこと返し」として4組配置
- 各組を緑の矢印で結ぶ
- 少しだけ傾き、紙色、テープ、ピンを変える
- にぎやかさは残すが、幼い寄せ書きにはしない
- 深い緑 + 生成りを中心にする
- 黄は見出し下線などの小さなアクセントだけにする
- 人物イラストは使わない

## Information hierarchy

```text
日常を、言葉に。
↓
気になったことを、ひとことだけ。
↓
ひとこと → ひとこと返し × 4
↓
QRからどうぞ
↓
ひとことを書く → ひとこと返しを見る
↓
最低限の安心・注意
```

## QR

既存V3の固定入口assetを参照します。

`../hitokoto-poster-v3/assets/qr.png`

固定入口は `https://hitokoto-kaeshi-preview.web.app/poster` です。

stable Hostingの状態、実機QR、Print / Post、Real Trialは別Gateです。

## Files

- `content.md`: この候補で使用する掲示面コピー
- `poster.html`: A4縦のVisual Draft
- `visual-review.md`: Human Visual Review用の確認観点

## HOLD

この候補を `accepted/`、`patterns/`、`prompts/`、`foundations/` へ昇格しません。

Human Visual Acceptanceと後続Gateを通るまで、本印刷・正式掲示には使いません。
