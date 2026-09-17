# DESIGN-SYSTEMS-FOUNDATION-CANDIDATE-V1

複数の成熟したDesign Systemから反復して確認された原則のうち、既存design-foundationに不足するものだけを、再利用可能なFoundation候補として定義する in-progress candidate です。

このディレクトリは accepted authority ではありません。

## Status

```text
Authority class                          = references/in-progress/ candidate
Workstream                               = DESIGN-SYSTEMS-FOUNDATION-CANDIDATE-V1
Lifecycle authority / Human Gate evidence = Issue #268
Implementation Baseline                  = main @ 09b3190adc46504f831443c2533ce8f096668cea
Implementation PR                        = #273
Merge Commit                             = aa4befeff8d8a810705209687fdf1ced08a7234a
Merge                                    = MERGED
Human Ready                              = GO / CONSUMED
Merge GO                                 = GO / CONSUMED
Foundation Promotion                     = NOT AUTHORIZED / NOT CONSUMED
Candidate Location                       = references/in-progress/ (PRESERVED)
Accepted authority                       = NO
```

このパスは accepted authority ではありません。

Definition Review PASS や Implementation Start GO は、Human Ready / Merge / Foundation Promotion を意味しません。

Human Gate語彙とaccepted operating authorityは再定義しません。

## Purpose

既存design-foundationに不足している次の判断規則を、Repositoryから参照可能な形で表現する候補です。

- F1 Reuse Before Custom Build
- F2 Semantic Foundation Before Raw Values
- F4 Predictable Orientation and Interaction
- F6 Customization Requires Evidence

F3 / F5 は既存の authority（`foundations/accessibility.md` 等）を使用するため、重複Foundationとして再定義しません。

## Candidate principles

この README だけを candidate 正本とします。

### F1 — Reuse Before Custom Build

新しいUI pattern / componentを独自設計する前に、既存Foundation、Pattern、platform-native capability、利用可能な既存componentを確認します。

独自設計は探索を省略する理由にはなりません。

特定外部Design Systemへの依存は追加しません。

### F2 — Semantic Foundation Before Raw Values

色、spacing、typography、state等を再利用する場合、可能な範囲で生の値そのものではなく、意味・役割を表すsemantic layerを優先します。

semantic layerは特定Design System固有のtoken名をコピーすることを意味しません。

外部Design System固有のtoken name / hierarchy / implementationをコピーしません。

既存 `foundations/colors.md`、`foundations/typography.md`、`foundations/spacing.md` 等との矛盾を作りません。

### F4 — Predictable Orientation and Interaction

利用者が、「現在地」「現在の状態」「可能な操作」「操作後に何が起きるか」を予測できる構造を優先します。

情報密度や視覚的新規性を、orientationとinteraction predictabilityより優先しません。

特定navigation componentや外部UI implementationを必須化しません。

### F6 — Customization Requires Evidence

既存Foundation / Pattern / componentから意図的に外れる場合、その変更が必要な理由を説明可能にします。

外部Design Systemと異なること自体は欠陥ではありません。

外部Design Systemへの一致自体も採用根拠にはしません。

## 既存Foundationとの関係

既存 `foundations/principles.md` と `foundations/accessibility.md` を正本として維持します。

このcandidateは既存authorityを置換・弱体化・意味変更しません。

既存原則と意味的に重複するFoundationを新設しません。

## Borrow / Do Not Copy

### Borrow

```text
semantic abstraction
reuse-first decision
predictable interaction
evidence-backed customization
cross-system recurring principles
```

### Do Not Copy

```text
brand expression
proprietary visual identity
system-specific token names
system-specific component composition
colors / typography / icons / illustrations
external system implementation wholesale
```

## Evidence boundary

DesignSystems.One = discovery / index source

Canonical evidence = relevant official Design System sources

External source = reference-only

## Promotion boundary

このDefinitionのPASSはFoundation Promotionを意味しません。

Definition Review PASS ≠ Repository Mutation ≠ Implementation Start ≠ Foundation Promotion

Foundationへの実際の導入・変更・昇格には、対応する明示的Human Gateを必要とします。

## Human authority / mutation boundary

Human GateのGOは人間の明示入力だけをauthorityとします。

Agent / ReviewerはHuman GOを生成・推定・代理消費しません。

write / merge / publish / print / deploy / promotionは、対応するauthorityが明示されていない限り実行しません。

次の既存正本を読みます。

- `references/accepted/agent-operating-foundation-v1/operating-contract.md`
- `references/accepted/agent-operating-foundation-v1/readback-contract.md`

## Non-goals

```text
F3 / F5の重複Foundation
external Design System implementation
external proprietary visual identity
external token naming scheme
external component composition wholesale
runtime dependency
third-party package installation
application-specific redesign
production deployment
foundations/** mutation
patterns/** mutation
AGENTS.md mutation
CI / workflow mutation
Promotion
```