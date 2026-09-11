# ひとこと掲示 V3（検討用ドラフト）

- Medium: A4縦 掲示
- Status: Content Lock + Draft
- Date: 2026-09-08

## Current state

- PR / Merge state: PR #7 = MERGED。merge commit `6790d260d71d897efa3f6a25e5019ba388159151`
- Human Merge: GO / CONSUMED / COMPLETE。PR #7 comment `#issuecomment-5580716097`
- Human Ready: UNKNOWN / HOLD。独立した明示Human Ready evidenceは確認できず、PR本文・agent-authored review text・Human Merge GOから遡って推定しない
- Human Visual Acceptance: NOT CONSUMED / HOLD
- Human Output GO: UNKNOWN / HOLD
- Print / Post: HOLD。2026年12月の第2回までは正式導入しない
- Current evidence: PR #7 merged-main readback comment `#issuecomment-5580716097`、`visual-review.md`、`independent-review.md`
- Supersedes: NONE。このCurrent stateは既存evidenceを集約するが、元reviewをSUPERSEDED扱いしない

このフォルダは完成物の正本ではありません。掲示候補の本文固定と、印刷前の見た目確認用ドラフトです。

PR #7のMerge完了は、Human Visual Acceptance、Human Output GO、Print / Postを意味しません。
証拠が不足するHuman Gateは推定せず、UNKNOWN / HOLDを維持します。

掲示の構成ルールは `references/directions/poster-pattern.md` に候補として残します。`patterns/` へは、Human Visual Acceptance → 実寸印刷確認 → 実試行で少なくとも一度成立するまで昇格しません。

## 印刷QR

固定入口: `https://hitokoto-kaeshi-preview.web.app/poster`

期限付きPreview Channel URLは職員確認専用とし、印刷QRには使いません。

コード上の固定入口は別リポジトリでMerge済みでも、stable HostingへのDeploy・実URL確認・Real Trial StartまではQR本採用をHOLDします。

## ファイル

- `content.md`: 掲示面に載せる本文（運用メモは載せない）
- `poster.html`: A4ドラフト
- `assets/qr.png`: 固定入口のQR
- `assets/scene.jpg`: 補助イラスト1点（観察者。公式キャラクター採用ではない）

画面上部のHOLD表示は確認用です。本掲示面の一部ではありません。
