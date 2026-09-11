# Correction Loop Contract

Independent Review で修正可能な問題が見つかった場合、人間を呼ばずに修正する。

## Loop

```text
Review
↓
Finding
↓
Correction
↓
Fresh Re-Review
```

Correction や Re-Review は元 Evidence を上書きせず、新しい Evidence として記録する。

## Limit

```text
MAX_CORRECTION_LOOPS = 3
```

同じ stage（Definition / Scope / Implementation / Visual）について、自律 Correction は最大 3 回まで許可する。

3 回で PASS しない場合は Human Escalation とする。

## Severity

```text
P0 / P1
= 自動継続を止める。境界内で安全に直せるなら Correction Loop へ。
  直せない、または境界変更が必要なら強制停止 / Escalation。

P2
= 記録して carry-forward できる。PASS を自動的に阻害しない。
```

## Fresh Re-Review rules

- Reviewed-HEAD は Correction 後の current exact HEAD へ bind する。
- 旧 HEAD への PASS を新 HEAD へ継承しない。
- applicable CI がある場合は新 HEAD の CI を確認する。
- Reviewer は Implementation context から分離し、成果物を直接読む。

## Escalation triggers

```text
Correction loop limit exceeded
P0/P1 not safely correctable inside boundary
Authority interpretation required
Scope expansion required
Human judgment explicitly required
Production / external mutation required
Required evidence remains UNKNOWN
```

## Non-authority

Correction Loop は write authority を増やさない。

Activation IN の外へ修正範囲を広げない。

Human GO を生成・推定・代理消費しない。
