# Typography Generation Prompt V1

## 使う場面

AIやエージェントでチラシ、Web、UI、広報物、文書などの文字組みを生成するときに使います。

## Prompt

```text
対象制作物のTypographyを設計してください。

最初に `foundations/typography.md` を正本として読み、その役割・可読性・書体数・適用境界を優先してください。

文字を雰囲気語だけで決めず、最初に各テキストの役割を整理してください。

各役割について、必要に応じて次を明示してください。

- role
- family / fallback class
- weight
- relative size / hierarchy
- tracking / letter spacing
- leading / line-height
- alignment
- maximum lines / wrapping behavior
- reference source role
- prohibited substitutions / decorative drift

日本語、Latin、混在テキストを同じspacing recipeで処理しないでください。

日本語では、文字の分離と可読性を優先してください。

Latinのdisplay typographyで成立する強いnegative trackingを、日本語の既定値にしないでください。

行数を合わせるためだけに日本語を圧縮しないでください。

非常に詰めたleadingを全体の既定値にしないでください。

本文、説明、注意書き、CTA、安全情報では、コンパクトさより可読性を優先してください。

本文、説明、注意書き、CTA、安全情報へ装飾的な書体や強いキャラクターを流用しないでください。

参考フォント、フォントサンプル、参考画像、その他の生成入力を使う場合、それらは生成用Referenceとして扱ってください。

生成用Referenceを、repository font authority、runtime dependency、license authority、accepted outputとして扱わないでください。

Referenceに近い見た目が得られても、正確な書体identityが独立に確認できない限り、同一書体だと断定しないでください。

指定した正確な書体が利用できない場合は、利用不可または代替を明示し、代替後の見た目をレビュー対象にしてください。

特定provider、外部service、外部font listを必須条件にしないでください。

生成後は、少なくとも次を確認してください。

- glyph quality
- line breaks
- tracking
- leading
- hierarchy
- contrast
- readability
- role consistency
- unexpected decorative drift

最後に、次の形式で結果を返してください。

1. テキスト役割一覧
2. 役割別Typography指定
3. 日本語 / Latin / mixed-scriptの扱い
4. Referenceとfont identityの扱い
5. 生成結果の確認事項
6. 代替・未確認事項
7. Human Reviewで見る点

Promptへの適合だけでHuman Visual Acceptanceを成立させないでください。

Human Output GOを生成・推定・代理消費しないでください。
```
