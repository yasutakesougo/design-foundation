# Observability Boundary

Observability Boundaryは、repository evidenceだけで確認できる状態と、live runtime evidenceが必要な状態を分離するための契約です。

V1ではOpenTelemetry、trace backend、AI call inspector、session databaseを導入しません。

## Repository evidenceで確認する状態

次はGitHub readbackを主証拠にできます。

- Issue / PRのopen・closed・draft・merged state
- exact commit / HEAD
- changed paths
- Definition / Review内容
- Human Gate comments
- CI / review evidenceの存在と対象SHA
- next unconsumed gate

確認不能な場合はUNKNOWNです。

## Live runtime evidenceが必要な状態

次はrepository evidenceだけではPASSにしません。

- rendered UIが期待どおり見えること
- browser / device上のinteraction
- live API / SharePoint / Firebase等とのintegration成功
- production deploymentの実動作
- runtime exceptionの不存在
- real staff / real userによる価値確認
- real dataでのbehavior

必要なlive evidenceがない場合はHOLDです。

## Evidence substitutionを禁止する例

```text
synthetic rendering
≠ Actual Staff Value Check

unit test PASS
≠ live integration PASS

merged commit
≠ production healthy

repository config
≠ runtime connection confirmed
```

異なる証拠クラスを同一のPASSとして代用しません。

## Runtime evidenceの最小要件

live stateを判定するときは、少なくとも次を明示します。

```text
target
environment
exact build / commit if applicable
evidence type
observation time or run identity
result
limitations
```

証拠が対象buildと結び付かない場合は、current PASSとして扱いません。

## 将来observabilityを導入する条件

次の問題が反復し、GitHub readbackだけでは原因特定できない場合にruntime observabilityを別Definitionで検討します。

- agent actionの順序や失敗点を再構成できない。
- live integration failureの原因がlog不足で不明になる。
- 同一障害の再現性が低く、trace相関が必要になる。
- handover時にruntime状態の証拠が不足する。

導入する場合も、telemetry自体をHuman Gate authorityにはしません。

## Privacy / scope rule

observability導入時は必要最小限のevent、log、traceだけを対象にします。

個人情報や支援記録等の業務データを、設計上の必要性と別途承認なしにtelemetryへ送る前提を置きません。

## First sliceで行わないこと

- OpenTelemetry導入
- trace collector導入
- AI call logging
- session event store
- production telemetry
- runtime instrumentation
- CI telemetry

## Completion criteria

状態判定に使う証拠クラスが明示され、repository evidenceとlive runtime evidenceが混同されず、証拠不足時にPASSへ補完されないときに成立します。
