# Visual Evidence Path

UI、SVG、ポスター、印刷物などの視覚成果物では、Implementation 完了だけでは人間を呼ばない。

人間が判断できる状態まで委任側で完成させる。

非視覚の内部文書 / Foundation candidate では、この path は N/A とする。

## Path

```text
Implementation
↓
Render
↓
Desktop Evidence
↓
Mobile Evidence
↓
Print Evidence
↓
Agent Visual Review
↓
Visual Correction
↓
Fresh Visual Re-Review
↓
Human Visual Acceptance
```

媒体に存在しない evidence（例: Web-only の Print Evidence）は、不在理由を記録して N/A とする。存在すべき evidence を省略して PASS にしない。

## Agent Visual Review checklist

少なくとも次を確認する。

```text
文字切れ
重なり
不自然な改行
余白
階層
視線誘導
CTA
Typography authority
Color authority
Responsive behavior
印刷時の破綻
Definitionとの一致
```

## Human Visual Acceptance

ルールだけでは決められない視覚的・文脈的判断だけを人間に残す。

例:

```text
自然に見えるか
幼く見えないか
福祉を記号化していないか
生活感が適切か
Candidate A / B のどちらを採用するか
掲示物として採用したいか
```

到達時点で、技術的不具合や既知のルール違反を残さない。

## After Human Visual Acceptance GO

```text
Accepted Candidate固定
↓
Exact asset / SHA / HEAD固定
↓
Final verification
↓
PR Ready
↓
Merge
```

通常の Repository 内変更では、別途の Human Ready GO / Human Merge GO を要求しない。

Ready / Merge の Human authority は、IN に merge を含む Human Delegation Activation GO である。

## Visual Correction Loop

`correction-loop-contract.md` に従う。

```text
MAX_CORRECTION_LOOPS = 3
```

## Live boundary

Human Visual Acceptance は本番公開を許可しない。

本番・外部公開は `Human Live GO` が別途必要。詳細は `human-gate-model.md`。
