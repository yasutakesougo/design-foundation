# design-foundation

チラシ、Web、アプリUI、広報資料、イラストで使う共通のデザイン判断基盤です。

このリポジトリは完成物を大量に保存する場所ではなく、再利用できる判断基準、参照例、レビュー基準を正本として管理します。

## V1の対象

- `foundations/`: 複数制作物で共通利用する原則。
- `patterns/`: 媒体別の再利用パターン。
- `skills/`: 構想探索など、必要時だけ使う制作手順。
- `prompts/`: 制作時に再利用する指示テンプレート。
- `review/`: Human Reviewと出力前確認を補助する確認基準。
- `references/`: 外部参照や制作結果から、再利用できる判断を抽出して記録する場所。

方向性案は `references/directions/`、Human Visual Acceptance前のドラフトは `references/in-progress/` に置きます。

外部参考を使う場合は `references/reference-intake-template.md` で、再利用する原則とコピーしない固有表現を分離します。

初案や外部参考を Pattern / Prompt / Foundation へ自動昇格しません。

Agent Skill Architectureの未昇格候補は `references/in-progress/agent-skill-architecture-v1/` に置きます。

この候補はSkill runtimeへ自動適用せず、Human GateやPromotionを変更しません。

Agent Operating Foundationのaccepted authorityは `references/accepted/agent-operating-foundation-v1/` に置きます。

このauthorityはrepositoryのreadback・applicability・refinement・observability境界を示しますが、root `AGENTS.md`、runtime activation、CI enforcementを自動有効化しません。

## 目的から探す

必要な正本へ直接移動するための入口です。

- 共通原則を確認する: [`foundations/`](foundations/)
- 文字のルールを確認する: [`foundations/typography.md`](foundations/typography.md)
- 媒体別の再利用パターンを確認する: [`patterns/`](patterns/)
- 制作時の再利用Promptを確認する: [`prompts/`](prompts/)
- レビュー基準を確認する: [`review/`](review/)
- 公開・印刷前の確認をする: [`review/output-preflight.md`](review/output-preflight.md)
- Accepted Referenceを探す: [`references/accepted/README.md`](references/accepted/README.md)
- Reference領域の役割を確認する: [`references/README.md`](references/README.md)

この一覧は入口であり、各項目の意味や状態はリンク先の正本と明示されたevidenceで確認します。

Acceptedであることをruntime activationや現在のworkstream stateへ読み替えません。

## 共通Foundationと個別Style Guideの境界

Design Foundationは、複数案件で再利用できる判断だけを扱います。

個別案件では、内容、情報構造、対象者、媒体、ブランドに応じて適用方法を調整します。

案件固有の判断は、再利用性が確認されるまでFoundationへ昇格させません。

## 基本フロー

```text
Human Definition / Scope Lock
↓
Content Structure / Content Lock
↓
Reference Intake（外部参考を使う場合のみ）
↓
Concept Exploration / Concept Sketch（必要時のみ）
↓
Design Direction / Human Direction Selection
↓
Draft
↓
Accessibility Baseline Check
↓
Visual Review
↓
Correction
↓
Human Visual Acceptance
↓
Output Route Selection
↓
Preflight（印刷・公開する場合）
↓
Human Output GO
↓
Print / Publish
↓
Accepted Reference
```

文章とデザインは同時に大きく変更しません。

Reference Intakeでは、参考作品をそのまま再現せず、レイアウト、文字、色、素材などへ分解します。

そのうえで、再利用する設計原則を `Borrow`、作品固有でコピーしない表現を `Do Not Copy` として分離します。

参考を分析しただけでは共通Foundationへ昇格させません。

Concept Sketchは完成物ではなく、方向性を比較するための探索物です。

最終的なデザイン採否は自動化せず、`Human Visual Acceptance` で決めます。

`Human Visual Acceptance` は見た目と情報設計の採否です。

`Human Output GO` は、QR、サイズ、塗り足し、解像度、誤字などの出力条件を確認した後に、印刷または公開してよいかを決める別ゲートです。

## Output Route Selection

制作物の種類に応じて、最終出力の経路を選びます。

```text
普通のPDF資料
Agent → Direct PDF

チラシ・ポスター・軽い広報物
Agent → Canva → PDF

冊子・ページ物・精密な印刷調整
Agent → Affinity等のページレイアウトツール → PDF
```

Canvaやページレイアウトツールを制作の起点にはしません。

内容整理、初稿、レビュー、修正方針はエージェント側で先に固めます。

人が直接触る編集ツールは、最終調整と出力制御の面として使います。

印刷または公開前の確認には `review/output-preflight.md` を使います。

## 人に説明すると

最初に人が「何を、誰に、どの形で伝えるか」を決めます。

外部のチラシやWebを参考にする場合は、好きな作品をそのまま真似せず、「余白が広い」「色数が少ない」などの要素に分けます。

次にエージェントが文章とレイアウトを整理し、完成品に近い初稿を作ります。

人は初稿を見て、読みやすさ、雰囲気、伝わり方を確認します。

修正するときは、直す範囲を絞ってエージェントへ戻します。

見た目が決まった後で、Canva、Affinity等、または直接PDFの経路を選びます。

最後にQRや印刷条件を確認し、人が `Human Output GO` を出してから印刷または公開します。

つまり、AIに全部を任せるのではなく、AIを主な制作担当にして、人は目的、採否、最終出力を受け持ちます。

## V1で扱わないもの

- Figma / Canva同期。
- Storybook。
- Design Tokensの自動配布。
- npm package化。
- CIによるデザイン自動合否。
- 大規模なブランドガイドライン。
- 外部Skillや外部デザインシステムのruntime依存化。

まず実案件で使い、繰り返し必要になったものだけを追加します。
