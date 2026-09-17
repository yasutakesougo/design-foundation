# In-Progress References

`references/in-progress/` は、まだAcceptedへ昇格していないcandidateを評価・検討し、必要に応じて運用Evidenceを蓄積するための領域です。

Human Visual Acceptance前のvisual candidateだけでなく、contract、workflow、review、architectureなどのnon-visual candidateも置かれることがあります。

## Authority boundary

このディレクトリへの配置や、このREADMEへの掲載だけでは状態や権限は決まりません。

```text
in-progress placement
!= Accepted authority
!= ACTIVE runtime authority
!= current lifecycle state
!= Human GO
!= Review PASS
!= Ready / Merge eligibility
!= Deploy / Print / Publish authority
!= Promotion
```

各workstreamの現在地は、そのworkstreamのcanonical Issue、PR、exact evidence chainから再構成します。

current GitHub stateとaccepted [`readback-contract.md`](../accepted/agent-operating-foundation-v1/readback-contract.md) が、このlocator indexより優先されます。

一覧への掲載有無、並び順、名前、更新時期やrecencyからcurrentnessやauthorityを推定しません。

## Candidate locators

以下は、このREADMEを作成した時点で確認できたcandidate directoryの例です。網羅的なregistryではなく、current lifecycle stateのauthorityでもありません。

- [`agent-skill-architecture-v1/`](agent-skill-architecture-v1/) — Agent Skill Architectureの未昇格candidate。
- [`brand-system-skill-extraction-v1/`](brand-system-skill-extraction-v1/) — Brand System Skillからの抽出candidate。
- [`delegated-execution-v2/`](delegated-execution-v2/) — Delegated Execution V2のcandidate contractsと運用Evidence。
- [`hitokoto-poster-v3/`](hitokoto-poster-v3/) — ひとことポスターV3の制作candidate。
- [`image-first-semantic-redraw-v1/`](image-first-semantic-redraw-v1/) — Image-first semantic redrawのcandidate。
- [`review-context-isolation-v1/`](review-context-isolation-v1/) — Review context isolationのcandidate。

候補の追加・削除によってこの一覧が古くなることがあります。その場合でも、一覧の欠落や残存をlifecycle stateとして読み替えません。

## Current stateの確認

Human Gate、Review verdict、exact current HEAD、merge eligibility、Deploy / Print / Publish state、Promotion readinessは、このREADMEにcurrent authorityとして記録しません。

確認が必要な場合は、対象workstreamのcanonical Issue / PR / exact evidenceを直接readbackしてください。
