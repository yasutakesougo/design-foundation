# Human Gate Model

DELEGATED-EXECUTION-V2 の通常運用で使う Human Gate は次の 3 種類に限定する。

## 標準 Human Gate

### 1. Human Delegation Activation GO

最初に一度だけ、人間が委任可能範囲（IN / OUT）を承認する。

この GO が有効な間は、範囲内の工程遷移に追加の Human GO を要求しない。

### 2. Human Visual Acceptance GO

視覚成果物がある場合のみ。

ルールだけでは決められない視覚的・文脈的判断を人間に残す。

到達時点で、技術的不具合や既知のルール違反を残さない。

詳細は `visual-evidence-path.md`。

### 3. Human Live GO

次の場合だけ、最後に要求する。

```text
本番Deploy
外部公開
実利用者への公開
不可逆な外部変更
Production data mutation
```

内部文書、Foundation / Pattern / Prompt candidate、外部公開を伴わない SVG authority などでは不要。

## 案件別の人間操作回数

```text
内部文書 / Foundation candidate
→ 1回（Delegation Activation）

視覚成果物
→ 2回（+ Visual Acceptance）

視覚成果物 + 本番公開
→ 最大3回（+ Live）
```

## 廃止する通常停止点

委任範囲内では、次を独立 Human Gate として使わない。

```text
Human Definition / Scope Lock GO
Human Implementation Start GO
Human Ready GO
Human Merge GO
```

### Ready / Merge の authority source

```text
Human authority for Ready / Merge
= consumed Human Delegation Activation GO
  whose IN explicitly authorizes Ready / Merge of the activated candidate

Independent Review PASS
= required condition of that grant
≠ Human GO
≠ proxy / inferred Human GO
```

Agent / Skill は Human Ready GO / Human Merge GO を生成・推定・代理消費しない。

## Activation 外

Human Delegation Activation GO が無い workstream では、既存の Operating Foundation / workstream gate vocabulary を変更しない。

## 運用原則

Human approval は工程遷移の許可ではなく、権限境界の許可として扱う。

委任側は、人間が判断する必要がある地点まで停止せずに進める。

人間が見る時点では、作業途中ではなく判断可能な完成候補を提示する。
