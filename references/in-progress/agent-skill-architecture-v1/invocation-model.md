# Invocation model

SkillとReferenceは、誰が起動できるかと、何を決められるかを分けて扱います。

Human GateはSkill分類の外に置きます。

## 1. Human-invoked orchestrator

Human-invoked orchestratorは、人間が明示的に開始する工程を束ねます。

この分類は、複数のModel-invoked disciplineやReferenceを順に使うための入口です。

Human-invoked orchestratorはHuman Gateそのものではありません。

Human GOを生成、推定、代理消費しません。

完了条件は、定義した工程の出力が揃い、次のHuman判断へ渡せる状態になっていることです。

## 2. Model-invoked discipline

Model-invoked disciplineは、条件が合う場合にエージェントが自律的に使える再利用規則です。

対象は、レビュー、文章規約、アクセシビリティ確認、配色確認などの判断規則です。

Model-invoked disciplineはHuman Gateを遷移させません。

write、merge、publish、print、deploy、promotionのauthorityを暗黙に取得しません。

完了条件は、対象規則を適用した結果が確認可能な形で残っていることです。

## 3. Reference / context pointer target

Referenceは、実行手順ではなく定義、規則、判断根拠を保持します。

常時ロードせず、必要条件を持つpointerから参照します。

既存のFoundation、Pattern、Review、Accepted Referenceが正本を持つ場合は、その文書を参照します。

Referenceを新しい正本として複製しません。

## Human Gateとの境界

次のGateはSkill分類の外に置きます。

- Human Definition / Scope Lock。
- Human Implementation Start GO。
- Human Ready GO。
- Human Merge GO。
- Human Visual Acceptance。
- Human Output GO。
- Runtime activation / Promotionに対するHuman GO。

これらのGOは、人間が明示した場合だけ成立します。

SkillやAgentが、前後の状況からGOを補完してはいけません。

## 分類するときの判断順序

最初に、その処理が人間の明示開始を必要とするかを確認します。

必要ならHuman-invoked orchestrator候補です。

次に、その処理をエージェントが別の工程でも自律利用できるかを確認します。

自律利用でき、Human Gateを動かさない規則ならModel-invoked discipline候補です。

実行ではなく定義や根拠を読むだけならReference候補です。

どの分類でもHuman Gateのauthorityは取得しません。

## Always-visible guardrails

次の規則はProgressive Disclosureの対象外です。

- Human GateのGOは人間の明示入力だけがauthorityである。
- Skill / AgentはHuman GOを生成、推定、代理消費しない。
- write / merge / publish / print / deploy / promotionは、対応するauthorityが明示されている場合だけ実行する。
- Model-invoked disciplineはHuman Gateを遷移させない。

詳細な手順やbranch固有の規則だけをReferenceへ分離します。

## このV1で変えないもの

`skills/concept-sketch/SKILL.md` のruntime semanticsは変更しません。

既存SkillをHuman-invokedまたはModel-invokedへ強制再分類しません。

runtime metadataは、実利用Pilot後の別Definitionで扱います。
