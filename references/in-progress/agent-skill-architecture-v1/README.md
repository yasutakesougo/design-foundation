# AGENT-SKILL-ARCHITECTURE-V1

このディレクトリは、`design-foundation` の Skill / Reference 構造を整理するための未昇格候補です。

この候補は runtime を変更しません。

`skills/*`、`foundations/*`、`patterns/*`、`prompts/*`、`review/*` は変更対象外です。

## この候補が扱う問い

エージェントが制作を支援するとき、次の3点を一貫して判断できる構造を定義します。

- 人間が明示的に開始する工程はどれか。
- エージェントが必要時に自律利用できる判断規則はどれか。
- 実行手順ではなく参照情報として読む文書はどれか。

Human Gateはこの3分類の外に置きます。

Human GateのGOは、人間の明示入力だけをauthorityとします。

## 常時維持する境界

次の不変条件は、branch-specificなReferenceの奥へ移しません。

- Skill / AgentはHuman GOを生成・推定・代理消費しない。
- Model-invoked disciplineはHuman Gateを遷移させない。
- write / merge / publish / print / deploy / promotionは、対応するauthorityが明示されている場合だけ実行する。
- runtime activationとFoundation / Pattern / Prompt / ReviewへのPromotionは、architecture文書の完成とは別Gateで扱う。

## 文書構成

- `invocation-model.md`: Human-invoked / Model-invoked / Referenceの分類とauthority境界。
- `context-pointer-rules.md`: 必要な文書だけを読むためのpointerとProgressive Disclosureの規則。
- `handoff-rules.md`: 引き継ぎを第二の正本にしないための参照中心ルール。
- `skill-classification-matrix.md`: 現行資産と将来候補を分類するためのマトリクス。

## 外部参考の扱い

設計原則の検討には `mattpocock/skills` をreference-onlyで参照しました。

参照した主な考え方は、invocation ownership、context pointer、progressive disclosure、single source of truth、completion criteria、handoff by reference、tracer-bullet work decompositionです。

外部Skillのファイル、設定、runtime semanticsはローカル正本にしません。

外部Skillのインストール、自動同期、runtime dependency化も行いません。

## Baseline

- Definition: Issue #130 + Correction-1。
- Independent Definition / Scope Review: Issue #131 = PASS。
- Implementation baseline: `main@1abc391be2f526065b7e537901772481fe0595a2`。

## 現在の状態

```text
Definition / Scope Lock = GO / CONSUMED
Implementation Start    = GO / CONSUMED
Architecture candidate  = IMPLEMENTED ON BRANCH
Runtime activation      = HOLD
Human Ready             = HOLD
Human Merge             = HOLD
Promotion               = HOLD
```

この候補をmergeしても、Skill runtimeへの適用やFoundationへのPromotionは自動では行いません。
