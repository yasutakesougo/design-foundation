# DELEGATED-EXECUTION-V2

委任作業を、承認済み境界の中で自律的に最後まで進めるための in-progress operating-mode candidate です。

人間は工程遷移の許可ではなく、委任範囲・視覚的採否・本番反映を判断します。

## Status

```text
Authority class              = references/in-progress/ candidate
Human Delegation Activation  = GO / CONSUMED (this workstream)
Independent Definition Review= PASS (Re-Review-2)
Independent Scope Review     = PASS
Promotion                    = HOLD
Human Visual Acceptance      = N/A (non-visual candidate)
Human Live GO                = NOT REQUIRED for this candidate
Accepted authority           = NO
```

このパスは accepted authority ではありません。

Independent Review PASS は Human GO ではありません。

Ready / Merge の Human authority は、IN に当該 candidate の merge を含む Human Delegation Activation GO だけです。

## Contracts

- `delegated-execution-contract.md` — 基本フロー、自動継続、強制停止
- `human-gate-model.md` — 標準Human Gate 3種と廃止する通常停止点
- `correction-loop-contract.md` — 自律Correctionと上限
- `visual-evidence-path.md` — 視覚成果物の証拠列と Agent Visual Review
- `compatibility.md` — accepted Operating Foundation との共存規則

## Locked Definition / Scope evidence

- `DEFINITION.md` — locked Definition（Implementationで内容を変更しない）
- `IMPLEMENTATION-SCOPE.md` — locked Implementation Scope
- `evidence/` — Independent Review evidence

## Out of scope for this candidate

```text
references/accepted/** mutation / Promotion
accepted Operating Foundation rewrite
CI / telemetry / secrets
Deploy / Print / Publish / Live mutation
unrelated workstream gate rewrite
```
