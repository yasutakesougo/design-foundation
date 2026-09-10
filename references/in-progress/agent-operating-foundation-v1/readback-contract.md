# Readback / Reconstruction Contract

Readbackは、前任エージェントの会話履歴がなくてもrepository上の証拠から現在地を再構成するための契約です。

V1ではsession event storeを導入しません。

GitHub上の既存artifactをEvidence Chainとして扱います。

## 最小Evidence Chain

```text
Issue Definition
→ Independent Review
→ Human Gate comment
→ implementation PR
→ exact HEAD
→ CI / review evidence
→ merge state
→ next unconsumed gate
```

各段階は、存在が確認できた証拠だけを採用します。

## 再構成する状態

保守エージェントは少なくとも次を復元します。

1. canonical Definition
2. latest independent review
3. consumed Human Gates
4. next unconsumed Human Gate
5. implementation PRとexact HEAD
6. merge / draft / open state
7. applicable canonical contracts
8. unresolved findings
9. evidence gaps
10. permitted next action

## Authority order

状態が食い違う場合は、最新の実体readbackを優先します。

```text
1. current GitHub state / current PR metadata
2. exact commit / diff / CI evidence
3. Human Gate comments
4. Definition / Review documents
5. handoff summary
```

ただし、Human Gate authorityそのものは人間の明示入力以外から生成しません。

## UNKNOWNの扱い

取得不能と「存在しない」を区別します。

```text
not found after authoritative readback
≠
readback unavailable
```

確認できない状態は次のように扱います。

```text
State  = UNKNOWN
Action = HOLD or additional readback
```

UNKNOWNをPASS、CLOSED、MERGED、CONSUMEDへ補完しません。

## Stale evidence

過去のHEADやhandoffに書かれたstateをcurrentとして扱いません。

PRに新しいcommitがある場合、以前のreview PASSは新HEADへ自動継承しません。

exact HEADに対する証拠かを確認します。

## Live stateの境界

repository readbackだけで次を断定しません。

- rendered UIの見え方
- live integrationの成功
- real staff / real user value
- runtime failureの不存在
- production deploymentの健全性

これらは`observability-boundary.md`に従います。

## Pilot input candidate

将来のhandover pilotでは、次の最小入力を想定します。

```text
- repository URL
- target workstream ID
- prior conversation unavailable
```

この入力だけから現在地と次操作を復元できるかを評価します。

## Fail conditions

- Human GOを推定する。
- stale HEADをcurrent扱いする。
- UNKNOWNをPASS扱いする。
- reference candidateをaccepted authority扱いする。
- live runtime stateをrepository evidenceだけで断定する。
- next unconsumed gateを飛ばす。

## Completion criteria

Readbackは、再構成した各状態に確認可能なEvidence Chainがあり、未確認項目がUNKNOWNとして明示され、次の許可操作がHuman Gateを迂回していないときに完了します。
