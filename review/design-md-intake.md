# DESIGN.md Intake Review

## 対象

外部サービスやAIが生成した `DESIGN.md` を、Human Direction Selection前のcandidateとして利用するときに使います。

案件の方向性が既に十分明確な場合は、このレビュー自体を省略できます。

## 先に確認するもの

candidateを読む前に、次を確認します。

- Human Definition / Scope
- Content Authority
- `foundations/*`
- `foundations/accessibility.md`
- 必要なAccepted / Rejected Reference

外部candidateを先に読んで、後からFoundationを合わせません。

## 入力してよい情報

外部サービスへ渡す情報は、公開して問題ないデザイン要件に限定します。

個人情報、ケース記録、認証情報、秘密情報は入力しません。

必要な案件文脈は、対象者、目的、媒体、雰囲気、情報量などへ一般化します。

## Candidate normalization

外部candidateを保存するときは、サービス固有の説明をそのまま正本化せず、次の項目へ整理します。

- Project purpose
- Audience
- Medium / output context
- Visual tone
- Typography roles
- Color roles
- Spacing / rhythm
- Composition principles
- Illustration / photography role
- Accessibility constraints
- Anti-patterns / avoid list
- Source
- Reviewed date
- Foundation conflicts
- Project-specific items

該当しない項目は無理に埋めません。

## Conflict check

各candidate ruleを、次のいずれかに分類します。

### ACCEPT AS CANDIDATE

Foundationと矛盾せず、今回の案件で試す価値がある判断です。

この判定だけではFoundationへ昇格しません。

### PROJECT-SPECIFIC

今回の案件では有効でも、共通Foundationへ持ち込む根拠がない判断です。

candidate内に残します。

### OVERRIDDEN BY FOUNDATION

既存FoundationまたはContent Authorityと衝突する判断です。

外部candidate側を採用しません。

### HOLD

根拠不足、意味不明、検証不能、またはHuman判断が必要な項目です。

自動的に補完しません。

## Accessibility check

外部candidateにWCAG、CUD、コントラスト、文字サイズ等の記述があっても、その記述をPASS evidenceとして扱いません。

既存のAccessibility Baseline Checkで再評価します。

外部candidateのアクセシビリティ記述は、確認項目を見つけるための参考情報としてのみ使います。

## Anti-AI translation

`AIっぽくしない`、`自然にする`、`温かくする` のような抽象語は、そのまま制作指示に残しません。

観察可能なルールへ変換します。

例:

```text
抽象: AIっぽくしない
↓
候補ルール:
- すべてを左右対称にしない
- 同じ角丸カードを反復しない
- 装飾目的のアイコンを増やさない
- 余白を均等割りしすぎない
- 人物イラストを過度にデフォルメしない
```

変換したルールもHuman Direction Selection前のcandidateです。

## Review output

レビュー結果は次の形で残します。

```text
Candidate source:
Reviewed date:
Purpose:

Accepted candidate rules:
- ...

Project-specific rules:
- ...

Overridden by Foundation:
- ...

HOLD:
- ...

Accessibility re-check required:
- YES / NO

Human Direction Selection ready:
- YES / NO
```

## Gate boundary

このレビューはHuman Direction Selectionを置き換えません。

このレビューはHuman Visual Acceptanceを置き換えません。

このレビューはHuman Output GOを置き換えません。

candidateの採用結果から、Pattern、Prompt、Foundationへの自動Promotionを行いません。
