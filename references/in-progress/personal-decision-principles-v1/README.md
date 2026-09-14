# PERSONAL-DECISION-PRINCIPLES-V1

個人の運用判断に使う原則の in-progress candidate です。

このディレクトリは第二の operating authority ではありません。

## Status

```text
Authority class                 = references/in-progress/ candidate
Workstream                      = PERSONAL-DECISION-PRINCIPLES-V1
Lifecycle-Issue                 = #262
Human Definition Lock           = CLAIMED in #262 / GitHub HUMAN-GATE comment NOT reconstructed here
Independent Definition Review   = SEPARATED
Human Implementation Start      = GO / CONSUMED (this Implementation)
Human Ready                     = HOLD
Human Merge                     = HOLD
Runtime activation              = HOLD
Always Loaded integration       = OUT of this V1
Promotion                       = HOLD
Accepted authority              = NO
```

このパスは accepted authority ではありません。

Review PASS は Human GO ではありません。

Human Gate 語彙と accepted operating authority は再定義しません。

## Purpose

既存の agent-context / operating architecture に、小さな参照層として Personal Decision Principles を置く候補です。

目的は、権限範囲内の個人判断を一貫させることです。

目的は、法、組織正本、Canonical Source、明示的 Human Gate を置き換えることではありません。

## Non-goals

```text
accepted/** mutation
foundations/** mutation
AGENTS.md mutation
AGENT-SKILL-ARCHITECTURE-V1 の責務変更
Skill invocation model の変更
Progressive Disclosure の変更
runtime context hierarchy の実装
Always Loaded への統合
他 architecture からの locator / pointer 追加
自動 principle 学習 / mutation
自動 Critical Review 実行
CI / workflow mutation
Promotion
```

## Human authority / mutation boundary（既存正本への pointer）

Human authority と mutation boundary の規範は、この candidate が持ちません。

次の既存正本を読みます。

- 常時見える不変条件: `references/accepted/agent-operating-foundation-v1/operating-contract.md`
- readback / UNKNOWN: `references/accepted/agent-operating-foundation-v1/readback-contract.md`
- candidate の Always-visible guardrails: `references/in-progress/agent-skill-architecture-v1/invocation-model.md`

Personal Decision Principles は、これらの上位層に勝りません。

Agent / Skill は Human GO を生成、推定、代理消費しません。

## Authority precedence

```text
Law / External Rules
↓
Organizational Authority / Canonical Source
↓
Explicit Human Gate
↓
Personal Decision Principles
↓
Domain / Project Rules
↓
Task Prompt
```

Personal Decision Principles は、この列で Explicit Human Gate より下に位置します。

法、組織権限、Canonical Source、明示的 Human Gate と衝突する場合は、上位を採用します。

## Documents

- `README.md`（このファイル）— P-01 … P-08 と RULE / SHARED / PERSONAL の candidate 正本
- `critical-review.md` — Critical Review と principle 更新契約
- `context-model.md` — 将来の agent context における概念上の位置。runtime 実装ではない

P-01 … P-08 の本文は、この README だけを candidate 正本とします。

他ファイルは pointer し、原則本文を複製しません。

## Locked V1 principles

```text
P-01 正本が特定できない状態では、不可逆または影響の大きい状態変更を進めない。
P-02 確認可能な事実を、推測、記憶、好みだけで決定しない。
P-03 不明なものは不明として扱い、不足した証拠をAIが補完しない。
P-04 同じ判断を複数箇所で独立管理せず、既存の正本を参照する。
P-05 状態変更の影響が大きいほど、判断領域を一段上げる。
P-06 個人判断が許される事項を、不必要にチームまたは組織判断へ上げない。
P-07 不確実な段階では可能な限り可逆に試し、実物・実データ・実運用を確認してから固定する。
P-08 HOLDには解除条件を示し、STOPには次へ進める条件がある場合その条件を示す。
```

自動 principle mutation は禁止します。

AI は Principle Candidate を示せます。

AI は canonical principle set へ自動昇格しません。

canonical 更新は明示的 Human decision だけです。単一の判断だけでは共有原則を作りません。

詳細は `critical-review.md` を読みます。

## Decision domains

V1 の判断領域は次の3つだけです。

```text
RULE     = 社会的・制度的・組織的ルールで確認できること
SHARED   = 複数人で共有または合意する必要があること
PERSONAL = 権限範囲内で個人が決めてよいこと
```

### 分類例（分類の説明に限定）

```text
RULE
= ライセンス、法令、組織の公開規則など、確認可能な外部/組織ルールがある判断。
  例: 著作権のある素材を無断で再配布しない。

SHARED
= 他者の作業、共通語彙、共有成果物の意味が変わる判断。
  例: チームで使う Gate 名を変える。accepted 正本の読み方を変える。

PERSONAL
= 権限内で、他者の必須合意なしに進められる可逆な運用判断。
  例: 自分の下書きメモの見出し順を試す。
```

例は分類の説明だけです。新しい原則や Gate 語彙を追加しません。

P-05 / P-06 は、影響が大きいほど領域を上げ、個人判断を不必要に上げない、という対です。

RULE または SHARED に当たる事項を PERSONAL として処理しません。

## Principle を使うとき

次のときに、この README の P-01 … P-08 を読みます。

- 明示的 Human Gate、法、組織正本、Canonical Source の下で、権限内の個人運用判断をするとき
- RULE / SHARED / PERSONAL のどれかを選ぶとき
- HOLD / STOP の書き方を決めるとき

次のときには、この原則より先に上位正本を読みます。

- Human Gate の GO / HOLD
- write / merge / publish / print / deploy / promotion の可否
- accepted operating authority の解釈

## Context model

将来の agent context における位置の候補表現は `context-model.md` です。

この V1 は、その文書を書くことだけを行います。

他 architecture からこのディレクトリへ locator / pointer を追加しません。

## Out of scope

```text
references/accepted/**
foundations/**
patterns/**
prompts/**
skills/**
review/**
AGENTS.md
CLAUDE.md
CONTEXT.md
Human Gate vocabulary rewrite
runtime orchestration
CI / workflow
Merge
Deploy / Print / Publish
Promotion
```
