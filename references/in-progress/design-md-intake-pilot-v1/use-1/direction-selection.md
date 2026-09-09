# Direction Comparison / Human Selection Handoff

## Route A

Source:

`Human brief + Foundation only`

Likely characteristics:

- centered title
- symmetric vertical stack
- three equal-size example blocks
- evenly distributed spacing
- minimal decoration
- no illustration

Strengths:

- stable
- easy to scan
- low visual risk

Risks:

- `少し人の手触り` の解釈が弱い
- `小綺麗にまとめすぎない` の具体化が制作担当ごとに変わる
- card / spacing / alignmentの選択が未固定

## Route B

Source:

`Human brief + Foundation + normalized candidate + conflict review`

Likely characteristics:

- left-aligned title
- warm off-white + deep green + muted yellow
- examplesは完全同型のUIカードにしない
- semantic spacing levels
- subtle paper-like offsets
- illustrationは必要なら成人1scene以下

Strengths:

- Human intentの抽象語が観察可能なルールへ変換されている
- alignment / spacing / repetition / illustration roleの未指定範囲が狭い
- Web UI driftを具体的に抑制できる

Risks:

- project-specific rulesをFoundationへ誤昇格させない管理が必要
- exact color valuesへ過度に依存しないこと

## Recommendation for Pilot production

**Route B を比較用production draftとして採用することを推奨します。**

理由は、Human briefの意味を変えずに、制作担当が独自判断する箇所を減らしているためです。

## Human Gate state

- Recommendation: `Route B`
- Human Direction Selection: **NOT CONSUMED**
- Pilot comparison draft production: **allowed as experiment evidence under Issue #57**
- Human Visual Acceptance: **NOT REQUESTED**
- Print / Publish: **NOT AUTHORIZED**

このファイルはHuman Direction Selection GOを代行しません。
