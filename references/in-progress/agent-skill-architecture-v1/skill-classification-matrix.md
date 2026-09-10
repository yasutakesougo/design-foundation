# Skill classification matrix

この表は、現行資産と将来候補をHuman-invoked / Model-invoked / Referenceの観点で整理するための候補です。

このV1ではruntime metadataを変更しません。

## 現行資産

| 対象 | 現在の役割 | V1での扱い | Human Gate authority |
|---|---|---|---|
| `skills/concept-sketch/SKILL.md` | 構成・情報の流れ・代替案を比較する既存Skill | runtime semanticsを変更せずbaselineとして保持 | なし |
| `foundations/*` | 複数制作物で共通利用する原則 | Reference正本 | なし |
| `patterns/*` | 媒体別の再利用パターン | Reference正本 | なし |
| `review/*` | Human Reviewと出力前確認を補助する確認基準 | Model-invoked disciplineから参照可能なReference正本 | なし |
| `references/accepted/*` | Human Acceptance後の参照 | Reference正本 | なし |
| `references/in-progress/*` | 未昇格の候補・検証物 | Reference candidate | なし |

## Human-invoked orchestrator候補

| 候補 | 人間が開始する理由 | 到達点 | 自動化しないもの |
|---|---|---|---|
| Definition / Scope preparation | 目的と変更範囲の開始判断が必要 | Reviewへ渡せるDefinition candidate | Human Definition / Scope Lock |
| Reference Intake start | 外部参考を使う判断が必要 | Borrow / Do Not Copyを分離したintake | Foundation Promotion |
| Concept exploration start | 複数案を比較する判断が必要 | Human Direction Selectionへ渡せる比較案 | Human Direction Selection |
| Output route / preflight start | 印刷・公開経路を選ぶ判断が必要 | Human Output GO前の確認結果 | Human Output GO |
| Handoff preparation | sessionや担当を切り替える判断が必要 | fresh agentが現在地を復元できるhandoff | 後続Human Gate |

Human-invoked orchestratorはHuman Gateではありません。

## Model-invoked discipline候補

| 候補 | 発火条件 | 参照する正本 | 到達点 |
|---|---|---|---|
| accessibility review | 制作物のアクセシビリティ確認が必要 | 該当するFoundation / Review | 確認結果を残す |
| output preflight check | 印刷または公開前 | `review/output-preflight.md` | preflight結果を残す |
| typography role check | 文字の役割・書体判断が必要 | typography関連Foundation | 適用結果を残す |
| color foundation check | 配色判断が必要 | color関連Foundation | 適用結果を残す |
| reference-intake discipline | 外部参考を分析する | Reference Intake正本 | Borrow / Do Not Copyを分離する |
| agent-document writing discipline | Agent向けSkill / pointer / instructionを書く | 本Architectureのpointer / completion criteria規則 | 文書がcheckableな構造になる |

Model-invoked disciplineはHuman Gateを遷移させません。

## Reference候補

| 対象 | 読む条件 | 正本性 |
|---|---|---|
| Foundation docs | 共通原則を適用するとき | 正本 |
| Pattern docs | 媒体別パターンを適用するとき | 正本 |
| Review checklists | 該当レビューを行うとき | 正本 |
| Accepted references | 採用済み判断を参照するとき | 正本 |
| External reference intake records | 外部参考の採否理由を確認するとき | ローカル判断の正本 |
| Gate vocabulary / authority rules | Agentが工程やmutation可否を判断するとき | always-visible契約から到達する正本候補 |

## 分類時の禁止事項

分類しただけではruntimeを有効化しません。

分類しただけでは外部Skillをインストールしません。

分類しただけでは既存Skillを書き換えません。

分類しただけではHuman Gateを消費しません。

## Completion criteria

分類対象ごとに次の4点が明確になれば完了です。

- 誰が起動できるか。
- どの条件で使うか。
- どの正本を参照するか。
- どのHuman authorityを持たないか。
