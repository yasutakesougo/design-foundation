# DESIGN-MD-INTAKE-PILOT-USE-1 — Result Evaluation

## Comparison target

- Route A: `draft-a-no-candidate.svg`
- Route B: `draft-b-candidate.svg`
- Same Content Authority: YES
- Same local Foundation baseline: YES
- External-style candidate used only in Route B: YES

## Render verification

Both SVGs were rendered at A4 portrait equivalent size for visual inspection.

Observed:

- Japanese text rendered after adding the available `Noto Sans CJK JP` fallback.
- no visible clipping
- no visible overflow
- title remains first focal point in both routes
- all three examples are readable
- closing copy remains readable

## Accessibility spot check

This is a local contrast spot check, not a complete Accessibility Baseline PASS.

Observed text/background contrast ratios:

- Route A primary `#24483D` on `#F8F6F0`: approximately `9.39:1`
- Route A body `#334A43` on `#F8F6F0`: approximately `8.83:1`
- Route B primary `#234B3E` on `#F6F2E8`: approximately `8.75:1`
- Route B body `#24352F` on `#F6F2E8`: approximately `11.56:1`
- Route B primary `#234B3E` on pale mint `#E9F0E8`: approximately `8.43:1`

Yellow is decorative emphasis only and is not required to read any text.

## A/B findings

| Evaluation point | Route A — no candidate | Route B — candidate intake | Finding |
| --- | --- | --- | --- |
| hierarchy | clear, centered | clear, left-led | both pass; B better matches the observant / editorial intent |
| palette | deep green + off-white + yellow | deep green + warm off-white + muted yellow + pale mint | both controlled; candidate removes color-choice ambiguity |
| spacing / rhythm | nearly even vertical rhythm | large title gap + clustered examples + distinct closing gap | B translates the Human intent into observable spacing roles |
| examples | three equal rounded blocks | three paper-like surfaces with small offsets | B reduces SaaS-card drift and over-neatness |
| illustration role | none | one small adult supporting scene | B fixes a bounded role instead of leaving illustration policy open |
| anti-pattern control | Foundation prevents excess, but shape language remains open | rounded-card repetition / all-centered / gradient / welfare pictogram explicitly blocked | B narrows common agent drift |
| hard Human-brief conflict | 0 | 0 | neither route changes the message |
| soft Human-intent mismatch | 2 | 0 observed | A under-expresses `少し人の手触り` and `小綺麗にまとめすぎない` |
| Foundation conflict | 0 | 0 after review | candidate did not override Foundation |

## Interpretation ambiguity proxy

This Dry Run cannot prove cross-model reproducibility because both routes were produced in one execution context.

Instead, it counts design decisions that remained materially open before drafting.

### Route A

At least six choices remained open to individual agent interpretation:

1. centered vs left-aligned title
2. symmetric vs asymmetric composition
3. equal UI-like blocks vs paper-like examples
4. uniform vs semantic spacing rhythm
5. illustration none vs small supporting scene
6. exact accent placement / treatment

### Route B

After normalization and conflict review, the same choices were mostly bounded:

- title alignment: fixed to left
- composition: lightly asymmetric
- repetition: identical SaaS-card repetition avoided
- spacing: semantic large / medium / compact roles
- illustration: 0–1 adult supporting scene
- accent: muted yellow, small marker-like use

Remaining implementation freedom is mainly exact geometry, not design direction.

## Did interpretation drift decrease?

**Dry-run verdict: YES — at the decision-ambiguity level.**

The candidate intake reduced the number of high-impact choices an agent must invent after reading the Human brief.

It also converted abstract intent such as `少し人の手触り` and `小綺麗にまとめすぎない` into reviewable rules without changing Content Authority or Foundation.

## What this does not prove

This result does not yet prove:

- actual DESIGN.md Maker JP output quality
- consistency across ChatGPT / Claude / Gemini
- repeated success across multiple design tasks
- Foundation Promotion readiness

## Next evidence needed

For a full Pilot conclusion, replace `external-style-candidate.md` with one real DESIGN.md Maker JP output and run the same normalization / conflict check once.

For stronger evidence, give the normalized candidate to at least two independent agents and compare the resulting design decisions against the same checklist.

## Gate conclusion

- Pilot use-1 dry run: **COMPLETE**
- Candidate intake usefulness: **SUPPORTED**
- DESIGN.md Maker-specific validation: **PENDING REAL OUTPUT**
- Human Direction Selection recommendation: **Route B**
- Human Direction Selection: **NOT CONSUMED**
- DESIGN-MD-INTAKE-PILOT-V1 Merge: **HOLD**
- Foundation / Pattern / Prompt Promotion: **HOLD**
