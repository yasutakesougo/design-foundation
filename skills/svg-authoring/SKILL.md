---
name: svg-authoring
description: SVGを新規作成、部分修正、再構成、レビューするときに、意味、形、関係、編集可能性、曲線品質を保ちながら作業するためのSkill。
---

# SVG Authoring

## いつ使うか

SVGを新規作成するときに使います。

既存SVGの一部だけを修正するときに使います。

ラスタや別形式からSVGへ再構成するときに使います。

SVGを構造、見た目、意味の観点でレビューするときにも使います。

## 1. 既存の契約を先に読む

案件に既存SVG、Style Guide、Foundation、Pattern、accepted assetがある場合は先に確認します。

`viewBox`、色、線幅、fill、角丸、font、path数などを、このSkillの固定値として扱いません。

案件固有の契約がある場合は、その契約を優先します。

## 2. SVGを意味構造として扱う

SVGを座標列だけとして扱いません。

次の順で判断します。

```text
semantic readability
→ silhouette / major shape
→ major gesture
→ spatial relationships
→ project-specific visual consistency
→ structural editability
→ path cleanliness / compactness
```

下位項目を改善するために上位項目を悪化させません。

## 3. 作業モードを決める

新規作成では、意味と主要形状を先に決めます。

```text
intent
→ semantic parts
→ major silhouette / gesture
→ object relationships
→ SVG groups / paths
→ style application
→ render review
```

既存SVGの修正では、局所修正を既定にします。

```text
visual / semantic failure
→ responsible geometry
→ minimum affected parts
→ protected parts
→ bounded edit
→ before / after review
```

再構成では、pixel similarityだけで完成判定しません。

```text
source evidence
→ topology / semantic anchors
→ path reconstruction
→ normalization
→ structural review
→ visual review
→ semantic review
```

## 4. geometry変更前に修正範囲を固定する

既存SVGを変更する前に、最低限次を明確にします。

```text
Intended meaning
Current visual / semantic failure
Geometry responsible for the failure
Minimum parts / groups requiring modification
Elements / relationships that must remain unchanged
```

この情報を特定できない場合は、座標の試行錯誤から始めません。

全面再構成が必要な場合は、局所修正で解決できない理由を記録します。

## 5. 意味のある構造だけを残す

意味単位で分ける価値がある場合は、編集可能な構造を残します。

例を示します。

```text
head
face
arm
hand
paper
pen
label
icon
connector
```

意味のある `<g>`、`id`、`data-part` は使用できます。

単純なSVGへ機械的に大量のgroupを追加しません。

Exporter由来の匿名groupや不要なtransformは、見た目と意味を変えずに除去できる場合だけ整理します。

## 6. 意味を持つ関係を保護する

object間の意味を持つ関係は、geometry optimizationより上位に置きます。

例を示します。

```text
hand ↔ face
pen ↔ paper
arrow ↔ target
label ↔ referenced object
connector ↔ connected nodes
icon ↔ bounding shape
```

曲線を滑らかにするために、接触点、端点、junction、意味上必要な距離関係を動かしません。

## 7. 曲線品質を一つの指標へまとめない

長い有機的輪郭では、必要に応じて滑らかな曲線を使います。

短い意図的な直線まで無理にBézier化しません。

曲線品質では次を分離して確認します。

```text
kink
micro-wave
perceivable segment handoff
over-regularization
source / intended contour character
```

数値指標は補助証拠として扱います。

数値が改善しても、Human Reviewで不自然に見える場合はPASSにしません。

## 8. path数や制御点数を自己目的化しない

path数や制御点数が少ないことだけを品質とみなしません。

一つの巨大pathへまとめて編集性や意味分離を失う場合は失敗です。

見た目の誤差を減らすためにmicro-fragmentationを増やし、修正不能になる場合も失敗です。

必要な意味分離と編集可能性を残します。

## 9. 実使用条件に合わせて確認する

最低限、parseとrenderの成立を確認します。

その後、案件のStyle Contract、構造、clipping、overlap、見た目、意味を確認します。

小サイズで使う場合は、小サイズで主要な意味が残るか確認します。

64pxは案件が必要とする場合だけ使います。

曲線修正では、必要に応じて200〜400%程度の拡大表示でkinkやsegment handoffを確認します。

## 10. 完成判定を段階化する

```text
G1 Parse / render validity
↓
G2 Project style contract
↓
G3 Structural editability
↓
G4 Geometry / clipping / overlap
↓
G5 Multi-scale visual review
↓
G6 Semantic / relationship retention
↓
G7 Human Visual Acceptance when required
```

自動検査でHuman Visual Acceptanceを代替しません。

## 失敗時の扱い

SVGがvalidでも、意味が弱くなった場合は完成扱いにしません。

主要シルエットが意図せず変わった場合は完成扱いにしません。

意味を持つ関係や接触点を失った場合は完成扱いにしません。

編集困難なfragmentationや機械的な過剰平滑化が発生した場合は完成扱いにしません。

失敗した候補では、可能な範囲で次に修正すべき対象を明示します。

## Human Gate

このSkillは既存のHuman Gateを自動で消費しません。

既存SVGやproduction assetを無断で置き換えません。

Merge、Promotion、Deploy、Print、Publishは別の承認として扱います。
