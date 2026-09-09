# DESIGN-MD-INTAKE-PILOT-V1

## 目的

DESIGN.md Maker JPなどで生成した `DESIGN.md` を、Design Foundationの正本ではなく、Human Direction Selection前のcandidateとして扱う方法を検証します。

狙いは、曖昧なデザイン意図を構造化し、複数エージェント間の解釈差を減らせるか確認することです。

## Pilotで確認すること

少なくとも1件の新規または独立したデザイン課題で、次を確認します。

1. 同じ要件を複数エージェントへ渡したときの解釈差が減るか。
2. Foundationとの衝突を明示できるか。
3. 抽象的なデザイン語を観察可能なルールへ変換できるか。
4. Human Direction Selectionの判断材料として役立つか。
5. Web UI寄りの提案を印刷物や広報物へ無理に持ち込まないか。
6. 外部サービスを使わない案件でも既存フローが成立するか。

## Authority

優先順位は次の通りです。

```text
Human Definition / Content Authority
↓
foundations/* + Accessibility Baseline
↓
Accepted / Rejected Reference
↓
external DESIGN.md candidate
↓
individual agent interpretation
```

外部candidateはCanonical Design Guideではありません。

Foundationと衝突する場合はFoundationを優先します。

## Pilot workflow

```text
Human Definition / Scope Lock
↓
Content Structure / Content Lock
↓
Foundation readback
↓
DESIGN.md candidate generation（必要時のみ）
↓
review/design-md-intake.md で normalization / conflict check
↓
Concept Exploration（必要時のみ）
↓
Human Direction Selection
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
Preflight
↓
Human Output GO
```

## Pilot files

- `candidate-template.md`: candidateをローカル形式へ整理するテンプレート。
- `../../external/design-md-maker-jp.md`: 外部サービスのprovenanceと利用境界。
- `../../../review/design-md-intake.md`: normalizationとconflict checkの確認基準。

## Privacy

外部サービスへ個人情報、ケース記録、認証情報、秘密情報を入力しません。

必要な文脈は、一般化した対象者、目的、媒体、雰囲気、情報量へ変換します。

## Promotion boundary

Pilotが成功しても、生成された `DESIGN.md` 自体をFoundationへ昇格しません。

複数案件で繰り返し有効だった判断だけを、別ScopeでFoundation、Pattern、Promptの候補にします。

## Current status

- Human Definition / Scope Lock: GO / CONSUMED / LOCKED
- Human Implementation Start: GO / CONSUMED / AUTHORIZED
- Pilot implementation: IMPLEMENTED / FRESH REVIEW REQUIRED
- Human Ready: HOLD
- Merge / Promotion: HOLD
