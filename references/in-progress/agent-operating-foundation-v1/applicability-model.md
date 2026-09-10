# Applicability Model

Applicability Ruleは、変更対象から読むべきCanonical Contractを特定するための関係です。

V1では実装方式を固定しません。

## 目的

変更するファイルやartifactに対して、関連するFoundation、Pattern、Review、Skill、Referenceを漏れなく確認できる状態を目指します。

単なるファイル一覧ではなく、どの変更にどの正本が適用されるかを示します。

## 比較する候補

### A. Front matter

各Canonical Contractに対象path patternを持たせます。

利点:

- 正本と適用範囲を同じ場所で保守できる。
- changed pathから機械的に逆引きしやすい。

懸念:

- 既存文書へのmetadata追加が広範囲になる。
- path移動時に更新漏れが起こり得る。

### B. Central applicability matrix

一つのmatrixで変更領域とCanonical Contractの対応を管理します。

利点:

- 導入範囲を限定しやすい。
- 既存文書を直接変更せず試行できる。

懸念:

- matrixが第二の正本になり得る。
- 文書追加時の同期忘れが起こり得る。

### C. Lightweight manifest

機械可読の軽量manifestに対応関係だけを持ちます。

利点:

- helperやCIへ発展させやすい。
- 表現を小さく保てる。

懸念:

- 人間向け文書との二重管理になり得る。
- automation導入前には保守価値が低い可能性がある。

## V1の判断基準

方式選択では次を評価します。

```text
coverage
= 必要な正本を漏らさないか

maintenance cost
= path移動・文書追加時の更新負担が過大でないか

source-of-truth risk
= 第二の正本を作らないか

refactor tolerance
= 通常の構造変更で頻繁に壊れないか

human readability
= agentだけでなく人間も適用理由を確認できるか
```

## Fail-closed rule

適用対象が不明な場合は「該当なし」としません。

```text
Applicability = UNKNOWN
Action        = HOLD or broaden readback
```

間接的なarchitecture影響が疑われる場合は、path matchだけを根拠に対象外と断定しません。

## First sliceで行わないこと

- front matter追加
- central matrixの正本化
- manifest作成
- helper CLI実装
- GitHub Actions enforcement
- existing canonical docsの変更

## Completion criteria

方式候補を比較するときは、少なくとも次を確認します。

- 代表的な変更pathから必要な正本へ到達できる。
- 1つの変更に複数のCanonical Contractが適用される場合を扱える。
- path移動時の更新責任が定義できる。
- UNKNOWN時にfail-openしない。
- metadata保守が実運用負担を超えない。
