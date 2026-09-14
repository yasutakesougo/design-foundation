# Critical Review — PERSONAL-DECISION-PRINCIPLES-V1

この文書は、Critical Review と principle 更新契約の candidate です。

原則本文の正本は `README.md` です。この文書は P-01 … P-08 を複製しません。

この文書は accepted authority ではありません。

## Independent Review との区別

```text
Independent Review
= 対象 artifact は、すでに決まった契約に適合しているか。

Critical Review
= その原則 / 判断規則自体が、今の状況に対してまだ適切か。
```

Independent Review を Critical Review で置き換えません。

Critical Review は Independent Review の PASS / HOLD を代行しません。

Human GO を生成、推定、代理消費しません。

canonical principles を Critical Review 自身が mutation しません。

## On-demand only

Critical Review は on-demand だけです。

定期実行、CI、自動発火、常時ロードは V1 対象外です。

Agent は Critical Review を自動実行しません。

人間が明示的に求めたとき、または人間が下記 trigger を認めたあとにだけ実施します。

## Trigger candidates

Trigger 候補は次に限定します。

```text
- 同一原則が原因の HOLD が繰り返される
- Human Gate / 判断のオーバーヘッドが増えている
- 運用負担が実質的に大きい
- 原則同士が衝突する
- 原則を実質的に新しい種類の作業へ適用している
- 原則の期待と、実際の運用証拠が繰り返し食い違う
```

この一覧にない理由だけで Critical Review を始めません。

Trigger 候補を満たしても、それ自体は Human GO ではありません。

## できること / できないこと

できること:

- 対象原則が現状に合っているかを問う
- Principle Candidate を推奨する
- HOLD の理由と、人間が次に判断できる材料を残す

できないこと:

- canonical principle set を書き換える
- Human GO を生成、消費、推定する
- Independent Review を置き換える
- 単一判断から共有原則を mint する
- 自動で Candidate を昇格する

## Principle update contract

更新フローは自動化しません。

```text
Actual Decision
↓
Decision Rationale
↓
Repeated Pattern Detection
↓
Principle Candidate
↓
Critical Review
↓
Human Decision
↓
Canonical Principle Update
```

### 各段の意味

```text
Actual Decision
= 実際に行った判断。仮想の例だけでは足りない。

Decision Rationale
= その判断でどの原則 / 領域（RULE / SHARED / PERSONAL）を使ったか。

Repeated Pattern Detection
= 同様の判断が繰り返されたことの確認。1回では不十分。

Principle Candidate
= 共有原則の提案。現行 P-01 … P-08 の置換案または追加案。
  AI が作成してよい。canonical ではない。

Critical Review
= Candidate と現行原則の適切さを、契約適合レビューとは別に問う。

Human Decision
= 人間の明示入力だけが authority。GO なしでは更新しない。

Canonical Principle Update
= Human Decision の後にだけ、candidate 正本（この workstream では README.md）
  を更新する。accepted / runtime への昇格は別 Gate。
```

AI は Principle Candidate を示せます。

AI は Candidate を canonical principle set へ自動昇格しません。

単一の Actual Decision だけでは、新しい共有原則を作りません。

## 既存 Human authority との関係

Human Gate、mutation boundary、UNKNOWN の扱いはこの文書が定義しません。

既存正本:

- `references/accepted/agent-operating-foundation-v1/operating-contract.md`
- `references/in-progress/agent-skill-architecture-v1/invocation-model.md`

Critical Review の推奨は、それらの Human Gate を通過しません。

## Completion criteria

Critical Review candidate は、次をすべて満たすときにこの文書として成立します。

- Independent Review と Critical Review が区別されている
- on-demand であり、自動実行しない
- trigger が限定列挙である
- Principle Candidate は作れるが、自動昇格しない
- canonical update に明示的 Human Decision が必要である
- 原則本文の正本が `README.md` のままである
