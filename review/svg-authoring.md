# SVG Authoring Review

## 目的

SVGの完成候補または修正差分を、validity、style、structure、geometry、visual、semanticの観点で分けて確認します。

自動検査だけでHuman Visual Acceptanceを代替しません。

## G1 Parse / Render Validity

次を確認します。

- XMLとして解釈できる。
- `viewBox`が案件の契約と一致する。
- 必要なrendererで表示できる。
- 意図しない欠落やclippingがない。

G1がFAILの場合は後続評価へ進みません。

## G2 Project Style Contract

次を案件固有の契約と照合します。

- stroke / fill。
- stroke-width。
- linecap / linejoin。
- color authority。
- font。
- corner / terminal treatment。
- transform / mask / filter等の許容範囲。

人物線画など別案件の固定値を流用しません。

## G3 Structural Editability

次を確認します。

- 意味のある部品を必要な範囲で個別修正できる。
- 一つの巨大pathへ不必要に集約されていない。
- micro-fragmentationが過剰でない。
- anonymous groupやtransform chainが編集を妨げていない。
- meaningful groupingが保たれている。

path数やnode数は補助指標です。

少ないこと自体をPASS条件にしません。

## G4 Geometry / Relationship

次を確認します。

- 主要シルエットが意図通りである。
- object間の距離と接触関係が意図通りである。
- clipping、意図しないoverlap、隙間がない。
- protected endpointやjunctionが維持されている。
- 修正対象外のgeometryが不必要に変わっていない。

意味を持つ関係が失われた場合はFAILです。

## G5 Multi-scale Visual Review

実使用サイズで確認します。

小サイズ利用がある場合は、そのサイズで主要な意味が残るか確認します。

64pxは必要な案件だけに適用します。

曲線品質を確認する場合は、必要に応じて200〜400%程度でも確認します。

曲線では次を分けて見ます。

```text
kink
micro-wave
perceivable segment handoff
over-regularization
source / intended contour character
```

## G6 Semantic / Relationship Retention

次を確認します。

- SVGが伝えるべき意味が維持されている。
- gestureや方向性が必要な場合は判別できる。
- hand ↔ face、pen ↔ paper、connector ↔ nodeなど、案件固有の関係が維持されている。
- 細部を増やすことで意味を補っていない。
- filenameや説明ラベルを見ないと意味が分からない状態になっていない。

semantic failureは、見た目の類似度が高くても全体FAILです。

## G7 Human Visual Acceptance

Human Visual Acceptanceが必要な案件では、人の目による採否を別Gateとして残します。

自動validator、SSIM、path count、曲率指標などは補助証拠です。

数値改善だけでHuman Visual Acceptanceを消費しません。

## Targeted Edit Review

既存SVGの局所修正では、before / afterの差分を確認します。

最低限次を記録します。

```text
Intended meaning
Observed failure
Changed parts
Protected parts
Unintended change = NONE / FOUND
```

問題と無関係なpathが広く変わっている場合はscope driftとして扱います。

## Verdict template

```text
G1 Parse / Render              = PASS / FAIL
G2 Project Style Contract      = PASS / FAIL
G3 Structural Editability      = PASS / HOLD / FAIL
G4 Geometry / Relationship     = PASS / HOLD / FAIL
G5 Multi-scale Visual Review   = PASS / HOLD / FAIL
G6 Semantic Retention          = PASS / HOLD / FAIL
G7 Human Visual Acceptance     = PASS / HOLD / NOT REQUIRED
Scope drift                    = NONE / FOUND
Required correction            = NONE / <target>
Overall                         = PASS / HOLD / FAIL
```
