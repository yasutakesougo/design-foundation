# SVG-AUTHORING-V1

## Status

```text
Definition / Scope          = LOCKED / CONSUMED
Fresh Definition Review     = PASS / CONSUMED
Human Implementation Start  = GO / CONSUMED
Implementation              = IN PROGRESS
Human Ready                 = HOLD
Pilot execution             = HOLD
Merge / Promotion           = HOLD
```

## 目的

このPilotは、AIエージェントがSVGを意味、形、関係、編集可能性を持つ構造として扱えるかを確認します。

特定の人物線画Styleや特定のvectorization backendを共通標準へ昇格させることは目的にしません。

## Authority

Canonical DefinitionはIssue #104です。

Fresh Definition / Scope ReviewはIssue #105です。

実装baseは次です。

```text
main@b267fa765a355ef279822afa508c46abd6519725
```

実装branchは次です。

```text
work/svg-authoring-v1
```

## 実装物

```text
skills/svg-authoring/SKILL.md
review/svg-authoring.md
references/in-progress/svg-authoring-v1/README.md
references/in-progress/svg-authoring-v1/evaluation-cases.md
```

README.md本体の変更は、初回実装では不要と判断して見送ります。

## Skillの役割

`skills/svg-authoring/SKILL.md` は、SVGの新規作成、局所修正、再構成、レビューで使う作業手順を定義します。

案件固有Style Contractを先に読みます。

意味、主要形状、関係、編集可能性をpath cleanlinessより上位に置きます。

局所問題ではminimum-changeを既定にします。

Human Gateを自動消費しません。

## Reviewの役割

`review/svg-authoring.md` は、完成候補または修正差分を段階的に確認します。

```text
G1 Parse / Render
G2 Project Style Contract
G3 Structural Editability
G4 Geometry / Relationship
G5 Multi-scale Visual Review
G6 Semantic Retention
G7 Human Visual Acceptance when required
```

## 既存レーンとの関係

次の既存レーンは参照evidenceです。

```text
HITOKOTO-PERSON-LINE-STYLE-V1
SEMANTIC-VECTORIZATION-PILOT-V1
IMAGE-FIRST-SEMANTIC-REDRAW-V1
Curve Reconstruction corrections
```

このPilotから既存レーンを変更しません。

人物線画の `viewBox=0 0 512 512`、`stroke-width=8`、64px確認などは共通固定値へ昇格させません。

## 非対象

```text
existing SVG asset mutation
existing PR mutation
production asset replacement
vectorization backend selection
foundations/* mutation
patterns/* mutation
prompts/* mutation
CI mutation
repository-wide dependency changes
runtime application changes
Canva / Figma mutation
Deploy / Print / Publish
Human Visual Acceptance automation
Merge / Promotion
```

## 次のGate

実装後はFresh Implementation / Scope Reviewを行います。

そのReviewがPASSしてもHuman Readyは自動消費しません。
