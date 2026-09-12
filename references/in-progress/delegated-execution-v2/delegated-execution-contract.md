# Delegated Execution Contract

この契約は、Human Delegation Activation GO が消費された workstream にだけ適用する。

Activation が無い workstream では、既存の Operating Foundation / workstream gate vocabulary を変えない。

## 基本フロー

```text
Human Delegation Activation GO
        ↓
Definition
        ↓
Independent Definition Review
        ↓
Correction Loop
        ↓
Implementation Scope
        ↓
Independent Scope Review
        ↓
Correction Loop
        ↓
Implementation
        ↓
Build / Test / CI
        ↓
Independent Implementation Review
        ↓
Correction Loop
        ↓
Rendered Evidence          (visual only)
        ↓
Agent Visual Review        (visual only)
        ↓
Visual Correction Loop     (visual only)
        ↓
Human Visual Acceptance    (visual only)
        ↓
Finalization
        ↓
Ready / Merge
        ↓
Human Live GO              (production / external only)
        ↓
Production / External Release
```

## 自動継続条件

承認済み境界の中では、次をすべて満たすとき追加の Human GO を要求しない。

```text
P0 = 0
P1 = 0
Independent Review = PASS
Reviewed-HEAD == current exact HEAD
Prior Independent Review PASS is not inherited across HEAD moves
Authority boundary = unchanged
Scope boundary = unchanged
Required evidence = observable
Runtime coordination readback = reconciled
No production mutation
No secret / credential mutation
No irreversible external action
```

`Runtime coordination readback = reconciled` は `runtime-coordination-contract.md` に従う。

MarkerはHuman authorityやReview PASSを生成せず、accepted `readback-contract.md` が常にcontrolling authorityである。

applicable CI がある場合:

```text
CI target SHA == current exact HEAD
CI status / conclusion = successful
```

applicable CI が無い場合:

```text
Applicable CI = NONE
CI PASS       = NOT DECLARED
```

applicable CI の不在を CI PASS と叙述しない。

### Required evidence minimum

少なくとも次が推論なしで再構成できること。

```text
canonical Definition identity
latest Independent Review identity + verdict bound to Reviewed-HEAD
consumed Human Delegation Activation GO
current V2-ACTIVE-ACTIVATION marker when runtime coordination applies
current V2-REQUIRED-NEXT-EVIDENCE marker when runtime coordination applies
underlying Activation evidence referenced by the marker
required-next evidence satisfaction state observed directly
Implementation PR identity when mutation exists
current exact HEAD
applicable CI target SHA / status / conclusion when CI exists
unresolved findings / UNKNOWN items
authority boundary IN / OUT for the Activation
```

P2 は記録して carry-forward できる。

## Runtime coordination prerequisite

Active V2 workstream では、repository mutation、PR Ready、Merge、production / external action の直前に `runtime-coordination-contract.md` に従うfresh readbackを行う。

最低限:

```text
current GitHub main / PR metadata
current exact HEAD
unique current V2-ACTIVE-ACTIVATION marker
underlying explicit Human Activation evidence
unique current V2-REQUIRED-NEXT-EVIDENCE marker
required evidenceの直接観測 + baseline / HEAD binding
unresolved P0 / P1 / UNKNOWN
applicable CI state when CI exists
```

current GitHub state と marker / handoff が矛盾する場合、accepted `readback-contract.md` のauthority orderに従い current GitHub stateを優先する。

Marker text自体をevidence satisfactionとして扱わない。

古い `NEXT`、handoff、historical gate state、old review PASSは、current Required-Next-Evidenceが未充足ならcontinuation authorityとして使用しない。

## 強制停止条件

次のいずれかで自動進行を停止する。

```text
P0 >= 1 and not safely correctable inside boundary
P1 >= 1 and not safely correctable inside boundary
Review = HOLD / FAIL
Required evidence = UNKNOWN
Reviewed-HEAD != current exact HEAD
Prior Independent Review PASS would need inheritance across a HEAD move
Applicable CI exists and target SHA != current exact HEAD
Applicable CI exists and status / conclusion is not successful
Active Activation marker required but absent / ambiguous
Required Next Evidence marker required but absent / ambiguous
Required Next Evidence = REQUIRED and target evidence is absent / mismatched
stale legacy NEXT / handoff conflicts with current required evidence
Authority interpretation required
Authority boundary change required
Scope expansion required
Human judgment explicitly required
Production / external mutation required
Correction loop limit exceeded
Attempt to treat marker presence as Human GO or evidence satisfaction
Attempt to treat Independent Review PASS as Human Ready / Merge GO
```

UNKNOWN を PASS として扱わない。

Human Gate を推定・生成・代替しない。

Marker ambiguityをchronological recencyだけで解消しない。

## Correction

修正可能な finding は人間を呼ばずに直す。詳細は `correction-loop-contract.md`。

```text
MAX_CORRECTION_LOOPS = 3
```

## Ready / Merge authority

Ready / Merge の Human authority は、IN に当該 candidate の merge を明示する Human Delegation Activation GO だけである。

Independent Review PASS と自動継続条件は、その Human grant の必要条件であり、Human GO そのものでも代理でもない。

Runtime coordination marker、marker supersession、`Required-Evidence = NONE` もHuman GOではない。

## 非対象

```text
accepted Operating Foundation rewrite
Promotion by this contract alone
secret / credential mutation
production / external / irreversible action without Human Live GO
Agent/Skill minting of Human GO
marker-based minting / inference / proxy-consumption of Human GO
```
