# CARD-WALL-V1 — V3 DESIGN.md

Status: **V3 HUMAN-LOCKED / IMPLEMENTATION START GO / CONSUMED / PR #24**

Date: 2026-09-09

この文書は、V3「入口特化ポスター」のvisual design authorityです。

本文・QR・Human Gateは、それぞれ`content.md`、`production-microcopy.md`、Issue #59のHuman-locked authorityを優先します。

## 1. Purpose

V3は、A「ひとこと循環」の**入口だけを伝えるA4縦ポスター**です。

目的は、活動の仕組みを詳しく説明することではありません。

職員が「この程度の小さな気づきなら書けそう」と理解し、QRを読めることを最優先にします。

視線の順序を次に固定します。

```text
日常を、言葉に。
→ 具体例3件
→ 大きなQR
→ ひとことを書く → ひとこと返しを見る
→ 最低限の安心・注意
```

掲示面では返し例を並べません。

返しはQR先の体験として残します。

## 2. Visual tone

- A4縦。
- 白〜生成り背景。
- 深い緑を主色。
- 黄〜オレンジは少量のaccentのみ。
- 温かいが幼くしない。
- 静かだが、QRへの入口は明確にする。
- Web UI / SaaS card gridの均一感を避ける。
- 手作り感はcontrolled imperfectionで出し、装飾量では作らない。
- 文化祭ポスターや啓発ポスターのようにしない。
- 広報ネタ募集・改善提案BOXに見せない。
- AI生成物らしさを消すための装飾追加をしない。

```text
Quiet participation entrance.
Warm, adult, editorial.
Less explanation, more permission to notice.
```

## 3. Information density

V2までの紙面より明確に減らします。

目安として、V2の本文量のおよそ半分以下をproduction surfaceの上限とします。

V3で許可する主要情報は次だけです。

- header / title / lead
- short explanation 1文
- examples exactly 3
- CTA / QR
- reassurance 2文
- safety / routing 2文
- closing

次は掲示面へ載せません。

- reply examples
- A→B→C→D
- AI説明
- system説明
- 投稿フォーム説明
- 長い運用説明
- 詳細なtrial specification
- 未確定の匿名性、閲覧範囲、保存期間

## 4. Typography

主要見出しは親しみのある丸みを持たせてもよいですが、本文の可読性を優先します。

推奨:

```css
:root {
  --font-family-heading: 'Zen Maru Gothic', 'Hiragino Maru Gothic ProN', sans-serif;
  --font-family-body: 'Noto Sans JP', 'Yu Gothic', sans-serif;
}
```

A4実寸での視認性を最終判断にします。

タイトルは第一焦点。

例文は50〜80cm程度から「内容の種類」が読めるサイズを目標にします。

安全文言は小さくしても判読可能なサイズを維持します。

## 5. Color

推奨token:

```css
:root {
  --color-primary: #164A42;
  --color-primary-soft: #5E8C78;
  --color-background: #F6F2E8;
  --color-paper: #FFFDF7;
  --color-mint: #DDEDE2;
  --color-accent-yellow: #F2C94C;
  --color-accent-peach: #D7A38C;
  --color-line: #174A42;
  --color-skin-base: #F1D2B6;
}
```

黄・オレンジは文字色の主役にしません。

重要本文は十分なcontrastを持つdeep greenを使います。

## 6. Example notes

3件の例は、同一UIカードではなく、少し異なる紙メモとして見せます。

- exactly 3 notes
- 破いた紙 / 方眼紙 / テープ留め紙など、素材差は小さく
- 角度差は固定的に2〜4度以内を目安
- 影は弱く
- テープやクリップは必要な箇所だけ
- reply card / reply arrowは置かない

3件の内容差が視覚的にも混ざらないよう、適度な段差と余白を作ります。

## 7. QR / CTA

V3ではQRを紙面中央付近の主要行動対象にします。

タイトルの次に目立つ情報群はexamplesで、その直後にQRへ着地させます。

QR単体を広告的に巨大化するのではなく、次のCTAと一つの行動ブロックとして成立させます。

```text
QRからどうぞ
ひとことを書く → ひとこと返しを見る
30秒くらい。文章にしなくても大丈夫です。
```

QRはWeb UI card風の囲みではなく、紙面上の静かな参加入口として扱います。

- 十分なquiet zoneを確保する。
- texture / opacity / filter / decorative overlayをQRへ重ねない。
- canonical QR assetを使う。
- Preview Channel URLを使わない。

Authoritative destination:

`https://hitokoto-kaeshi-preview.web.app/poster`

## 8. Illustration — exactly one scene

V3の人物イラストは**1場面だけ**です。

場面テーマ:

`現場の日常の中で、一瞬立ち止まって気づきをメモしようとしている成人職員`

目的は説明ではなく、人の気配を少しだけ添えることです。

- adult editorial flat illustration
- 成人として自然な頭身
- mascot / chibi / anime / 3D / photo風を避ける
- pure blackではなくdeep green系の線
- 表情は「少し気になった」程度
- 大げさな笑顔・驚き・感情線を避ける
- 福祉を人物記号で表現しない
- QRより視覚的に弱くする
- 2場面目、3場面目を足さない

## 9. Controlled imperfection

- 完全中央揃えを避ける。
- 例メモに小さな角度差を持たせる。
- brush / markerは1〜2箇所まで。
- runtime randomは使わない。
- 位置差は再現可能な固定値にする。
- 植物・付箋・テープ・線画を空き埋め目的で増やさない。

## 10. Reassurance / safety

安心・注意は紙面下部にまとめます。

Primary reassurance:

- `書いたひとことが、そのまま広報に使われることはありません。`
- `必要なものだけ、広報部会で少し先を考えます。`

Secondary safety:

- `氏名など、個人がわかる情報は書かないでください。`
- `事故・虐待・苦情・職場の相談などは、いつもの相談・報告ルートへ。`

安全文言は読めることを優先しますが、紙面の主役にはしません。

## 11. Print / Physical QR

A4実寸で確認します。

過去Canva candidateのPhysical QR PASSはV3へ継承しません。

V3 final production candidateについてfreshに次を確認します。

```text
actual intended final paper size / print settings
physical device scan
canonical /poster PASS
Preview Channel redirect 0
```

PDFをfinal candidateに使う場合は、日本語フォント埋込とPDF render後のQR decodeも確認します。

## 12. Authority boundaries

この文書とV3 implementation candidateは、次のGateを通過させません。

- Human Visual Acceptance
- Canva final save
- Physical A4 / fresh QR validation
- CLOUD-TRIAL activation
- LIVE WRITE
- Merge
- Print / Post
- Real Trial Start
- Actual Staff Pilot
- Pattern / Prompt / Foundation promotion

2026年12月の第2回広報部会までは、明示的なHuman superseding decisionがない限り正式導入しません。
