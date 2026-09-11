# Blind Pilot Protocol

IR-L2候補を、答えをReviewerへ見せずに評価するためのProtocolです。

## Case A — known-clean control

```text
Purpose = false-positive control
Input = known acceptable historical change
Expected = unsupported P0/P1を生成しない
```

Case Aは、Reviewerが不要なblocking findingを作らないことを確認します。

## Case B — seeded or known finding control

```text
Purpose = must-detect control
Input = known defectを含むhistorical artifactまたはsynthetic fixture
Expected = predefined Must-Detect findingを発見する
```

Case Bは、Reviewerが定義済みのblocking findingをEvidence付きで検出できることを確認します。

## Blindness requirement

Reviewerには次を見せません。

```text
Expected Findings
Must-Detect oracle
evaluator scoring key
expected Human verdict
```

これらはPilot終了までReviewer-accessible repository、Issue、prompt、tool surfaceへ置きません。

Evaluator-side evidenceとして保持し、Pilot終了後に結果と比較します。

## Input binding

各Caseのreview packetはcontent-addressedまたは同等のartifact identityへ結び付けます。

Reviewer Input Manifestには、対象artifact、Definition、Locked Scope、Acceptance Criteria、Allowed / Excluded / Ambientを記録します。

Reviewerへ渡した入力を後から推測で補完しません。

## Read-only boundary

Pilotはread-onlyです。

```text
Reviewer mutation authority = NONE
Repository mutation = PROHIBITED
Human Gate inference / consumption = PROHIBITED
```

## Separate evaluation

Case AとCase Bは別々に評価します。

一方のPASSだけでPilot全体をPASSにしません。

最低限、次を確認します。

```text
Case A:
- unsupported P0/P1なし
- evidence-bound findings
- contamination eligibility satisfied

Case B:
- predefined Must-Detect finding detected
- finding is evidence-bound
- contamination eligibility satisfied
```

Humanの過去Verdictとの一致率は主評価にしません。

主評価は、predefined acceptance contractとreview findings / evidenceの対応です。

## Contamination eligibility

```text
Contamination = NONE
→ eligible for evaluation

Contamination = POSSIBLE / UNKNOWN
→ case alone cannot establish Pilot PASS

Contamination = PRESENT
→ case cannot PASS

ExcludedItemIntentionallyRetrieved != NO
→ case cannot PASS
```

## Fixture boundary

この候補文書には、Case A/Bの実fixture、Expected Findings、Must-Detect oracle、scoring keyを保存しません。

Fixtureは `Human Pilot Evaluation Start GO` 後にEvaluator-side temporary artifactとして用意します。

## Pilot output

各Caseは `review-output-contract.md` に従って結果を返します。

Pilot結果は後続のIndependent Pilot Evidence Reviewへ渡します。

Pilot実行だけではPromotionを承認しません。
