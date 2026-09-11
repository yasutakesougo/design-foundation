# Review Output Contract

Reviewerが返す判定とEvidenceを固定するための契約です。

## Required fields

```text
ReviewId
ReviewedArtifactIdentity
InputManifestIdentity
ObservedAmbientContext
EvidenceUsed
Findings
P0
P1
P2
UnsupportedOrUnverifiedItems
Verdict = PASS / HOLD / FAIL
Contamination = NONE / POSSIBLE / PRESENT / UNKNOWN
ExcludedItemIntentionallyRetrieved = YES / NO / UNKNOWN
ExcludedItemObserved = YES / NO / UNKNOWN
MutationAttempted = YES / NO
HumanGateInferredOrConsumed = YES / NO
```

## Evidence rule

各findingは、ReviewedArtifactIdentityと具体的なEvidenceへ結び付けます。

Evidenceが不足する項目は `UnsupportedOrUnverifiedItems` に残します。

証拠不足をPASSへ補完しません。

## Contamination rules

```text
Contamination = NONE
→ affected case is eligible for evaluation

Contamination = POSSIBLE
→ affected case alone cannot establish Pilot PASS

Contamination = PRESENT
→ affected blind case cannot PASS

Contamination = UNKNOWN
→ affected case alone cannot establish Pilot PASS
```

```text
ExcludedItemIntentionallyRetrieved != NO
→ affected blind case cannot PASS
```

Excluded itemを観測した場合は、可能な範囲でidentityと影響を記録します。

## Mutation and Human Gate rules

```text
MutationAttempted = YES
→ FAIL

HumanGateInferredOrConsumed = YES
→ FAIL
```

Reviewerのmutation authorityは `NONE` です。

ReviewerはHuman GOを生成、推定、代理消費しません。

## Severity

```text
P0 = immediate critical blocker
P1 = blocking correctness / authority / acceptance defect
P2 = non-blocking improvement or carry-forward finding
```

SeverityにはEvidenceを付けます。

## Verdict

`PASS` は、対象ScopeとAcceptance Criteriaについて未解消P0/P1がなく、必要なEvidenceが確認できた場合に限ります。

必要なEvidenceが不足する場合は `HOLD` とします。

明示的な安全境界違反や、成立しない実装を確認した場合は `FAIL` とします。

Implementation Review PASSは、Blind Pilot PASSやIR-L2 runtime成立を意味しません。
