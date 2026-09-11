# Operating Contract

Operating Contractは、エージェントがrepository作業を始めるときに必ず到達できる不変条件と入口だけを持ちます。

詳細な制作規則やレビュー本文を複製しません。

## 常時確認する不変条件

- Human GateのGOは人間の明示入力だけをauthorityとする。
- Agent / SkillはHuman GOを生成・推定・代理消費しない。
- write / merge / publish / print / deploy / promotionは、対応するauthorityが明示されていない限り実行しない。
- `references/in-progress/` は未昇格候補であり、accepted authorityとして扱わない。
- 証拠不足の状態をPASSへ補完しない。
- live runtime evidenceが必要な状態をrepository evidenceだけで断定しない。

## Canonical Contractへの入口

対象作業に応じて、既存の正本へpointerします。

候補となる正本は次です。

- `foundations/*`
- `patterns/*`
- `review/*`
- `skills/*`
- `prompts/*`
- `references/accepted/*`
- locked Definition / Review / Human Gate evidence

同じ規則をOperating Contractへ全文転載しません。

## 作業開始時の最小readback

作業開始時は、対象workstreamについて次を確認します。

```text
1. canonical Definition
2. latest independent review
3. consumed Human Gates
4. next unconsumed Human Gate
5. implementation PR / exact HEAD if present
6. merge state
7. applicable canonical contracts
8. unresolved findings / evidence gaps
9. permitted next action
```

確認不能な項目はUNKNOWNとして残します。

## 変更前の判断

変更対象が決まったら、`applicability-model.md` に従って読むべきCanonical Contractを特定します。

findingが出た場合は、`refinement-routing.md` に従って局所patch、上位Definitionへの復帰、またはHOLDへ振り分けます。

runtime状態を扱う場合は、`observability-boundary.md` に従って必要な証拠種類を確認します。

## 非対象

この文書は次を承認しません。

- root `AGENTS.md` の導入
- automated applicability enforcement
- CI変更
- telemetry導入
- runtime mutation
- Human Gate遷移
- Promotion

## Completion criteria

Operating Contract候補は、次をすべて満たすときに成立します。

- Human authorityが常時見える。
- mutation boundaryが常時見える。
- 詳細正本を複製していない。
- applicable contract、readback、refinement、observabilityの各文書へ到達できる。
- UNKNOWNをPASSへ変換する規則がない。
