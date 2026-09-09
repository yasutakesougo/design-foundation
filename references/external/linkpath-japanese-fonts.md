# Linkpath Japanese Fonts — External Reference

## Reference

- Article: `【現役デザイナー厳選】おすすめの日本語フォント15選！フリーフォントサイトも紹介`
- URL: `https://design.linkpath.jp/topic/design/ja_font/`
- Published date shown on source: `2025-11-18`
- Reviewed date: `2026-09-10`
- Role: reference-only

このファイルは、外部記事から採用した再利用可能な考え方と、採用しない境界を記録します。

外部記事そのものをDesign FoundationのAuthorityにはしません。

`foundations/*` とAccessibility Baselineを、このReferenceより優先します。

## 採用する考え方

### 1. フォントは情報の「声」に影響する

同じ文章でも、書体によって受け取られ方が変わるという観点を採用します。

このRepositoryでは、その観点を「雰囲気」だけの選択にせず、文字の話者・役割へ接続します。

### 2. ゴシック体は情報伝達の基盤にしやすい

本文、説明、注意、CTA、安全情報など、明確さと可読性を優先する情報ではゴシック体を基本にします。

既存Foundationの `Noto Sans JP` 第一候補と整合させます。

### 3. 手書き系は人らしさを示す限定用途に使える

手書き系の温度感や人らしさを、人の投稿や人の声を示す短い箇所に限定して利用できます。

指示、安全情報、長文本文には広げません。

### 4. 丸ゴシックの柔らかさは目的がある場合だけ使う

丸ゴシックが柔らかさや親しみやすさを作る性質は参考にします。

ただし、福祉・教育・親しみやすさを理由に紙面や画面全体へ一律適用しません。

## Local interpretation

このReferenceから、次のローカル判断を採用します。

```text
System / instruction / safety / CTA
→ neutral Gothic

Human voice / short submitted words
→ handwritten style may be used in a limited area

AI reply
→ neutral or slightly soft Gothic
```

日本語フォントファミリーは原則2系統までとします。

`Noto Sans JP 80〜90% / 手書き系 10〜20%` は厳密な数値規則ではなく、手書き系を限定使用する感覚を共有するためのヒューリスティックとして扱います。

## 採用しないもの

次は、このReferenceから自動的に採用しません。

- 記事掲載フォント15種類の標準フォント化。
- 紹介されているフォント配布元・サービスの自動導入。
- Web font CDNやruntime dependencyの追加。
- 書体カテゴリーごとの印象説明を固定的な心理効果として扱うこと。
- 丸ゴシックを「福祉向け」の標準書体にすること。
- 手書き系をページ全体の基本書体にすること。
- 第三者の特徴的な表現をそのまま模倣すること。

## Application boundary

このReferenceと今回のTypography改訂は、新規制作または改訂時の判断材料です。

既存のAccepted Reference、in-progress制作物、公開済み成果物へ自動的に遡及適用しません。

個別制作物での書体採否は、その制作物のHuman Visual Acceptanceを別途必要とします。

## Re-review conditions

次の場合は、このReferenceを自動更新せず再レビューします。

- 記事の別の書体や配布サービスを標準採用したくなった場合。
- 有料フォントやライセンス条件を共通基盤へ取り込みたくなった場合。
- Web font配信やfont packageをruntime dependencyとして導入したくなった場合。
- 日本語フォントのFamily数や話者別ルールを変更したくなった場合。
