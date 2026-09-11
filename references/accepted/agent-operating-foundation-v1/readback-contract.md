# Readback / Reconstruction Contract

Readbackは、前任エージェントの会話履歴がなくてもrepository上の証拠から現在地を再構成するための契約です。

V1ではsession event storeを導入しません。

GitHub上の既存artifactをEvidence Chainとして扱います。

## 最小Evidence Chain

既存workstreamでは、確認できるartifactを次の順序で読みます。

```text
Issue Definition
→ Independent Review
→ Human Gate comment
→ implementation PR
→ exact HEAD
→ applicable CI status / conclusion and review evidence
→ merge state
→ next unconsumed gate
```

compact-modeでは、Definition以外のEvidence stageを別Issueへ分割する必要はありません。

```text
Lifecycle Issue
├─ Definition
├─ typed Independent Review / Correction / Human Gate evidence
└─ next unconsumed gate

optional Implementation PR
├─ exact HEAD
├─ applicable CI
├─ typed implementation review / Human Gate evidence
└─ merge state
```

compact-modeのtyped evidenceは`typed-evidence-contract.md`に従います。

各段階は、存在が確認できた証拠だけを採用します。

applicable CIが存在する場合は、対象SHA、status、conclusionを同じ証拠列で確認します。

applicable CIが存在しない状態は、CI PASSとは表現しません。

## 再構成する状態

保守エージェントは少なくとも次を復元します。

1. canonical Definition
2. latest independent review
3. consumed Human Gates
4. next unconsumed Human Gate
5. implementation PRとexact HEAD
6. merge / draft / open state
7. applicable canonical contracts
8. applicable CIの対象SHA・status・conclusion（存在する場合）
9. unresolved findings
10. evidence gaps
11. permitted next action

compact-modeでは、さらに次を確認します。

1. Lifecycle Issue
2. Workstream
3. current Evidence-Idとsupersession chain
4. locked DefinitionのDefinition-Id、Definition-Revision、Definition-Content-SHA256
5. Lifecycle IssueとImplementation PRの相互binding
6. ReviewとCIがcurrent exact HEADへbindingされていること

## compact-modeのcanonical Definition

compact-modeのHuman Definition / Scope Lockは、locked Definitionをcontent anchorへbindingします。

```text
Definition-Id: <stable id>
Definition-Revision: <positive integer>
Definition-Content-SHA256: <sha256 of exact canonical Definition content>
Lifecycle-Issue: #<number>
Decision: GO | HOLD
```

Readbackでは、再構成したcanonical Definition contentのSHA-256をlocked `Definition-Content-SHA256` と照合します。

一致しない場合は、後続のauthorized Definition Correction、independent review、Human re-lock chainが確認できるまでfail-closedにします。

```text
Canonical Definition = UNKNOWN
Mutation             = HOLD
```

Human Gate authorityはcontent hashから生成しません。

Human Gate authorityは人間の明示入力だけから成立します。

## typed Evidenceのcurrent判定

compact-modeのEvidenceは`Evidence-Id`、`Evidence-Revision`、`Evidence-State`、`Supersedes-Evidence`を使ってcurrent nodeを決定します。

時系列上もっとも新しいコメントであることだけをauthority判定に使いません。

明示されたsupersessionを適用した後にCURRENT候補が0件または複数件残る場合は、状態をUNKNOWNとしてHOLDします。

CorrectionやRe-Reviewは元Evidenceを上書きせず、新しいEvidence nodeとして記録します。

## Lifecycle IssueとImplementation PRのbinding

compact-modeでrepository mutationを行う場合は、Lifecycle IssueとImplementation PRを明示的にbindingします。

Lifecycle Issue側のEvidenceは対象PRを識別できる情報を持ちます。

PR側のEvidenceは対象Lifecycle IssueとWorkstreamを識別できる情報を持ちます。

implementation reviewは`Implementation-PR`と`Reviewed-HEAD`を持ち、current exact HEADへbindingします。

PR HEADが更新された場合、以前のimplementation review PASSは新HEADへ自動継承しません。

applicable CIも対象SHAがcurrent exact HEADと一致することを確認します。

## Authority order

状態が食い違う場合は、最新の実体readbackを優先します。

```text
1. current GitHub state / current PR metadata
2. exact commit / diff / CI evidence
3. Human Gate comments
4. locked Definition / independent review evidence
5. handoff summary
```

ただし、Human Gate authorityそのものは人間の明示入力以外から生成しません。

compact-modeでも同じauthority orderを維持します。

## UNKNOWNの扱い

取得不能と「存在しない」を区別します。

```text
not found after authoritative readback
≠
readback unavailable
```

確認できない状態は次のように扱います。

```text
State  = UNKNOWN
Action = HOLD or additional readback
```

UNKNOWNをPASS、CLOSED、MERGED、CONSUMEDへ補完しません。

compact-modeでは、Evidence identity、supersession、Definition content anchor、Issue/PR binding、exact HEAD bindingのambiguityもUNKNOWNとして扱います。

## Stale evidence

過去のHEADやhandoffに書かれたstateをcurrentとして扱いません。

PRに新しいcommitがある場合、以前のreview PASSは新HEADへ自動継承しません。

exact HEADに対する証拠かを確認します。

applicable CIについても、別SHAのstatusやconclusionをcurrent validationとして扱いません。

compact-modeのsuperseded Evidenceもcurrent authorityとして扱いません。

## 既存workstreamとの互換性

この契約は、既存のmulti-Issue Evidence Chainを無効化しません。

既存workstreamをcompact-modeへ自動移行しません。

過去Issueを一括closeしません。

compact-modeが明示的に適用されたworkstreamだけが`typed-evidence-contract.md`の追加規則を使います。

## EVIDENCE-CHAIN-COMPACTION-V1 bootstrap境界

`EVIDENCE-CHAIN-COMPACTION-V1` Issue #183は、このcontractが成立する前にDefinition Lockが消費されたbootstrap Pilotです。

Issue #183のpre-scope Definition integrityは`BOOTSTRAP-LIMITED`として扱います。

Issue #183を、`Definition-Content-SHA256`によるlock/readback経路を成功検証した証拠として扱いません。

compact modelを一般にprovenとしてPromotionする前に、contract適用後に開始した別workstreamでcontent-anchor経路を実際に検証します。

このbootstrap例外を新しいcompact-mode workstreamへ一般化しません。

## Live stateの境界

repository readbackだけで次を断定しません。

- rendered UIの見え方
- live integrationの成功
- real staff / real user value
- runtime failureの不存在
- production deploymentの健全性

これらは`observability-boundary.md`に従います。

## Pilot input candidate

将来のhandover pilotでは、次の最小入力を想定します。

```text
- repository URL
- target workstream ID
- prior conversation unavailable
```

この入力だけから現在地と次操作を復元できるかを評価します。

## Fail conditions

- Human GOを推定する。
- stale HEADをcurrent扱いする。
- UNKNOWNをPASS扱いする。
- reference candidateをaccepted authority扱いする。
- applicable CIの存在だけを成功したvalidationとして扱う。
- pending、failed、cancelled等のnon-successful CIをPASS扱いする。
- applicable CIが存在しない状態をCI PASSと表現する。
- live runtime stateをrepository evidenceだけで断定する。
- next unconsumed gateを飛ばす。
- chronological recencyだけでtyped Evidenceのcurrent nodeを決める。
- superseded Evidenceをcurrent authorityとして扱う。
- Definition content anchor不一致を無視する。
- Lifecycle IssueとImplementation PRのbindingを推定する。
- old implementation reviewを新しいPR HEADへ継承する。
- Issue #183のbootstrap制限をcontent-anchor enforcement PASSとして扱う。

## Completion criteria

Readbackは、再構成した各状態に確認可能なEvidence Chainがあり、applicable CIが存在する場合は対象SHA・status・conclusionが明示され、未確認項目がUNKNOWNとして示され、次の許可操作がHuman Gateを迂回していないときに完了します。

compact-modeでは、typed Evidenceのcurrent node、locked Definition content anchor、Lifecycle IssueとImplementation PRのbinding、current exact HEADへのreview / CI bindingも一意に再構成できる必要があります。
