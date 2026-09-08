# design-foundation

チラシ、Web、アプリUI、広報資料、イラストで使う共通のデザイン判断基盤です。

このリポジトリは完成物を大量に保存する場所ではなく、再利用できる判断基準、参照例、レビュー基準を正本として管理します。

## V1の対象

- `foundations/`: 複数制作物で共通利用する原則。
- `patterns/`: 媒体別の再利用パターン。
- `skills/`: 構想探索など、必要時だけ使う制作手順。
- `prompts/`: 制作時に再利用する指示テンプレート。
- `review/`: Human Reviewを補助する確認基準。
- `references/`: 採用・不採用事例と外部参照の記録。

## 共通Foundationと個別Style Guideの境界

Design Foundationは、複数案件で再利用できる判断だけを扱います。

個別案件では、内容、情報構造、対象者、媒体、ブランドに応じて適用方法を調整します。

案件固有の判断は、再利用性が確認されるまでFoundationへ昇格させません。

## 基本フロー

```text
Content Lock
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
Final
↓
Accepted Reference
```

文章とデザインは同時に大きく変更しません。

Concept Sketchは完成物ではなく、方向性を比較するための探索物です。

最終的なデザイン採否は自動化せず、`Human Visual Acceptance` を最終判断とします。

## V1で扱わないもの

- Figma / Canva同期。
- Storybook。
- Design Tokensの自動配布。
- npm package化。
- CIによるデザイン自動合否。
- 大規模なブランドガイドライン。
- 外部Skillや外部デザインシステムのruntime依存化。

まず実案件で使い、繰り返し必要になったものだけを追加します。
