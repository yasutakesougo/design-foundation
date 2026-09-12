# Automation Contract

## Network boundary

外部通信は HTTPS の GET のみに限定します。

許可 host は `api.github.com` と `raw.githubusercontent.com` の exact hostname です。

許可 repository は `yasutakesougo/design-foundation` の exact owner/repository identity です。

redirect は追従しません。

3xx は `HOLD / REDIRECT_NOT_ALLOWED` として扱います。

## Packet identity

Packet の substantive payload から `ReviewId`、`IdempotencyKey`、`PacketSHA256` だけを除外して canonical JSON 化し、その bytes の SHA-256 を `PacketSHA256` とします。

Idempotency preimage は、Issue #251 Correction-1 が指定する7フィールドだけを持つ canonical JSON object です。

`ReviewId` は `IdempotencyKey` から決定的に導出します。

## Reviewer process

reviewer command は argv vector として外部から受け取ります。

`shell=False` とし、packet bytes を stdin に渡します。

child environment は固定 allowlist と、`FRA_REVIEWER_CONTEXT`、`FRA_REVIEW_ID`、`FRA_PACKET_SHA256` に限定します。

`FRA_REVIEWER_CONTEXT=1` からの nested invocation は拒否します。

coordinator instance 全体で reviewer process は同時に1つだけです。

same-key active duplicate は `DUPLICATE`、cross-key concurrent invocation は `BUSY` です。

automatic retry count は 0 です。

`FRA_DISABLE=1` のとき reviewer process は起動しません。

## Reviewer output

reviewer stdout bytes を改変せずに検証します。

`ReviewerOutputSHA256` は coordinator が exact stdout bytes から計算します。

independence-required PASS には、`Contamination=NONE`、`ExcludedItemIntentionallyRetrieved=NO`、`ExcludedItemObserved=NO`、`P0=0`、`P1=0` が同時に必要です。

`MutationAttempted=YES` または `HumanGateInferredOrConsumed=YES` は fail-closed です。

## Relay

reviewer stdout bytes は Base64 で可逆保存します。

relay envelope 作成時に decode 後 bytes と SHA-256 を再検証します。

この slice は relay target へ書き込みません。

## Reconciliation

reconciliation は fresh GET と現在の caller-supplied authority identity を再照合します。

正の結果は次の1種類だけです。

```text
REVIEW_PREDICATE_SATISFIED__REEVALUATE_EXISTING_AUTHORITY
```

Human GO、AUTO_RESUME、READY、MERGE、DEPLOY、PROMOTION は生成しません。
