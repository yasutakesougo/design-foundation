# ひとこと掲示 Card Wall V1

- Medium: A4縦 掲示
- Active direction: **V3 入口特化ポスター**
- Definition: Issue #59
- Fresh Review: Issue #60 / Correction-1後 PASS
- PR: #24
- Date: 2026-09-09
- Human Definition / Scope Lock: GO / CONSUMED / LOCKED
- Human Implementation Start: GO / CONSUMED
- Human Visual Acceptance: HOLD
- V3 Physical A4 / fresh real-device QR: REQUIRED / HOLD
- Print / Post: HOLD
- Deploy / LIVE WRITE / Real Trial: separate gates / HOLD

このフォルダは、「日常を、言葉に。」を核とした職員向けの参加入口ポスターを扱います。

V3の目的は、A「ひとこと循環」の仕組みを詳しく説明することではありません。

**何を書けばよいかがわかり、QRを読めること**を優先します。

## V3 information hierarchy

```text
日常を、言葉に。
↓
具体例3件
↓
大きなQR
↓
ひとことを書く → ひとこと返しを見る
↓
最低限の安心・注意
```

V3掲示面では、3件の返し例を並べません。

返しそのものはQR先の体験として残します。

## Authority split

- GitHub = 本文 / QR / Scope / 証跡 / Human Gate の正本
- `content.md` = V3 broader content / operational boundary authority
- `production-microcopy.md` = V3 active production surface copy authority
- `DESIGN.md` = V3 visual design authority
- `poster.html` = V3 deterministic A4 implementation candidate
- Canva / SVG / PNG / PDF = 後続の見た目確認・制作面。別Gate

Correction-8 / Correction-9aの文書は履歴証拠として保持します。

V3はそれらを削除せず、V3 production surfaceについて新しいauthorityを定義します。

## Current visual direction

- 「説明」ではなく「参加入口」
- 白〜生成り + 深緑 + 黄〜オレンジ少量
- titleは第一焦点
- example notes exactly 3
- reply examples 0
- QRは紙面中央付近の主要行動対象
- illustration exactly 1 scene
- adult editorial flat illustration
- controlled imperfection
- Web UI / SaaS card gridにしない
- 広報ネタ募集 / 改善提案BOXに見せない
- AI / system / A→B→C→Dを前面に出さない
- safetyは読めるが紙面を支配しない

## QR

Repository asset:

`../hitokoto-poster-v3/assets/qr.png`

Fixed destination:

`https://hitokoto-kaeshi-preview.web.app/poster`

期限付きFirebase Preview Channel URLは印刷QRへ使いません。

## Physical QR boundary

過去Canva candidateのPhysical QR Validation PASSは履歴証拠のみです。

V3 final production candidateにはfreshなPhysical QR Validationが必要です。

```text
actual intended final paper size / print settings
→ physical device scan
→ canonical /poster PASS
→ Preview Channel redirect 0
```

## Timing boundary

明示的なHuman superseding decisionがない限り、**2026年12月の第2回広報部会までは正式導入しません。**

準備・実装・レビュー・別GateのCloud readiness作業は可能です。

ただし少なくとも次は第2回前に自動承認しません。

- Human Print / Post GO
- Human Real Trial Start GO
- Actual Staff Pilot Start

## Current files

- `content.md`: V3 content / operational boundary authority
- `production-microcopy.md`: V3 exact production copy authority
- `DESIGN.md`: V3 visual authority
- `poster.html`: V3 deterministic implementation candidate
- `visual-review.md`: historical visual review record; V3 HVAはまだ未実施
- `correction-8-approved-visual-direction.md`: historical evidence
- `correction-8-canva-production-spec.md`: historical implementation spec
- `correction-8-canva-checklist.md`: historical checklist

## HOLD

V3 implementation candidateができても、次は自動承認しません。

- Canva final save
- Human Visual Acceptance
- Physical A4 / fresh QR validation
- CLOUD-TRIAL activation
- LIVE WRITE
- Merge
- Print / Post
- Real Trial Start
- Actual Staff Pilot
- `accepted/` / `patterns/` / `prompts/` / `foundations/` promotion
