# Visual Review V1

Visual Reviewは自動採否ではなく、Human Visual Acceptanceを支える確認工程です。

## Accessibility Baseline Check

Visual Reviewの前に `foundations/accessibility.md` を確認します。

明確なBaseline違反がある場合は、見た目の好みに関係なくCorrectionへ戻します。

## 5項目レビュー

1. 最初に見る場所と情報階層が明確か。
2. 情報量と余白のバランスが適切か。
3. 装飾、イラスト、カード構造に内容上の意味があるか。
4. Accepted Referenceを参照した場合、有効なDesign DNAをFoundationに反しない範囲で継承しているか。
5. Rejected Referenceで確認済みのAnti-patternを、案件固有の理由なく再発していないか。

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
