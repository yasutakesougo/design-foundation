# DESIGN.md Maker JP — External Reference

## 参照情報

- Service: `DESIGN.md Maker JP`
- URL: `https://designmdmaker.jp/`
- Reviewed date: `2026-09-09`
- Role: reference-only / candidate generator

このファイルは、DESIGN.md Maker JPのprovenanceと、このRepositoryで採用する使い方の境界を記録します。

このサービスをDesign Foundation、runtime dependency、Canonical Design Guideとして扱いません。

## 2026-09-09時点で確認した機能

公開ページでは、対象者と目的を選び、雰囲気を入力し、AI提案から候補を選ぶ3段階の流れが案内されています。

日本語フォントと和色のプリセットを扱うと説明されています。

アクセシビリティについて、WCAG AAとCUDへの対応を掲げています。

最終結果として `DESIGN.md` とRationaleを出力すると説明されています。

料金、利用回数、UI、内部モデルの挙動は変更され得るため、このRepositoryの恒久契約にはしません。

## 採用する使い方

人が持つ曖昧なデザイン意図を、比較しやすい候補へ構造化する用途で使います。

生成された `DESIGN.md` は、Human Direction Selection前のcandidateとして扱います。

candidateは、`review/design-md-intake.md` でローカルFoundationとの衝突を確認してから利用します。

案件の方向性が既に十分明確な場合は、この工程を省略します。

## Authority boundary

優先順位は次の通りです。

```text
1. Human Definition / Content Authority
2. foundations/* と local Accessibility Baseline
3. Accepted / Rejected Referenceから得たローカル知見
4. DESIGN.md Maker JPが生成したcandidate
5. 個別AIエージェントの解釈
```

外部candidateがFoundationと衝突する場合は、Foundationを優先します。

外部candidateを自動でCanonical化しません。

外部candidateを自動でPattern、Prompt、Foundationへ昇格しません。

## Accessibility boundary

DESIGN.md Maker JPがWCAG、CUD、アクセシビリティ配慮を出力しても、その出力自体をこのRepositoryのPASS evidenceとして扱いません。

必ず `foundations/accessibility.md` と既存のAccessibility Baseline Checkで再評価します。

外部サービスの準拠表示だけを根拠に、ローカルのAccessibility PASSへ昇格しません。

## Privacy boundary

外部サービスへ入力する内容は、公開して問題ないデザイン要件に限定します。

次の情報は入力しません。

- 個人を特定できる利用者・職員情報
- 未公開のケース記録
- 認証情報、API key、秘密情報
- 第三者著作物の大量貼り付け

案件文脈が必要な場合は、個人や組織を特定しないデザイン要件へ一般化してから入力します。

## Copyright / reference boundary

第三者デザインの外観を再現するためのコピー指示には使いません。

参考デザインを扱う場合は、情報階層、構成、書体の役割、色の使い方、余白・リズム、イラストの役割などのDesign DNAへ分解します。

第三者の固有イラスト、写真、ロゴ、特徴的な表現、テンプレート固有の外観は複製しません。

## Hallmarkとの関係

`references/external/hallmark.md` にある `automatic design.md generation` の非採用は維持します。

その判断は、Hallmark由来の機能、runtime、catalogをV1へ取り込まないという当時の境界です。

本PilotはHallmarkの判断を上書きせず、DESIGN.md Maker JPを別External Sourceとして隔離評価します。

## 採用しないもの

- runtime dependency化
- API連携
- 自動ログイン
- 自動送信
- automatic Canonicalization
- Design Tokensの自動配布
- Human Direction Selectionの自動化
- Human Visual Acceptanceの自動化
- Human Output GOの自動化

## Re-review conditions

次の場合は再レビューします。

- サービスの主要な生成形式が変わった場合
- APIや自動連携を導入したい場合
- 外部candidateを共通Foundationへ直接反映したい場合
- アクセシビリティ判定の責務を変更したい場合
- 個人情報や非公開情報を扱う必要が生じた場合
