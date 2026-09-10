# SVG-AUTHORING-V1 Evaluation Cases

## 目的

SkillがSVG編集を安定させるかを、意味、曲線、構造の3種類に分けて確認します。

既存Human-accepted assetは直接変更しません。

必要な場合はimmutable fixtureまたはcopyを使います。

## Case A — Semantic local edit

### 問い

局所的な意味の失敗を、無関係な部分へscope driftせず修正できるかを確認します。

### 例

```text
writing gesture
thinking gesture
hand ↔ object relation
arrow ↔ target relation
```

### 事前brief

```text
Intended meaning
Current semantic failure
Responsible geometry
Minimum affected parts
Protected parts
```

### PASS条件

- intended meaningが改善する。
- protected partsが維持される。
- unrelated geometryの変更が最小である。
- path cleanlinessのために意味を損なわない。
- before / afterで変更理由を説明できる。

### FAIL例

- 手の修正だけでよいのに髪、服、顔まで再生成する。
- object contactが消える。
- small-useで主要gestureが消える。

## Case B — Curve local edit

### 問い

長い輪郭の不自然さを、意味や形を崩さず局所修正できるかを確認します。

### 対象となる失敗

```text
kink
micro-wave
perceivable segment handoff
over-regularization
```

### 事前brief

```text
Target contour
Observed curve defect
Protected endpoints / junctions
Protected object relationships
Required source / intended contour character
```

### PASS条件

- kinkやhandoffが改善する。
- endpointとjunctionが維持される。
- major silhouetteが意図せず変わらない。
- 機械的な円弧へ過剰平滑化しない。
- 必要な拡大率と実使用サイズの両方で確認できる。

### FAIL例

- numerical smoothnessだけを改善して見た目が不自然になる。
- long contour全体を不要に再構成する。
- control pointを増やしすぎて編集困難になる。

## Case C — Structural edit

### 問い

見た目と意味を変えず、編集を妨げる構造だけを整理できるかを確認します。

### 対象となる構造

```text
anonymous groups
unnecessary transform chains
micro-fragmented paths
unnecessary exporter metadata
meaningful group boundaries
```

### PASS条件

- render結果が意図せず変化しない。
- semantic groupingが維持される。
- 編集対象を見つけやすくなる。
- path数削減を自己目的化しない。
- giant path collapseを起こさない。

### FAIL例

- semantic partを一つの巨大pathへ統合する。
- group削除でstyle inheritanceが壊れる。
- transform flatteningでgeometryがずれる。

## 共通評価項目

3ケースすべてで次を記録します。

```text
scope containment
protected-part retention
semantic retention
editability
review evidence clarity
```

判定は次を使います。

```text
PASS
HOLD
FAIL
```

一つの総合点へまとめません。

## Pilot結果の使い方

3ケースが成功しても、FoundationやPatternへ自動昇格させません。

Skillの修正が必要な場合は、失敗した判断手順を特定してから次版を検討します。

MergeやPromotionは別Human Gateとします。
