# Visual Review V1

Visual Reviewは自動採否ではなく、Human Visual Acceptanceを支える確認工程です。

## Accessibility Baseline Check

Visual Reviewの前に `foundations/accessibility.md` を確認します。

明確なBaseline違反がある場合は、見た目の好みに関係なくCorrectionへ戻します。

## 5項目レビュー

1. 最初に見る場所が明確か。
2. 情報を詰め込みすぎていないか。
3. 余白が十分あるか。
4. イラストや装飾が主役を奪っていないか。
5. Accepted Referenceと同じ判断方向にあり、案件固有の理由なく逸脱していないか。

## 判定

- `PASS`: Human Visual Acceptanceへ進める。
- `PASS WITH CORRECTION`: 小さな修正後に再確認する。
- `REJECT`: 構成または方向性から見直す。

## コメントの書き方

最初に判定を書きます。

次に、気になった箇所を具体的に示します。

修正が必要な場合は、何をどう変えるかを最小単位で示します。

「なんとなく」「もっとおしゃれに」だけで終わらせません。

## Human Gate

Visual ReviewのPASSは最終採用を意味しません。

最終採否は `Human Visual Acceptance` で決めます。
