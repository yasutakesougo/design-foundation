# ひとこと掲示 Card Wall V1（Correction-8 / Canva production）

- Medium: A4縦 掲示
- Status: Correction-8 Canva production / scene composition refinement
- Issue: #23 `HITOKOTO-POSTER-CARD-WALL-V1` / #39 Correction-8 / #41 Content Microcopy Gate
- PR: #24
- Canva Design ID: `DAHUqyhsx2s`
- Date: 2026-09-09
- Human Ready: HOLD
- Human Visual Acceptance: NOT DONE
- Print / Post: HOLD
- Deploy / Real Trial: HOLD

このフォルダは、大学生協の「ひとことカード」のような掲示感をDesign DNAとして参照した独立候補です。

実物の固有フォーマット、ロゴ、カード様式は複製しません。

この候補では、カードの数そのものより、**「ひとこと → ひとこと返し」**の往復が一目で分かることを優先します。

既存 `hitokoto-poster-v3` は変更しません。

## Authority split

- GitHub = 本文 / QR / Scope / 証跡 / Human Gate の正本
- Canva = 見た目を仕上げる制作面（Design `DAHUqyhsx2s`）
- HTML `poster.html` = Correction-7までの構造参考。Correction-8の最終印刷制作面ではない

## Current visual direction

採用方向は次です。

- 手描き感のあるタイトル + 黄色マーカー
- 少し不揃いな掲示カード / マスキングテープ / 手描き緑矢印
- 場面が読めるシンプルな大人の人物
- 温かいCTA / 淡い緑のフッター
- 補助マイクロコピーは主役にしない

詳細:

- `correction-8-approved-visual-direction.md`
- `correction-8-canva-production-spec.md`
- `correction-8-canva-checklist.md`

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
（補助マイクロコピーは常に最後）
```

## QR

既存V3の固定入口assetを参照します。

`../hitokoto-poster-v3/assets/qr.png`

固定入口は `https://hitokoto-kaeshi-preview.web.app/poster` です。

画像生成物のQRは参照用であり、本番に流用しません。

## Files

- `content.md`: 固定本文（変更禁止）
- `production-microcopy.md`: Human-locked 補助マイクロコピー5件
- `poster.html`: Correction-7構造参考（HTML再設計はしない）
- `visual-review.md`: Human Visual Review / Gate状態
- `correction-8-approved-visual-direction.md`: 選定ビジュアル方向
- `correction-8-canva-production-spec.md`: Canva完成版実装仕様書
- `correction-8-canva-checklist.md`: 実装担当向け1ページ版チェックリスト

## HOLD

この候補を `accepted/`、`patterns/`、`prompts/`、`foundations/` へ昇格しません。

Human Visual Acceptanceと後続Gateを通るまで、本印刷・正式掲示には使いません。
