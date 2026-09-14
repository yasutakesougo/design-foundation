# Context model — PERSONAL-DECISION-PRINCIPLES-V1

この文書は、Personal Decision Principles が将来の agent context model においてどこに位置するかを示す candidate 仕様です。

この文書は PERSONAL-DECISION-PRINCIPLES-V1 の候補仕様としてのみ存在します。

accepted authority ではありません。

## この表現が意味しないこと

ここでいう表現は、次を意味しません。

```text
runtime への統合
常時ロード機構の実装
Progressive Disclosure の変更
Skill invocation model の変更
AGENT-SKILL-ARCHITECTURE-V1 candidate の責務変更
root AGENTS.md の変更
accepted operating authority の変更
```

本 V1 ではそれらを行いません。

他 architecture からこの文書を参照する locator / pointer の追加は、本 workstream の対象外です。

将来、Personal Decision Principles を実際に Always Loaded context へ統合する場合は、対象 architecture を正本として、別 Definition / Scope / Independent Review / Human Gate を通します。

## 概念上の順序

Personal Decision Principles の位置だけを、次の順序で示します。

```text
Authority Hierarchy
↓
Safety / Mutation Boundary
↓
Human Gate
↓
Personal Decision Principles
↓
Skill Router / task-specific context
```

この図は PDP がどの層の**下**に置かれるかを示すものです。

新しい runtime hierarchy の実装ではありません。

## 各段の読み方

原則本文は `README.md` です。この文書は P-01 … P-08 を複製しません。

### Authority Hierarchy

法 / 外部規則と、組織権限 / Canonical Source が、Personal Decision Principles より上にあります。

詳細な優先順位の正本は `README.md` の Authority precedence です。

### Safety / Mutation Boundary

write / merge / publish / print / deploy / promotion と Human GO の不変条件です。

この段の規範正本は、この candidate ではありません。

既存正本:

- `references/accepted/agent-operating-foundation-v1/operating-contract.md`
- `references/in-progress/agent-skill-architecture-v1/invocation-model.md` の Always-visible guardrails

図の縦順は、Safety / Mutation Boundary が Explicit Human Gate より上位の **新しい authority** であることを意味しません。

Human GO は mutation の authority のままです。

Safety / Mutation Boundary は、その Human authority と mutation 禁止を常時見えるようにする境界であり、Human Gate を下位に置く規則ではありません。

### Human Gate

明示的な人間入力だけが GO / HOLD の authority です。

Agent / Skill / Personal Decision Principles / Critical Review は Human GO を生成、推定、代理消費しません。

Human Gate 語彙はこの文書で再定義しません。

### Personal Decision Principles

この candidate（`README.md` の P-01 … P-08）です。

上位（法、組織 / Canonical Source、明示的 Human Gate、mutation boundary）に勝りません。

下位の Skill Router / task prompt よりは先に参照する、という位置の候補です。

Always Loaded であることは、この V1 では主張しません。

### Skill Router / task-specific context

作業固有の Skill、手順、task prompt です。

Skill 分類と invocation の正本は AGENT-SKILL-ARCHITECTURE-V1 candidate のままです。

この文書はそれを変更しません。

## 衝突時

```text
Law / org / Canonical Source / explicit Human Gate / mutation boundary
>
Personal Decision Principles
>
Skill Router / task-specific context
```

衝突をこの文書の図だけで解消しません。上位の既存正本を読みます。

## Completion criteria

この文書は、次をすべて満たすときに成立します。

- PDP の概念上の位置が図として示されている
- 表現が runtime / Always Loaded 実装と区別されている
- 既存 architecture への pointer 追加を要求していない
- Human Gate / mutation authority を再定義していない
- 原則本文の正本が `README.md` のままである
