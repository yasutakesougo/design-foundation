# AGENT-OPERATING-FOUNDATION-V1

このディレクトリは、`design-foundation` を担当エージェントが交代しても同じ正本・同じHuman Gate・同じ証拠列から再開できるようにするためのRepository Operating Foundationです。

このV1はrepository runtimeを変更しません。

Magnitudeの実装をコピーせず、Repository Operating Contract、Applicability、Readback / Reconstruction、Refinement Routing、Observability Boundaryの設計原則だけをローカル向けに縮約します。

## Authority

このパスは、Promotion Definition #162、Independent Promotion Definition Review #163、明示的Human Promotion GOを経てmainへmergeされた時点でaccepted authorityとして扱います。

Promotion候補branchに存在するだけではaccepted authorityになりません。

root `AGENTS.md`、runtime activation、applicability automation、telemetryは別Definition / Human Gateです。

## このauthorityが扱う対象

このauthorityは次の5概念を分離します。

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

このauthorityはそれらを再定義しません。

Human Gate authorityとmutation boundaryは先行Architectureで定義された規範を優先します。

## 外部参考の扱い

`magnitudedev/magnitude` はreference-onlyです。

Magnitude runtime、ローカルモデル、session event store、OpenTelemetry、CLI、外部Skillは導入しません。

## Validation evidence

```text
Implementation PR          = #137 / MERGED
Actual Handover Pilot      = COMPLETED
Pilot Evidence Re-Review   = #161 / PASS
Human Issue Close          = GO / CONSUMED / COMPLETE
Promotion Definition       = #162
Promotion Definition Review= #163 / PASS
```

## Boundary after Promotion

```text
Authority class        = references/accepted/
Root AGENTS.md         = HOLD
Runtime activation     = HOLD
Applicability automation = HOLD
Telemetry / tracing    = HOLD
```

accepted authorityへの昇格は、runtime実行やroot `AGENTS.md`導入を自動承認しません。
