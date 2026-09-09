# CARD-WALL-V1 — DESIGN.md

Status: **IN-PROGRESS DESIGN AUTHORITY / PR #24**

Date: 2026-09-09

この文書は、`CARD-WALL-V1` の現在のHuman-selected visual directionを、再現可能なデザイン判断として固定するための仕様です。

本文・補助コピー・QR・Human Gateの正本は、それぞれ既存のauthority文書を優先します。

この文書はコピーauthorityを上書きしません。

## 1. Concept & Rationale

「日常を、言葉に。」を核とした、職員向けの参加型ミニ実験を知らせるA4縦ポスターです。

目的は、気づきの大切さを啓発することではありません。

日常の中で少し気になったことを、完成した意見にする前に、30秒程度でひとこと置いてみられる入口をつくることを目的とします。

視線の流れは、次の順序を基本とします。

```text
タイトル
→ 書けるひとことの例
→ ひとこと返し
→ CTA / QR
→ 安心情報・運用上の注意
```

「ひとこと循環」は正式導入前の「小さな試行」です。

そのため、制度、研修、啓発キャンペーンのような公式感は避けます。

全体は、生成りの紙面、深緑、淡い緑、黄色を基調とします。

破いたメモ、テープ、クリップ、わずかな配置のズレなどを使い、整いすぎない紙ものの手触りを加えます。

ただし、手作り感を目的に装飾を増やしません。

目標とする印象は、「気づきを大切にしましょう」ではなく、「このくらいの一言なら、自分も試せそう」です。

## 2. Design Principles

- 整っているが、無機質にはしない。
- 温かいが、幼くはしない。
- 静かだが、参加の入口は明確にする。
- 人の手触りは残すが、雑にはしない。
- 啓発物ではなく、小さな参加募集として設計する。
- Web UIのような完全な均一性を避ける。
- AIっぽさを消すために装飾を増やさない。
- `controlled imperfection` を使い、読みやすさを壊さない範囲で2〜5%程度の不均一さを許容する。

```text
Clean but not sterile.
Warm but not childish.
Quiet but inviting.
Human but not messy.
Participation notice, not educational campaign.
```

## 3. Typography

見出しには、親しみがありながらA4掲示で十分な視認性を持つ丸みのある書体を使用します。

本文は可読性を最優先し、`Noto Sans JP` を使用します。

手作り感はフォント自体を崩すことで作らず、黄色の筆跡、紙素材、微妙な位置差などで表現します。

| 用途 | フォントファミリー | ウェイト | CSS変数名 |
| --- | --- | --- | --- |
| 主要見出し | Zen Maru Gothic | Bold | `--font-family-heading` |
| 本文・安全情報 | Noto Sans JP | Regular / Medium | `--font-family-body` |

```css
:root {
  --font-family-heading: 'Zen Maru Gothic', sans-serif;
  --font-family-body: 'Noto Sans JP', sans-serif;

  --font-size-xxl: 3.5rem;
  --font-size-xl: 2.25rem;
  --font-size-l: 1.5rem;
  --font-size-m: 1rem;
  --font-size-s: 0.875rem;

  --line-height-heading: 1.3;
  --line-height-body: 1.7;

  --letter-spacing-heading: 0.05em;
  --letter-spacing-body: 0.02em;
}
```

フォントサイズの数値だけを最終authorityにはしません。

A4実寸での視認性を最終判断に使います。

## 4. Color System

色名より、Human-selected visual directionとの整合を優先します。

主色は藍色ではなく深緑です。

淡い緑、生成り、黄色、少量のピーチ・ベージュを補助色として使用します。

```css
:root {
  --color-primary: #164A42;
  --color-primary-soft: #5E8C78;

  --color-background: #F6F2E8;
  --color-surface-mint: #DDEDE2;
  --color-paper-cream: #F4EBDD;

  --color-accent-yellow: #F2C94C;
  --color-accent-peach: #D7A38C;

  --color-line: #174A42;

  --color-skin-base: #F1D2B6;
  --color-skin-shadow: #E5BEA2;
}
```

`--color-primary` と `--color-background` のコントラスト比は約 `8.98:1` です。

`--color-primary-soft` と `--color-background` のコントラスト比は約 `3.42:1` です。

`--color-primary-soft` は通常サイズの重要本文には使いません。

黄色やピーチは文字色ではなく、強調面、筆跡、補助装飾として使用します。

## 5. CTA

下部CTA領域を、ポスター上の行動の主役とします。

QRコード単体を主役にはしません。

CTAは、active production copy authorityで許可された文言とQRを組み合わせて成立させます。

QRコードは十分なquiet zoneを確保します。

QRコード自体にはtexture、opacity、filter、decorative overlayを重ねません。

CTAはWeb UIのボタン群には見せず、紙面上の参加案内として表現します。

## 6. Paper & Object System

「ひとこと」の例は、同一のカードUIではなく、異なる紙メモとして表現します。

代表例は次のとおりです。

- 破いた生成り紙
- 薄い方眼紙
- テープ留めした紙

紙ごとに形、角度、位置、影をわずかに変えます。

完全に均一なカード列にはしません。

### 6.1 Paper

- torn edgeは完全な周期パターンにしない。
- 紙にはごく弱い固定grainを使用してよい。
- 紙ごとにごく小さい影差を持たせる。
- 影はWeb UIのbox-shadowのように強くしない。
- 文字が紙端へ接近しすぎないよう、内側余白を優先する。

### 6.2 Tape

- 単色矩形だけで表現しない。
- ごく弱い透過を持たせる。
- テープごとに角度を変える。
- 紙との接地感を優先する。
- 素材感を出すために装飾を増やしすぎない。

### 6.3 Clip

- 通常のペーパークリップとして認識できる単純な形状にする。
- 紙の上辺に部分的に重ね、実際に紙を留めているように見せる。
- 紙から浮いた装飾アイコンのように見せない。
- 金属表現は最小限にする。
- 紙の縮尺に対してクリップを大きくしすぎない。

## 7. Character System

人物はポスターの主役ではありません。

「誰かが実際に少し試している」という人の気配を補助するために使用します。

方向性は、adult editorial flat illustrationとします。

### 7.1 Basic

- 成人として自然な頭身にする。
- マスコット化しない。
- アニメ調、3D、写真風にはしない。
- pure blackではなく深緑系の線を使う。
- 線幅を完全均一にしない。
- 強い陰影や光沢を使わない。
- 「福祉らしさ」を人物記号で表現しない。
- 人物は説明のための模範例ではなく、参加している人の気配として扱う。

### 7.2 Skin

全人物で共通の肌色tokenを使用します。

```css
:root {
  --color-skin-base: #F1D2B6;
  --color-skin-shadow: #E5BEA2;
}
```

顔、耳、首、手には同じbase skin colorを使用します。

上部人物とCTA人物で別の肌色を使いません。

背景の緑に引っ張られて灰色や緑に見える表現を避けます。

### 7.3 Face

- 目、鼻、口は最小限にする。
- 全員を同じ笑顔にしない。
- 過剰な喜びや驚きを描かない。
- 「日常の中で少し考えている」程度の表情を基本とする。
- 完全な左右対称を避ける。

### 7.4 Consistency

人物を同じ顔にする必要はありません。

ただし、次の作画文法は統一します。

- 肌色
- 線の色
- 線幅
- 顔の簡略化レベル
- 頭身
- 手の描き方
- 色温度

目標は「同じ人物」ではなく、「同じイラストレーターのシリーズ」です。

## 8. Anti-AI Visual Rules

次の表現を避けます。

- 全人物が同じ微笑み
- 同じ顔パーツの反復
- 過度に滑らかなベクター曲線
- すべてが完全に中央揃え
- 同型カードの連続
- 黄色い感情線の過剰反復
- 植物、テープ、付箋などの目的のない装飾追加
- stock illustration的な説明ポーズ
- 「人間味」を出すためだけの過剰な手描き加工

AIっぽさを減らす場合は、要素を追加するより、規則性を少し崩します。

## 9. Spacing & Controlled Imperfection

A4縦の限られたスペースでは、情報階層を優先して余白を設計します。

完全な機械整列は避けますが、読みやすさを崩すランダム配置もしません。

```css
:root {
  --spacing-xxl: 4rem;
  --spacing-xl: 2.5rem;
  --spacing-l: 1.5rem;
  --spacing-m: 1rem;
  --spacing-s: 0.5rem;
  --spacing-xs: 0.25rem;

  --border-radius-soft: 0.5rem;
  --border-width-thin: 1px;

  --shadow-light: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

`controlled imperfection` は固定値で再現可能にします。

runtime randomや実行ごとに変わるnoiseは使用しません。

## 10. Accessibility & Print Rules

色のみに意味を持たせません。

通常サイズの重要本文には、十分なコントラストを持つ`--color-primary`を使用します。

注意喚起の補助色だけで重要情報を表現しません。

A4普通紙で実寸確認します。

中央例文は50〜80cm程度から読めることを確認します。

安全上必要な注意文はA4実寸で判読できることを確認します。

PDFでは日本語フォント埋込を確認します。

QRコードはPDFレンダー後にもdecodeできることを確認します。

QRコードにはキャプションを併記します。

## 11. Authority Boundaries

この文書はvisual design authorityです。

本文とactive production subsetは、`content.md` と `production-microcopy.md` の現在のauthorityを優先します。

QR destinationは既存のauthoritative QR assetを優先します。

Human Visual Acceptance、Physical A4、real-device QR、Merge、Print、Post、DeployのGateをこの文書だけで通過させません。

Human-selected referenceとdeterministic reproductionに差がある場合は、差を隠さず具体的に記録します。
