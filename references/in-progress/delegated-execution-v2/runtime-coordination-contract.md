# Runtime Coordination Contract

この契約は、`DELEGATED-EXECUTION-V2` が明示的にactivateされた workstream において、複数runtime間で「現在どのActivationに従い、次に何のEvidenceが必要か」を一意に再構成するための coordination overlay です。

この契約は `references/accepted/agent-operating-foundation-v1/readback-contract.md` を置き換えません。

accepted Readback Contract が常に controlling authority です。

```text
current GitHub state / exact evidence
> marker text
> handoff / old NEXT / conversation summary
```

Marker は locator であり、Human authority、review verdict、evidence satisfaction を生成しません。

## Applicability

この契約は次を満たす workstream にだけ適用します。

```text
Human Delegation Activation GO = explicit / consumed
DELEGATED-EXECUTION-V2 = applicable
```

Activation がない workstream に marker semantics を一般化しません。

## Marker 1 — Active V2 Activation

V2-activated workstream は、governing Activation evidence を指す current marker を持ちます。

Minimum shape:

```text
Evidence-Type: V2-COORDINATION-MARKER
Marker-Type: V2-ACTIVE-ACTIVATION
Marker-Id: <stable id>
Marker-State: ACTIVE
Workstream: <workstream id>
Activation-Evidence: <direct GitHub evidence identity>
Activation-Main: <exact SHA>
Supersedes-Marker: <marker id | NONE>
```

Semantics:

```text
Marker != Human GO
Marker != new repository authority
Marker != replacement for explicit Human Activation evidence
Marker != proof that Activation remains usable after contradictory current evidence
```

Executor は marker が指す underlying Human Activation evidence を直接readbackできなければなりません。

## Marker 2 — Required Next Evidence

V2 が specific evidence 待ちで停止するとき、current required evidence を指す marker を記録します。

Minimum shape:

```text
Evidence-Type: V2-COORDINATION-MARKER
Marker-Type: V2-REQUIRED-NEXT-EVIDENCE
Marker-Id: <stable id>
Marker-State: REQUIRED | NONE
Workstream: <workstream id>
Activation-Evidence: <governing activation evidence>
Required-Evidence: <exact evidence type / issue / review target | NONE>
Required-Baseline: <exact SHA / PR HEAD / binding | N/A>
Supersedes-Marker: <marker id | NONE>
```

Examples:

```text
Fresh Scope Re-Review on main@<sha>
Fresh Implementation Review on PR #<n>@<head>
Human Visual Acceptance for <candidate identity>
Human Live GO for <release identity>
```

Marker text itselfはrequired evidenceを満たしません。

```text
Required-Evidence marker exists
!= Required evidence observed
!= Review PASS
!= Human GO
```

## State = NONE

現在の中間required evidenceがすべて直接観測され、次のauthorized V2 actionを検討できる場合は、prior REQUIRED markerを明示的にsupersedeして次を記録できます。

```text
Marker-Type = V2-REQUIRED-NEXT-EVIDENCE
Marker-State = NONE
Required-Evidence = NONE
Reason = all currently required intermediate evidence observed
```

`NONE` は PASS、Ready、Merge authority、Human GO ではありません。

通常のV2 auto-continue predicatesは引き続きすべて必要です。

## Supersession and ambiguity

Marker currentness は chronological recency だけで決めません。

同一 `Workstream + Marker-Type` について、明示された `Supersedes-Marker` chain を適用して current candidate を決めます。

V2 continuation に marker が必要な状況で、unsuperseded current marker が0件または複数件残る場合:

```text
Marker state = UNKNOWN
Auto-continue = HOLD
Mutation = HOLD
Ready / Merge = HOLD
```

新しいmarkerは、置き換えるprior markerがある場合、そのMarker-Idを明示的にsupersedeします。

## Mandatory fresh readback

V2 executor は、次の直前にfresh readbackを行います。

```text
repository mutation
PR Ready transition
Merge
production / external action
```

最低限、直接再構成するもの:

```text
1. current GitHub main / PR metadata
2. current exact HEAD where applicable
3. current V2-ACTIVE-ACTIVATION marker
4. underlying explicit Human Delegation Activation evidence
5. current V2-REQUIRED-NEXT-EVIDENCE marker
6. required evidenceが実際に存在し、baseline / HEAD bindingが一致するか
7. unresolved P0 / P1 / UNKNOWN
8. applicable CI target SHA / status / conclusion when CI exists
9. current authority IN / OUT boundary
10. current scope boundary
```

accepted `readback-contract.md` のauthority orderを使用します。

Marker と current GitHub state が矛盾する場合、current GitHub stateが優先されます。

## Required evidence satisfaction

Required evidence を satisfied と扱うには、marker記述ではなく対象Evidenceを直接観測します。

Reviewの場合:

```text
review identity = observed
verdict = observed
P0 / P1 state = observed
reviewed baseline / Reviewed-HEAD = current bindingと一致
```

Human evidenceの場合:

```text
explicit Human input evidence = observed
required candidate / release binding =一致
```

CIの場合:

```text
CI target SHA = current exact HEAD
status / conclusion = successful
```

Applicable CI がない場合は既存V2 semanticsどおり:

```text
Applicable CI = NONE
CI PASS = NOT DECLARED
```

## Stale legacy next-step rejection

次の情報は、それだけではcurrent continuation authorityになりません。

```text
old chat handoff
old NEXT
historical gate order
superseded marker
old review PASS
old PR HEAD
historical scope state
conversation summary
```

current Required-Next-Evidence が `REQUIRED` で、対象Evidenceが未充足またはbinding不一致なら:

```text
stale legacy continuation instruction = REJECT
Action = HOLD
```

Historical Human GO は、その元のbounded actionに対するhistorical authorityとして保持します。

このruleは過去のHuman Gateを消去・書換えしません。

新しいHuman authorityが必要なら、accepted Human Gate semanticsに従うexplicit Human inputが必要です。

## Interaction with V2 auto-continue

Runtime coordination reconciliation はauto-continueの前提条件です。

```text
Active Activation marker = unique / reconstructed
Underlying Human Activation evidence = observed
Required Next Evidence marker = unique / reconstructed
Required evidence state = directly reconciled
No stale-continuation conflict
```

これらが満たされても、既存V2 predicatesを省略できません。

特に:

```text
P0 = 0
P1 = 0
Independent Review = PASS
Reviewed-HEAD == current exact HEAD
prior PASS not inherited across HEAD move
authority boundary unchanged
scope boundary unchanged
required evidence observable
applicable CI semantics satisfied
```

## Case 3 operational evidence

`BRAND-SYSTEM-SKILL-EXTRACTION-V1 / Case 3` では、HEAD move後にFresh Scope Re-Reviewがrequiredと記録されたにもかかわらず、別runtimeが旧lifecycle stateからimplementationへ進みました。

この事象は:

```text
Case 3 V2 operational evidence = P1 coordination-conformance defect
```

として保持します。

この契約はCase 3をPASSへ書換えず、PR #236を遡及無効化もしません。

## Human authority preservation

```text
Marker presence != Human GO
Marker supersession != Human GO
Required-Evidence NONE != Human GO
Independent Review PASS != Human Ready / Merge GO
```

Ready / Merge のHuman authority sourceは既存 `delegated-execution-contract.md` の規則から変更しません。

Human Visual Acceptance / Human Live GO が必要なpathも変更しません。

## Fail conditions

次の場合はfail-closedです。

```text
Active Activation marker absent or ambiguous when required
underlying Activation evidence unavailable
Required Next Evidence marker absent or ambiguous when required
required evidence unavailable
required baseline / HEAD mismatch
marker textをevidence satisfactionとして扱う
markerをHuman GOとして扱う
chronological recencyだけでmarker currentnessを決める
stale legacy NEXTでunsatisfied evidenceを迂回する
markerでaccepted Readback authorityをoverrideする
Case 3 defectをretroactive PASSへ書換える
```

## Scope boundary

このcontractは coordination evidence model だけを定義します。

次は非対象です。

```text
references/accepted/** mutation
AGENTS.md mutation
root README mutation
CI / workflow mutation
telemetry / daemon / event store
database / external service
Promotion
production / external release
new Human Gate vocabulary
```

## Promotion boundary

このcontractの実装・成功だけで `DELEGATED-EXECUTION-V2` をPromotionしません。

```text
Promotion = HOLD
Case 4 = HOLD
```

Case 4 は、次の両方が直接観測されるまで開始しません。

```text
1. exact-HEAD Fresh Independent Implementation Review = PASS / REVIEW-CLEARED
2. bounded correction PR merge = COMPLETE
```

Implementation Review clearance だけでは Case 4 を開始できません。merge 完了前の Case 4 は `HOLD` です。
