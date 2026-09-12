# FRESH-REVIEW-AUTOMATION-V1

このディレクトリは、Fresh Review の実装候補を保持します。

accepted authority ではありません。

実装の正本は Issue #251、Clarification-1、Correction-1 です。

この slice は、GitHub の bounded read-only GET から review packet を作り、外部から明示された reviewer command を一度だけ起動し、出力を検証し、lossless relay envelope と read-only reconciliation result を生成します。

GitHub write、repository write by coordinator、auto-resume、Ready、Merge、Deploy、Promotion、provider SDK、credential 管理は実装しません。

## 実装パス

- `tools/fresh_review_automation_v1/__init__.py`
- `tools/fresh_review_automation_v1/cli.py`
- `tools/fresh_review_automation_v1/schemas/review-packet.schema.json`
- `tools/fresh_review_automation_v1/schemas/reviewer-output.schema.json`
- `tools/fresh_review_automation_v1/schemas/relay-envelope.schema.json`
- `tools/fresh_review_automation_v1/tests/test_cli.py`

契約詳細は `automation-contract.md` を参照してください。
