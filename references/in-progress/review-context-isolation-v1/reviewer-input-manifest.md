# Reviewer Input Manifest

Reviewerへ渡すtask-specific inputを固定するための契約です。

## Required fields

```text
ReviewId
ReviewedRepository
ReviewedArtifactIdentity
DefinitionIdentity
LockedScopeIdentity
AcceptanceCriteriaIdentity
AllowedInputs
ExcludedInputs
DeclaredAmbientContext
ExpectedFindingsVisibility
MutationAuthority
```

## Required values

```text
ExpectedFindingsVisibility = HIDDEN
MutationAuthority = NONE
```

## AllowedInputs

Reviewerへ明示的に供給するtask-specific inputだけを列挙します。

V1の既定候補は次です。

```text
reviewed diff / artifact
locked Definition
locked Scope
Acceptance Criteria
required deterministic test results
relevant accepted repository authority
```

実際のReviewでは、各項目をpath、SHA、blob、URLなどのidentityへ結び付けます。

## ExcludedInputs

最低限、次はtask-specific inputとして供給しません。

```text
implementer conversation transcript
implementer private reasoning
implementer self-review / self-verdict
previous reviewer verdict
Human expected verdict
hidden pilot expected findings
handoff summary that reveals the expected answer
```

`Excluded` は `Inaccessible` を意味しません。

Excluded itemがruntimeやtoolから到達可能でも、Reviewerは意図的に探索、取得、利用しません。

## DeclaredAmbientContext

task packet外から見える可能性がある情報を明示します。

最低限、観測可能な範囲で次を記録します。

```text
system / runtime instructions
root AGENTS.md or equivalent repository bootstrap
globally loaded rules
available tools
automatically loaded Skills / plugins
repository files reachable outside the explicit review packet
```

確認できない項目は `UNKNOWN` とします。

## Contamination boundary

Excluded itemをexecution中に観測した場合、またはblind resultへの影響を否定できない場合は、Review OutputでContaminationを記録します。

IR-L2で証明するのは次です。

```text
controlled task-specific input
excluded-input declaration
ambient-context declaration
reviewer declaration of excluded-item non-use
evidence-bound output
```

IR-L2は次を証明しません。

```text
tool/file accessが技術的に完全遮断された
hidden contextがruntime内部に存在しなかった
every read operation was independently audited
```

これらはIR-L3の対象です。

## Human authority

ReviewerはHuman GOを生成、推定、代理消費しません。

Reviewerのrepository mutation authorityはありません。
