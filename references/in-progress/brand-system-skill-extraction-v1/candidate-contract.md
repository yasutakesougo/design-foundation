# BRAND-SYSTEM-SKILL-EXTRACTION-V1 — Candidate Contract

## Provenance

This contract is an extraction / adaptation materially derived from reusable process ideas in:

```text
Repository = amirmushichge/brand-system-skill
Pinned source commit = 30f6084ddf6adf4173cf882fce266015f8872c17
Source author = Amir Mushich
Source license = CC-BY-4.0
Source version = 0.2.0-alpha
```

This local contract is provider-neutral and does not vendor or activate the external Skill.

## Authority

```text
Lifecycle Issue = #232
Canonical Definition = BSSEV1-DEF-002
Definition Lock = GO / CONSUMED / COMPLETE
Implementation Scope = BSSEV1-SCOPE-001
Implementation Start = GO / CONSUMED / COMPLETE
Candidate status = IN-PROGRESS / NOT PROMOTED
```

This contract is project-level candidate guidance only.

Existing Foundation / Pattern / Review / Accepted authority wins on conflict.

## C1 — Reference Role

Every visual reference used for generation or correction must have an explicit permitted role and explicit non-role.

Record at minimum:

```text
Reference
Permitted influence
Prohibited influence
Project / stage
Status
```

A reference may not silently gain authority outside its declared role because it is newer, visually attractive, easier to use, or already present in the repository.

Example boundary:

```text
Scene reference
MAY control:
- composition family
- camera / distance class
- lighting direction
- material / texture category
- broad mood

MUST NOT control:
- project identity
- approved typography
- approved logo
- approved color system
- accepted asset identity
```

Existing `Borrow / Do Not Copy` remains the upstream reference-intake contract.

## C2 — Current Project Anchor

A `Current Project Anchor` is a project-local working reference selected through the existing project `Design Direction / Human Direction Selection` process.

It may guide later drafts and variants inside the same project.

It creates no new repository authority and no new Human Gate.

```text
Current Project Anchor
!= Human Visual Acceptance
!= Human Output GO
!= Accepted Reference
!= Foundation authority
!= Pattern authority
!= runtime activation
!= permission for unrelated repository mutation
```

If explicit Human Direction Selection evidence is absent or ambiguous:

```text
Current Project Anchor = NOT SET / HOLD
```

## C3 — Correction Classification

Before correcting a failed output, classify the defect.

### REFINE

Use `REFINE` when the core direction remains valid and the defect is localized.

Typical signals include:

```text
- spacing defect
- local hierarchy defect
- one illustration proportion issue
- one misplaced CTA
- isolated typography sizing issue within an otherwise approved direction
- local crop / alignment / detail error
```

A REFINE instruction must identify the bounded correction and the `PRESERVE` set.

### REJECT / RESTART

Use `REJECT / RESTART` when the defect changes or invalidates the foundational direction.

Typical signals include material failure in one or more of:

```text
- overall design direction
- typography system
- color logic
- material / illustration language
- hierarchy architecture
- photography / scene language
- audience fit
- product / information architecture
```

Do not blend a rejected foundational direction into the replacement merely because some generated artifact already exists.

Classification does not bypass any required Human review.

## C4 — Rejected Reference Isolation

An artifact explicitly rejected as a direction is excluded from later visual-generation inputs by default.

Only abstract decisions explicitly listed for preservation may carry forward automatically.

A rejected visual artifact may be reused as a generation reference only after an explicit Human project decision names its bounded new reference role.

The following cannot re-authorize a rejected reference:

```text
agent review
consistency score
implementation convenience
chronological recency
file placement
repository presence
```

Re-authorization is a project-level working decision only.

It does not imply Human Visual Acceptance, Human Output GO, Accepted status, Promotion, runtime activation, Deploy, Print, or Publish.

## C5 — Preserve Contract

Every correction instruction should state both what changes and what remains stable.

Minimum shape:

```text
CHANGE / CORRECT
- ...

PRESERVE
- ...
```

`PRESERVE` should contain only elements that are already successful and relevant to the correction.

Do not preserve an element merely because it appeared in an earlier output.

If the direction has been `REJECT / RESTART`, only abstract decisions explicitly retained by the project may enter the new `PRESERVE` set.

## C6 — Representative-case Before Scale

Before expanding one generated direction across many assets, variants, scenes, or formats, validate one representative case first.

The representative case should exercise the important locked rules for the planned expansion.

Scaling remains HOLD until the representative case satisfies:

```text
applicable consistency checks
required project review
required Human review where applicable
```

A representative-case PASS does not consume Human Visual Acceptance or Human Output GO for other assets.

It establishes only that scaling may be considered under the applicable project authority.

## Candidate consistency check

Before a project scales or corrects under this candidate, review:

```text
1. Are all active references role-bounded?
2. Is a Current Project Anchor explicitly set through existing Human Direction Selection?
3. Is the defect REFINE or REJECT / RESTART?
4. Are rejected artifacts excluded unless Human re-authorized with a bounded role?
5. Does the correction state both CHANGE and PRESERVE?
6. Has one representative case been checked before scale?
7. Are existing Foundation / Pattern / Review rules still controlling?
8. Is any Human Gate being inferred? If yes => HOLD.
```

## Promotion boundary

This candidate must accumulate real operational evidence before Promotion is even proposed.

A later Promotion Definition must set its own evidence-sufficiency criteria.

Neither elapsed time, repository age, implementation completion, nor one successful project is sufficient by itself.

Until an explicit future Promotion process completes:

```text
Foundation = NO
Pattern = NO
Prompt = NO
Skill = NO
Accepted authority = NO
Runtime authority = NO
```
