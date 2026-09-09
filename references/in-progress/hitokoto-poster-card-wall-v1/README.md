# ひとこと掲示 Card Wall V1

- Medium: A4縦 掲示
- Status: Final visual direction selected / deterministic reproduction refinement in progress
- Issue: #23 `HITOKOTO-POSTER-CARD-WALL-V1` / #39 Correction-8 / #41 Content Microcopy Gate / #45 Correction-9a
- PR: #24
- Date: 2026-09-09
- Human Visual Acceptance: HOLD
- Physical A4 / real-device QR: HOLD
- Print / Post: HOLD
- Deploy / Real Trial: HOLD

このフォルダは、「日常を、言葉に。」を核とした職員向けの参加型ミニ実験ポスターを扱います。

目的は、気づきの大切さを啓発することではありません。

日常の中で少し気になったことを、完成した意見にする前に、30秒程度でひとこと置いてみられる入口をつくることを目的とします。

既存 `hitokoto-poster-v3` は変更しません。

## Authority split

- GitHub = 本文 / QR / Scope / 証跡 / Human Gate の正本
- `DESIGN.md` = 現在のHuman-selected visual directionを再現するためのvisual design authority
- `production-microcopy.md` = active production copy subset authority
- Canva / deterministic SVG / PNG / PDF = 見た目を実装・確認する制作面
- HTML `poster.html` = Correction-7までの構造参考。最終印刷制作面ではない

`DESIGN.md` は本文、補助コピー、QR、Human Gateを上書きしません。

## Current visual direction

採用方向は次です。

- 「啓発物」ではなく「小さな参加募集」
- 生成りの紙面 + 深緑 + 淡い緑 + 黄色
- 手描き感のあるタイトル + 黄色brush
- 3つの異なる紙メモで「このくらいのひとことでよい」を見せる
- 紙、テープ、クリップ、影にごく小さい素材差を持たせる
- 完全な機械整列を避け、固定的なcontrolled imperfectionを使う
- 人物はadult editorial flat illustrationとし、説明の主役にはしない
- 上部人物とCTA人物の肌色、線、簡略化レベルを同一シリーズとして統一する
- CTAを行動の主役とし、QRコードは明確な入口として扱う
- 補助マイクロコピーと装飾は主役にしない

詳細:

- `DESIGN.md`
- `correction-8-approved-visual-direction.md`
- `correction-8-canva-production-spec.md`
- `correction-8-canva-checklist.md`

## Information hierarchy

```text
日常を、言葉に。
↓
気になったことを、ひとことだけ。
↓
ひとこと → ひとこと返し × 3
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

画像生成物のQRは参照用であり、本番に流用しません。

## Files

- `DESIGN.md`: 現在のvisual design authority。Concept / Typography / Color / Paper / Object / Character / Accessibilityを定義
- `content.md`: broader source copy authority
- `production-microcopy.md`: active production subset authority
- `poster.html`: Correction-7構造参考
- `visual-review.md`: Human Visual Review / Gate状態
- `correction-8-approved-visual-direction.md`: 選定ビジュアル方向の履歴
- `correction-8-canva-production-spec.md`: Canva完成版実装仕様書
- `correction-8-canva-checklist.md`: 実装担当向け1ページ版チェックリスト

## HOLD

この候補を `accepted/`、`patterns/`、`prompts/`、`foundations/` へ昇格しません。

Human Visual Acceptanceと後続Gateを通るまで、本印刷・正式掲示には使いません。
