# Typed Evidence Contract

この文書は、compact-mode workstreamでEvidence Chainを少数のGitHub artifactへ格納するための記録契約です。

目的はEvidenceを減らすことではありません。

目的は、Review、Correction、Human Gate、readback evidenceを別Issueへ分割せず、Lifecycle Issueと必要時のImplementation PRだけで再構成できるようにすることです。

## 適用モデル

compact-modeの基本単位は次です。

```text
1 workstream
= 1 Lifecycle Issue
+ optional 1 Implementation PR
```

Independent Review、Correction、Re-Review、Human Gate、Implementation Scope、Closure Reviewは、独立workstreamにならない限り新しいIssueを必要としません。

独立したblocker、別担当・別release、別Definition、または元Acceptance Criteriaでは完了判定できない新テーマは別workstreamとして扱えます。

## 共通identity fields

compact-modeで作成するtyped Evidence commentは、少なくとも次のfieldを持ちます。

```text
Evidence-Type: <enumerated type>
Workstream: <stable workstream id>
Evidence-Id: <stable unique id inside workstream>
Evidence-Revision: <positive integer>
Evidence-State: CURRENT | SUPERSEDED
Supersedes-Evidence: <Evidence-Id> | NONE
Lifecycle-Issue: #<number>
```

`Evidence-Id`を別のsemantic stageへ再利用しません。

同じEvidence系列を修正する場合は、新しいEvidence nodeを作り、`Supersedes-Evidence`で旧nodeを明示的に指します。

時系列上の新しさだけではcurrent authorityを決定しません。

明示されたsupersessionを適用した後にCURRENT候補が0件または複数件残る場合は、状態をUNKNOWNとしてHOLDします。

## V1 Evidence-Type enum

compact-mode V1で有効な`Evidence-Type`は次に限定します。

```text
INDEPENDENT-DEFINITION-REVIEW
DEFINITION-CORRECTION
HUMAN-GATE
IMPLEMENTATION-SCOPE
IMPLEMENTATION-SCOPE-CORRECTION
INDEPENDENT-IMPLEMENTATION-SCOPE-REVIEW
IMPLEMENTATION-BINDING
INDEPENDENT-IMPLEMENTATION-REVIEW
MERGED-MAIN-READBACK
```

この一覧にない`Evidence-Type`は自動的に有効なEvidenceとして扱いません。

新しいEvidence-Typeが必要な場合は、先にこのcontractを更新します。

未知のEvidence-Typeを検出した場合は、そのnodeをcurrent authorityへ補完せずUNKNOWN / HOLDとして扱います。

## Evidence-Typeごとの最小field

### INDEPENDENT-DEFINITION-REVIEW

```text
Review: <n>
Verdict: PASS | CORRECTION | HOLD
P0: <n>
P1: <n>
P2: <n>
Reviewed-Definition: <Definition-Id>
```

Reviewは対象Definitionを明示します。

Correction後のRe-Reviewは新しいEvidence nodeとして記録します。

### DEFINITION-CORRECTION

```text
Definition-Id: <new id>
Definition-Revision: <n+1>
Supersedes-Definition: <prior Definition-Id>
Definition-State: PROPOSED | LOCKED | SUPERSEDED
```

comment本文には、変更後authorityを再構成できる完全なauthoritative deltaを含めます。

### HUMAN-GATE

```text
Gate: <gate id>
Decision: GO | HOLD
Authority-Source: explicit human message
Related-Evidence: <Evidence-Id or stable comment id>
```

Human Gateは、人間の明示入力が確認できた場合だけ消費します。

Agent-created metadata、順序、周辺コメント、CI、Review PASSからHuman GOを生成・推定しません。

Definition / Scope Lock Gateには、この節のfieldに加えて`Definition content anchor`節のfieldが必要です。

### IMPLEMENTATION-SCOPE

```text
Scope-Id: <stable scope id>
Scope-State: PROPOSED | LOCKED | SUPERSEDED
```

Scope Correctionは新しいscope Evidence nodeを作り、旧scopeを明示的にsupersedeします。

### IMPLEMENTATION-SCOPE-CORRECTION

```text
Scope-Id: <new stable scope id>
Scope-State: PROPOSED | LOCKED | SUPERSEDED
Supersedes-Evidence: <prior scope Evidence-Id>
```

変更していないscope条件をcarry-forwardする場合は、その範囲をcomment本文で明示します。

### INDEPENDENT-IMPLEMENTATION-SCOPE-REVIEW

```text
Reviewed-Scope: <Scope-Id>
Verdict: PASS | CORRECTION | HOLD
P0: <n>
P1: <n>
P2: <n>
```

Re-Reviewは同じEvidence-Typeの新しいrevisionとして記録し、`Supersedes-Evidence`で旧Reviewを指します。

### IMPLEMENTATION-BINDING

```text
Implementation-PR: #<n>
Implementation-HEAD: <40-char exact commit SHA>
Reviewed-Scope: <Scope-Id>
```

Lifecycle Issue側にこのEvidenceを記録し、Implementation PR bodyから同じWorkstreamとLifecycle Issueへ逆向きに到達できる必要があります。

### INDEPENDENT-IMPLEMENTATION-REVIEW

```text
Implementation-PR: #<n>
Reviewed-HEAD: <40-char exact commit SHA>
Verdict: PASS | CORRECTION | HOLD
P0: <n>
P1: <n>
P2: <n>
```

PR HEADが変わった場合、以前のReview PASSを新HEADへ継承しません。

### MERGED-MAIN-READBACK

```text
Implementation-PR: #<n>
Merged-HEAD: <exact merge/main SHA as applicable>
Merge-State: MERGED
CI-State: <explicit status/conclusion or NOT_APPLICABLE>
```

`NOT_APPLICABLE`は`PASS`ではありません。

## canonical Definitionの再構成

compact-modeではDefinition revisionを明示的なobjectとして扱います。

Lifecycle Issue bodyを`Definition-Revision: 1`のsourceとします。

最低限、workstreamは次のidentityを確定します。

```text
Workstream: <id>
Definition-Id: <id>
Definition-Revision: 1
Lifecycle-Issue: #<number>
```

Human Lock後にIssue bodyを編集してDefinition authorityを変更してはいけません。

Definition変更が必要な場合は、typed `DEFINITION-CORRECTION` commentを新しいDefinition revisionとして作成します。

`DEFINITION-CORRECTION`は、変更後のauthorityを再構成できる完全なauthoritative deltaを含めます。

```text
Definition-Id: <new id>
Definition-Revision: <n+1>
Supersedes-Definition: <prior Definition-Id>
Definition-State: PROPOSED
```

canonical Definitionは、Revision 1のLifecycle Issue bodyに、`Supersedes-Definition` chainで一意に選ばれたauthoritative deltaをrevision順に適用して再構成します。

chronologyだけでCorrection chainを選びません。

Human Lockは、lock対象のexact `Definition-Id`と`Definition-Revision`を明示します。

## Definition content anchor

compact-modeのHuman Definition / Scope Lockは、locked Definitionのexact contentをSHA-256へbindingします。

```text
Definition-Id: <stable id>
Definition-Revision: <positive integer>
Definition-Content-SHA256: <sha256 of exact canonical Definition content>
Lifecycle-Issue: #<number>
Decision: GO | HOLD
```

`Definition-Content-SHA256`はintegrity metadataです。

このhash自体はHuman authorityを作りません。

Readbackでは、再構成したcanonical Definition contentのSHA-256とlocked hashを比較します。

```text
current reconstructed canonical Definition content SHA256
=
locked Definition-Content-SHA256
```

一致しない場合は、後続のauthorized Definition Correction、independent review、Human re-lock chainが確認できるまで次の状態とします。

```text
Canonical Definition = UNKNOWN
Mutation             = HOLD
```

## Independent Reviewのsupersession

各Review revisionは、reviewしたDefinitionまたはScopeを明示します。

Correction / Re-Reviewは元Reviewを編集して置換せず、新しいEvidence nodeとして作成します。

例:

```text
Evidence-Id: EXAMPLE-DEF-REVIEW-002
Evidence-Revision: 2
Evidence-State: CURRENT
Supersedes-Evidence: EXAMPLE-DEF-REVIEW-001
Reviewed-Definition: EXAMPLE-DEF-002
```

superseded Reviewをcurrent authorityとして扱いません。

## Lifecycle IssueとImplementation PRのbinding

repository mutationが必要なworkstreamでは、Lifecycle IssueとImplementation PRを双方向にbindingします。

Lifecycle Issue側のEvidenceは次を記録します。

```text
Lifecycle-Issue: #<issue>
Implementation-PR: #<pr>
```

Implementation PR bodyは次を記録します。

```text
Workstream: <workstream id>
Lifecycle-Issue: #<issue>
```

Implementation PRをIssueやWorkstreamへ結びつける情報が不足する場合は、readbackで推定せずUNKNOWN / HOLDとします。

## exact HEAD binding

implementation reviewはPR番号とexact HEADを同時に記録します。

```text
Implementation-PR: #<pr>
Reviewed-HEAD: <40-char exact SHA>
```

PR HEADが`Reviewed-HEAD`と異なる場合、そのReviewをcurrent validationとして扱いません。

新しいHEADには新しいreview evidenceが必要です。

## CI SHA binding

applicable CIが存在する場合、status / conclusionだけではなく対象SHAを確認します。

CI PASSとして使えるのは、accepted readback contractが要求するapplicable SHAへbindingされたsuccessful conclusionだけです。

pending、failed、cancelled、skipped等をPASSへ補完しません。

applicable CIが存在しない場合は、`NOT_APPLICABLE`または「存在しないことをauthoritative readbackした状態」として記録し、CI PASSとは表現しません。

## UNKNOWNとambiguity

次の場合はfail-closedにします。

- current Evidence nodeを一意に選べない。
- supersession chainが途切れる、循環する、または複数に分岐する。
- Evidence-TypeがV1 enumに含まれない。
- canonical Definitionを一意に再構成できない。
- Definition content hashがlocked hashと一致しない。
- Human GOの明示入力を確認できない。
- Lifecycle IssueとImplementation PRのbindingを確認できない。
- Implementation Reviewがcurrent exact HEADへbindingされていない。
- CIの対象SHAを確認できない。

```text
State  = UNKNOWN
Action = HOLD or additional readback
```

UNKNOWNをPASS、CONSUMED、MERGED、CLOSEDへ補完しません。

## 既存Evidenceとの互換性

このcontractは、既存のmulti-Issue Evidence Chainを自動変換しません。

既存Issueを一括closeしません。

既存Review Issueを自動的にtyped commentへ移しません。

compact-modeが明示的に適用されたworkstreamだけがこのgrammarを新規Evidenceへ使用します。

## EVIDENCE-CHAIN-COMPACTION-V1 bootstrap mapping

Issue #183は、このgrammarとDefinition content anchorが確立する前に開始したbootstrap Pilotです。

#183のpre-scope artifactに限り、次のbounded mappingを使用します。

```text
Issue #183 body
→ Definition-Id: ECFV1-DEF-001
→ Definition-Revision: 1

issuecomment-5632989276
→ Evidence-Id: ECFV1-DEF-REVIEW-001
→ Evidence-Type: INDEPENDENT-DEFINITION-REVIEW

issuecomment-5633005076
→ Evidence-Id: ECFV1-GATE-DEFLOCK-001
→ Evidence-Type: HUMAN-GATE
→ Gate: DEFINITION-SCOPE-LOCK
```

このmappingは過去コメントを書き換えません。

このmappingを、過去コメントがすでにpost-contract grammarを満たしていた証拠として扱いません。

#183のHuman Definition Lockは`Definition-Content-SHA256`必須化前に消費されたため、pre-scope Definition integrity testは`BOOTSTRAP-LIMITED`です。

`BOOTSTRAP-LIMITED`をcontent-anchor enforcement PASSとして扱いません。

compact modelを一般にprovenとしてPromotionする前に、contract適用後に開始した別workstreamで`Definition-Content-SHA256`のlock/readback経路を検証します。

このbootstrap例外を他workstreamへ一般化しません。

## 新しいIssueを作る境界

次のEvidence stageだけを理由に新Issueを作りません。

```text
Independent Review
Correction
Re-Review
Human Gate
Implementation Scope
Scope Review
Ready判定
Closure Review
```

新Issueは、独立して継続するblocker、別担当・別release、別Human Gateを持つ独立scope、または元Acceptance Criteriaでは完了判定できない新テーマに限定します。

## Completion criteria

compact-modeのreadbackは、prior conversationなしで少なくとも次を一意に復元できる場合に成立します。

1. canonical Definition
2. latest independent review
3. consumed Human Gates
4. next unconsumed Human Gate
5. implementation PRとcurrent exact HEAD
6. merge / draft / open state
7. applicable canonical contracts
8. applicable CIの対象SHA・status・conclusion
9. unresolved findings
10. evidence gaps
11. permitted next action
12. current typed Evidence nodeとsupersession chain
13. locked Definition content anchor
14. Lifecycle IssueとImplementation PRのbinding

Human authority、UNKNOWN、stale HEAD、CI、live-stateの既存境界は`readback-contract.md`および`operating-contract.md`を優先します。
