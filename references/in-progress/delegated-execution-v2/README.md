# DELEGATED-EXECUTION-V2

委任作業を、承認済み境界の中で自律的に最後まで進めるための in-progress operating-mode candidate です。

人間は工程遷移の許可ではなく、委任範囲・視覚的採否・本番反映を判断します。

## Status

```text
Authority class              = references/in-progress/ candidate
Human Delegation Activation  = GO / CONSUMED (this workstream)
Independent Definition Review= PASS (Re-Review-2)
Independent Scope Review     = PASS
Runtime Coordination         = candidate correction added / implementation review required
Promotion                    = HOLD
Human Visual Acceptance      = N/A (non-visual candidate)
Human Live GO                = NOT REQUIRED for this candidate
Accepted authority           = NO
```

このパスは accepted authority ではありません。

Independent Review PASS は Human GO ではありません。

Ready / Merge の Human authority は、IN に当該 candidate の merge を含む Human Delegation Activation GO だけです。

Runtime coordination marker は Human GO、Review PASS、required evidence satisfaction の代替ではありません。

accepted `references/accepted/agent-operating-foundation-v1/readback-contract.md` がreadbackの controlling authorityです。

## Contracts

- `delegated-execution-contract.md` — 基本フロー、自動継続、強制停止
- `runtime-coordination-contract.md` — Active Activation / Required Next Evidence marker、fresh readback、stale continuation rejection
- `human-gate-model.md` — 標準Human Gate 3種と廃止する通常停止点
- `correction-loop-contract.md` — 自律Correctionと上限
- `visual-evidence-path.md` — 視覚成果物の証拠列と Agent Visual Review
- `compatibility.md` — accepted Operating Foundation との共存規則

## Runtime coordination summary

Active V2 workstream では、repository mutation、Ready、Merge、production / external actionの直前にcurrent stateをfresh readbackします。

```text
current GitHub state
current exact HEAD
current Active V2 Activation marker
underlying explicit Human Activation evidence
current Required Next Evidence marker
required evidence direct observation + baseline / HEAD binding
unresolved P0 / P1 / UNKNOWN
applicable CI state when CI exists
```

Current markerが0件または複数件で一意に再構成できない場合は `UNKNOWN / HOLD` です。

古いhandoff / NEXT / historical gate stateは、current Required Next Evidenceが未充足ならcontinuation authorityとして拒否します。

Markerが `Required-Evidence = NONE` を示しても、それ自体はPASSでもHuman GOでもありません。既存V2 auto-continue predicatesをすべて満たす必要があります。

## Case 3 carry-forward

`BRAND-SYSTEM-SKILL-EXTRACTION-V1 / Case 3` で確認された cross-runtime coordination defect はOperational Evidence上のP1として維持します。

```text
Case 3 = not rewritten into PASS
PR #236 = not retroactively invalidated
Runtime Coordination Correction = prevention for later execution
```

## Locked Definition / Scope evidence

- `DEFINITION.md` — locked Definition（Implementationで内容を変更しない）
- `IMPLEMENTATION-SCOPE.md` — locked Implementation Scope
- `evidence/` — Independent Review evidence

## Out of scope for this candidate

```text
references/accepted/** mutation / Promotion
accepted Operating Foundation rewrite
AGENTS.md / root README mutation
CI / workflow / telemetry / daemon / event-store mutation
Deploy / Print / Publish / Live mutation
unrelated workstream gate rewrite
new Human Gate vocabulary
```
