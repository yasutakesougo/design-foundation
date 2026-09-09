# ひとこと返し A4ポスター — CANVA-OUTPUT-PILOT-V1

- Date: 2026-09-08
- Medium: A4 poster / Canva
- Source: PR #15 `CANVA-OUTPUT-PILOT-V1` / Issue #21 `HITOKOTO-POSTER-ACCEPTED-REFERENCE-V1`
- Human Visual Acceptance: PASS

## 採用した理由

- A4実寸で成立した。
- 実機QRで読み取り成立した。
- 実際の掲示で投稿が成立した。
- 紙での視覚的違和感がなかった。

## 実試行 evidence

- Period: 1 week
- Placement: 事務所壁
- 投稿成立: あり
- 紙での違和感: なし
- 迷い・質問: あり
- 内容: 「自分が関係あるのか？」

## 再利用できる判断

- Canva-first を Visual Production Surface として使う。
- GitHub = Content Authority / guardrails、Primary Visual Reference = 視覚参考、Canva = production surface、Human = final judgement と役割を分離する。
- 1つのQRを1つの連続した行動導線として見せる。
- `title → concrete examples → QR → action → safety` の情報構造を有力な構成候補として再利用する。
- AI生成物を最終デザイン正本として固定しない。
- Human Visual Review / Acceptance の後に、A4実寸、実機QR、実掲示、Real Trialまで確認する。

## 条件付きで引き継ぐ学び

- 次回は「自分も対象なのか」が一瞬で分かる参加対象・関係性の手掛かりを、Content Authority / CTA周辺の設計で明確にする。

## 再利用しない案件固有要素

- 現行全文言。
- 現行人物イラストそのもの。
- exact palette / exact geometry / exact decoration。
- 未確定の匿名性、閲覧範囲、保存期間などの運用約束。

## Promotion boundary

このAccepted Referenceは、今後の判断材料として再利用するための記録である。

一度のAccepted表現を、Pattern / Prompt / Foundationへ自動昇格させない。

`patterns/*`、`foundations/*`、`prompts/*`、`review/*` の変更はこの記録のScopeに含めない。
