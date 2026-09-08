# External Reference: write-in-pencil

## 参照情報

- Repository: `momotarabitch2/write-in-pencil`
- Reviewed commit: `3f0e4e62e0dcc86308567dad2dd8e07ae002b651`
- License: MIT
- Reviewed date: `2026-09-08`

## 採用する考え方

構想を整理するAIと、視覚化する画像生成工程を分ける考え方を採用します。

主題、構成、情報の流れだけでなく、設計意図、代替案、未解決事項をラフへ残す考え方を採用します。

完成物を直接作る前に、必要な場合だけ比較可能な探索物を作る考え方を採用します。

## 採用しないもの

外部Skill固有の青・オレンジ配色をDesign Foundationのブランド規則へしません。

木目机、筆記具、紙の写真表現を必須にしません。

外部Skillの文面をそのまま内部Skillの正本にはしません。

## 依存関係

submodule、package、runtime dependencyとして組み込みません。

外部更新へ自動追従しません。

別commitの変更を取り込む場合は、採用判断に影響する差分を再レビューします。
