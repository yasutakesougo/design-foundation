# Refinement Routing

Refinement Routingは、レビューで見つかったfindingをすべて即時patchへ送らないための分類規則です。

findingの種類ごとに、局所修正、上位Definitionへの復帰、追加readback、HOLDを使い分けます。

## 分類

### Correctness defect

意図された契約に対して実装が誤っている状態です。

確認する問い:

- どの条件で実際に発生するか。
- 現行契約に照らして不正か。
- 局所修正で意味を変えずに解消できるか。

局所修正が妥当でも、対応するHuman Gateとmutation authorityを確認してから変更します。

### Quality defect

既存の良いパターン、境界、言語規約、可読性を不必要に損なっている状態です。

確認する問い:

- 既存のCanonical Contractや確立済みpatternに反しているか。
- 単発か、systemicか。
- 修正がarchitecture判断を要求するか。

systemicな場合は局所patchだけで閉じません。

### Architecture / Definition defect

責務、境界、用語、所有関係、state modelなど、上位の意味づけ自体に問題がある状態です。

このfindingは局所patchより先に上位Definitionへ戻します。

```text
Finding
→ affected semantic levelを特定
→ Definition / architectureを再検討
→ Independent Review
→ Human Gate
→ implementation
```

実装都合だけを理由に契約を後追いで書き換えません。

### Evidence / State uncertainty

現在地、HEAD、Gate、merge state、runtime stateなどを確認できない状態です。

このfindingでは変更を開始しません。

`readback-contract.md` に従って証拠を追加取得し、解消しなければUNKNOWN / HOLDにします。

## Routing matrix

```text
Correctness defect
→ local correction candidate

Quality defect
→ local correction or broader cleanup candidate

Architecture / Definition defect
→ return to semantic / Definition layer

Evidence / State uncertainty
→ readback first; mutation HOLD
```

## Human Gateとの関係

Refinement Routingはwrite authorityではありません。

分類結果が明白でも、未消費のHuman Gateを自動で通過しません。

「修正すべき」というreview findingと「修正を開始してよい」というauthorityを分離します。

## Patchworkを避ける判断

次の状態では、追加patchより上位見直しを優先します。

- 同種の局所修正が繰り返されている。
- 一つの修正が別境界を壊す。
- 複数の名前や責務が同じ概念を重複表現している。
- 新しい例外が既存例外の上に積み上がる。
- acceptance criteriaを満たすためだけの特殊分岐が増える。

## Completion criteria

findingのroutingは、次が明示されたときに完了します。

- finding category
- affected contract / semantic level
- evidence
- proposed route
- required Human Gate
- mutation allowed / HOLD

分類不能なfindingは無理にlocal defectへ落とさずUNKNOWN / HOLDとします。
