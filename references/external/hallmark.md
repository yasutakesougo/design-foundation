# Hallmark — External Reference

## Reference

- Repository: `Nutlope/hallmark`
- URL: https://github.com/Nutlope/hallmark
- Reviewed commit: `13ac0ec7e148655948100b6396439e481361d690`
- Reviewed date: `2026-09-08`
- License: MIT
- Role: reference-only

このファイルはHallmark自体のprovenanceと、このDesign Foundationへ採用した考え方・採用しなかった考え方を記録します。

HallmarkをSkill、package、submodule、runtime dependencyとして組み込みません。

## 採用する考え方

### 1. Design DNA extraction

参考デザインを外観のコピー対象として扱わず、次のような移植可能な判断へ分解して参照します。

- information hierarchy
- composition / information structure
- typography role
- color anchor / color usage
- spacing / rhythm
- illustration role
- carry overしない要素

Hallmark固有の用語やWeb向けcatalogを、このRepositoryの共通語彙として必須化しません。

### 2. Named Anti-patterns

Rejected Referenceで同じ失敗の再発防止に役立つ場合だけ、短いAnti-pattern名を付けます。

HallmarkのAnti-pattern一覧をコピーせず、このRepositoryで実際に確認した失敗だけを蓄積します。

### 3. Promotion after iteration and Human acceptance

初回生成物や一度のAccepted結果を自動的にDesign Foundationへ昇格させません。

実案件での利用、必要なCorrection、Human Visual Acceptanceを経て、複数案件で再利用できると確認された判断だけを共通Foundationへ戻します。

## Responsibility boundary

- **Design DNA extraction**: Referenceから再利用できる特徴を読み取る任意の参照分析。
- **Concept Exploration**: 今回の制作物について構成や情報の流れを比較する任意工程。
- **Human Direction Selection**: Foundation、必要なDesign DNA、Concept Explorationを踏まえて今回の方向を人が選ぶ工程。
- **Foundation**: 外部ReferenceのDesign DNAより常に優先する共通判断基準。

Referenceがない制作ではDesign DNA extractionを行う必要はありません。

Design DNA extractionをFlyer Flowの新しい必須工程にはしません。

## Third-party reference boundary

第三者Referenceから抽出するのは、情報階層、構成原理、書体の役割、色の使い方、余白・リズム、イラストの役割などの移植可能な判断に限定します。

第三者の固有イラスト、写真、ロゴ、特徴的な表現、テンプレート固有の外観を複製しません。

この `hallmark.md` はHallmark自体のprovenance専用です。

将来分析する第三者Referenceのprovenanceをここへ混在させません。永続記録する価値がある場合は、成果物・判断と結び付けてAccepted / Rejected Referenceへ残します。単発の参考は永続化を必須にしません。

## 採用しないもの

V1では次を取り込みません。

- Hallmark Skill / runtime installation
- theme catalog
- macrostructure catalog
- slop-test gate set
- `tokens.css` contract
- Hallmark固有のDesign Token体系
- Web固有のnavigation / footer / motion / component catalog
- automatic `design.md` generation
- AIによる最終デザイン採否

## Re-review conditions

次の場合は、この参照を自動更新せず再レビューします。

- 別commitのHallmarkから新しい考え方を採用したい場合
- Hallmark本体をruntime / Skillとして導入したくなった場合
- theme、gate、token、component catalog等を追加採用したくなった場合
- このReferenceの採用内容がFoundationの責務やHuman Gateへ影響する場合
