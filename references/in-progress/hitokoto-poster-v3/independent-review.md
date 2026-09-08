# Fresh Independent Implementation / Scope Review

- PR: #7
- HEAD: `adc7dce055c1841c914195e390da351a60e56635`
- Date: 2026-09-08
- 判定: PASS

V3チラシの Human Visual Acceptance と、このPRの Human Ready は別ゲートとする。

## このPRの範囲

完成チラシの正本化ではない。次を履歴として残す。

- in-progressドラフトの保存
- Direction候補の保存
- Rejected / Anti-patternの保存
- 昇格条件の明示

## 確認したこと

- changed paths は11。`foundations/`、`patterns/`、`prompts/` に差分はない。
- `poster-pattern.md` / `poster-prompt.md` は `references/directions/` の候補。`patterns/` / `prompts/` へは、Human Visual Acceptance → 実寸印刷確認 → 実試行で少なくとも一度成立するまで昇格しない。
- Observer は方向性案。Foundation / illustration prompt へは昇格しない。
- 掲示面は「タイトル → 具体例3件 → QR → 行動 → 注意」。未確定の匿名・閲覧範囲・保存日数は約束していない。
- QR画像は `https://hitokoto-kaeshi-preview.web.app/poster` を指す。Deploy / Real Trial Start 前は Print/Post HOLD。

## このPRではまだ見ないこと

- Human Visual Acceptance
- 実寸QR読取
- Poster Pattern Promotion

## 次

Human Ready GO → Merge。V3は `references/in-progress` のまま。Pattern昇格は別PRで検討する。
