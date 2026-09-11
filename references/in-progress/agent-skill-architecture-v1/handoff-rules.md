# Handoff rules

Handoffは、次のAgentや次のsessionが現在地を復元するための案内です。

Handoff自体をIssue、PR、ADR、commit、diffの代わりの正本にしません。

## Handoffに残すもの

Handoffには次の情報を残します。

- 対象プロジェクトまたは機能名。
- 現在のphase。
- 消費済みHuman Gate。
- 未消費Human Gate。
- 現在のbranch、PR、Exact HEADなど、必要な実体参照。
- 次に実行可能な操作。
- 判断に必要な正本への参照。
- unresolved findingがある場合は、その識別子と状態。

既存artifactに本文がある場合は、その内容を再記述しません。

## Handoffに複製しないもの

次の内容は原則として参照だけにします。

- Definition全文。
- Acceptance criteria全文。
- Review全文。
- PR diff全文。
- ADR全文。
- accepted reference本文。
- CI log全文。

再記述が必要な場合は、次の操作に不可欠で、参照だけでは現在地を復元できない部分に限定します。

## Gateの書き方

Gateは消費済みと未消費を分けて記録します。

例:

```text
Human Definition / Scope Lock = GO / CONSUMED
Human Implementation Start    = GO / CONSUMED
Human Ready                   = READY / NOT CONSUMED
Human Merge                   = HOLD
```

前のGateが通っていても、後続Gateを推定しません。

## 次の操作

次の操作は一つの実行可能な単位として書きます。

Human GOが必要な場合は、必要なGate名と対象artifactを明示します。

Agentが自律実行できる作業と、人間の明示操作が必要な作業を混ぜません。

## 参照の優先順位

現在状態を確認するときは、次の順で正本を確認します。

1. 最新のIssue / PR stateとコメント。
2. Exact HEAD / commit / diff。
3. Definition / Review / ADRなどの判断文書。
4. Handoff。

Handoffと上位の正本が矛盾する場合は、上位の正本を採用します。

## 最小テンプレート

```text
Project:
Phase:

Consumed gates:
- ...

Unconsumed gates:
- ...

Current artifacts:
- Issue:
- PR:
- HEAD:

Unresolved:
- ...

Next action:
- ...
```

## Completion criteria

Handoffは、fresh agentが既存artifactを辿り、Human Gateを誤消費せず、次の一手を特定できる状態になったときに完了します。
