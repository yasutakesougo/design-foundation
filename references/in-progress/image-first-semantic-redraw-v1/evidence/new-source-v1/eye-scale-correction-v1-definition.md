# IMAGE-FIRST-SEMANTIC-REDRAW-V1 — EYE-SCALE-CORRECTION-V1 Definition / Scope

## Authority

```text
Parent lane = New Source Generation / Revalidation
Parent PR = #129
Authorized candidate HEAD = fe037894ffad4eeb1e79dd6442214923afe8f3d5
HVA package commit = e617fa5e27a60f6a8ea9141bf14abb44abe8c3ce
Human Visual Acceptance = CORRECTION
Human concern = 目が小さい
Definition / Scope = EYE-SCALE-CORRECTION-V1
```

## Trigger

Human Visual Acceptance of the new-source SOURCE-GUIDED candidates found eye marks too small.

Fresh visual readback confirmed:

```text
THINK / LOOK / WRITE = eyes render as very small dots / short dashes
512 face crops = concern confirmed
64px appearance = eye marks remain weak / easy to lose
ACTIVE source panels already use the same small eye marks
SOURCE-GUIDED preserved that source eye scale
```

This is therefore a **feature-scale / semantic eye enlargement** correction, not a backend-selection defect and not silent vectorizer drift away from source.

## Purpose

Enlarge THINK / LOOK / WRITE eye marks so they remain readable at 512px and practical at 64px, while preserving gesture contracts and the existing monoline SVG style contract.

```text
Smooth / scale the eye marks, not the meaning.
```

## Locked correction method

```text
primary method = candidate SVG eye-mark enlargement
ACTIVE archive source bytes = DO NOT MUTATE
backend selection = unchanged SOURCE-GUIDED
historical accepted SVG / HVA inheritance = PROHIBITED
```

Locked rationale:

```text
1. ACTIVE archival authority must remain exact-byte stable
2. The HVA defect is eye-scale readability, not gesture topology or backend choice
3. A narrow post-candidate eye-mark correction keeps non-eye geometry and provenance intact
4. Source redraw / re-archival is OUT unless a later Human gate explicitly reopens source identity
```

Implementation may identify eye marks by topology / local face-feature heuristics and/or explicit review metadata. Silent movement of non-eye protected geometry is forbidden.

## Protected geometry / semantics

Must remain intact:

```text
- THINK hand ↔ face contact and visible forearm
- LOOK modest head turn, both eyes open, lateral gaze, face direction supporting gaze
- WRITE notepad, long diagonal pen, writing hand, pen ↔ paper contact
- path topology outside corrected eye marks
- SVG style contract
```

Eye correction must not:

```text
- close LOOK eyes
- convert eyes into decorative marks unrelated to gaze
- enlarge nose / mouth / eyebrows as a side effect
- shift non-eye strokes to “make room” beyond the minimum needed for readable eye marks
```

## Eye-scale target

Corrected eye marks must satisfy all of:

```text
E1 Visible as intentional eye marks at 512px without relying on imagination
E2 Survive practical 64px reduction as detectable facial cues
E3 Remain smaller/simpler than major gesture cues (hand, pen, head turn)
E4 Stay paired / directional where LOOK requires lateral gaze
E5 Keep adult, quiet, monoline character — no cartoon oversizing, fills, or pupils-with-highlights
```

Exact pixel radius is not pre-locked. Implementation must record before/after metrics and review crops.

## SVG output contract

Unchanged:

```text
viewBox          = 0 0 512 512
fill             = none
stroke           = currentColor
stroke-width     = 8
stroke-linecap   = round
stroke-linejoin  = round
```

No raster embedding, filters, masks, clipPaths, gradients, or hard-coded paint colors.

## Acceptance model

```text
C1 Eye-scale readability improved for THINK / LOOK / WRITE
C2 Gesture contracts preserved
C3 Non-eye protected geometry preserved
C4 SVG style / validator PASS
C5 512px review PASS for eye visibility
C6 64px review PASS for practical eye cue retention
C7 Fresh Human Visual Acceptance required on corrected candidate identities
```

A gesture regression is overall FAIL even if eyes become larger.

## Implementation isolation

If Implementation Start is later authorized, create a separate correction branch / PR from exact authorized candidate HEAD:

```text
fe037894ffad4eeb1e79dd6442214923afe8f3d5
```

Authorized correction outputs are new candidate identities only. Expected narrow scope:

```text
references/in-progress/image-first-semantic-redraw-v1/candidates/new-source-v1/*.svg
references/in-progress/image-first-semantic-redraw-v1/evidence/new-source-v1/**
optional helper under scripts/ only if required for deterministic eye-mark correction / evidence
```

Exact file list must be re-declared at Human Implementation Start.

HVA package renders under `evidence/new-source-v1/hva-review/` may be superseded by correction review evidence; they are not acceptance authority.

## OUT / HOLD

```text
- mutating ACTIVE archive source bytes
- new source selection / re-archival
- changing production backend selection away from SOURCE-GUIDED
- historical accepted SVG SHA inheritance
- historical HVA inheritance
- existing HITOKOTO asset mutation
- consumer reference switching
- Accepted SVG Materialization
- Foundation / Pattern / promoted Prompt changes
- repository-wide dependency or CI changes
- Merge / Promotion
- Deploy / Print / Publish
```

## Current Gate

```text
EYE-SCALE-CORRECTION-V1 Definition / Scope = LOCKED
Fresh Definition / Scope Review = PASS
Human Definition / Scope Lock = GO / CONSUMED
Human Implementation Start = HOLD
Human Visual Acceptance = CORRECTION / awaiting corrected candidates
Accepted SVG Materialization = HOLD
Merge / Promotion = HOLD
```
