# REVIEW-CONTEXT-ISOLATION-V1

## Status

```text
Authority class = references/in-progress/ candidate
Definition / Scope = #171 + Definition Correction-1
Independent Definition Re-Review-2 = #173 / PASS
Human Definition / Scope Lock = GO / CONSUMED
V1 target = IR-L2 / Controlled Input
IR-L3 = OUT / HOLD
```

この候補は、Independent Reviewで使う入力と観測可能な周辺コンテキストを区別するための契約です。

`Fresh Context` と `Independent Review` は同義ではありません。

IR-L2では、task-specific inputを制御し、Excluded / Ambientを明示し、成果物とEvidenceへ判定を結び付けます。

IR-L2は、toolやfileへのアクセスが技術的に完全遮断されたことまでは証明しません。

その強いaccess proofはIR-L3へ残します。

## Contracts

- `reviewer-input-manifest.md`: Reviewerへ渡す入力と境界を定義します。
- `review-output-contract.md`: Reviewerが返すEvidenceとfail-closed判定を定義します。
- `blind-pilot-protocol.md`: Case A / BによるBlind Pilotの実行条件を定義します。

## Authority boundary

Reviewerのmutation authorityは `NONE` です。

ReviewerはHuman GOを生成、推定、代理消費しません。

証拠不足は `UNKNOWN / HOLD` に残します。

## External reference

ECCは設計上の外部参照です。

```text
External repository = affaan-m/ECC
Frozen reference SHA = c9148d0bb239ed01a95724a5928b98cdf9c30658
Authority role = NONE
Automatic sync = NOT AUTHORIZED
```

ECCの内容はこの候補へvendoringしません。

## Out of scope

```text
Pilot fixture / oracle materialization
ECC installation / vendoring
Skill Routing
Security Reviewer
Continuous Learning / Memory promotion
automatic reviewer spawning
root AGENTS.md mutation
review/* promotion
references/accepted/* mutation
CI / GitHub Actions mutation
runtime / tool permission mutation
telemetry / tracing
repository write automation
IR-L3 enforcement
Human Ready / Merge / Pilot Start / Promotion
Deploy / Publish / Print
```
