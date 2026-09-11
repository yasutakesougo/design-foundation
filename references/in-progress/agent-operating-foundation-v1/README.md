# AGENT-OPERATING-FOUNDATION-V1

このディレクトリは、`design-foundation` を担当エージェントが交代しても同じ正本・同じHuman Gate・同じ証拠列から再開できるようにするための未昇格候補です。

このV1はrepository runtimeを変更しません。

Magnitudeの実装をコピーせず、Repository Operating Contract、Applicability、Readback / Reconstruction、Refinement Routing、Observability Boundaryの設計原則だけをローカル向けに縮約します。

## この候補が扱う対象

本候補は次の5概念を分離します。

```text
Operating Contract
= 常時見える不変条件と入口

Canonical Contract
= Foundation / Pattern / Review / Skill / accepted reference等の正本

Applicability Rule
= 変更対象とCanonical Contractの関係

Evidence Chain
= Issue / Gate / PR / commit / CI等から現在地を再構成する証拠列

Refinement Route
= 発見事項をpatch / redesign / HOLDへ振り分ける規則
```

## 文書構成

- `operating-contract.md`: エージェントが最初に確認する不変条件とpointer。
- `applicability-model.md`: 変更対象から読むべき正本へ到達するための候補モデル。
- `readback-contract.md`: 過去会話なしで現在地を再構成するための証拠列。
- `refinement-routing.md`: findingをcorrectness / quality / architecture-definition / evidence-stateへ分類する規則。
- `observability-boundary.md`: repository evidenceとlive runtime evidenceの境界。

## 先行Architectureとの関係

`AGENT-SKILL-ARCHITECTURE-V1` がSkill分類、invocation ownership、progressive disclosure、handoff disciplineを扱います。

本候補はそれらを再定義しません。

Human Gate authorityとmutation boundaryは先行Architectureで定義された規範を優先します。

## 外部参考の扱い

`magnitudedev/magnitude` はreference-onlyです。

Magnitude runtime、ローカルモデル、session event store、OpenTelemetry、CLI、外部Skillは導入しません。

## 現在の状態

```text
Definition / Scope Lock = GO / CONSUMED
Implementation Start    = GO / CONSUMED
First slice             = ADD-ONLY CANDIDATE
README                   = UNCHANGED
Root AGENTS.md           = HOLD
Runtime activation      = HOLD
Human Ready             = HOLD
Human Merge             = HOLD
Promotion               = HOLD
```

この候補をmergeしても、root `AGENTS.md`、applicability automation、telemetry、runtime変更、Promotionは自動では行いません。
