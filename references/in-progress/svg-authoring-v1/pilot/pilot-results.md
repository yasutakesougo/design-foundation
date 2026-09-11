# SVG-AUTHORING-V1 Pilot Results

## Pilot authority

```text
Implementation PR              = #106
Human-Ready implementation SHA = 60c0b2bf1d445613d9a1e53646415f98c8db8757
Human Pilot Evaluation Start   = GO / CONSUMED
Fixture policy                 = synthetic / isolated copy only
Existing SVG mutation          = NOT AUTHORIZED
Merge / Promotion              = HOLD
```

## Purpose

This pilot checks whether the SVG Authoring Skill improves agent behavior across three distinct failure classes without relying on a project-specific backend.

The fixtures are synthetic and isolated from existing Human-accepted assets.

Each case contains three panels:

```text
BEFORE = known failure
NAIVE  = plausible unconstrained cleanup that creates a regression
SKILL  = bounded edit following SVG-AUTHORING-V1
```

The NAIVE panel is not a claim about every unconstrained model run.
It is a control example showing the failure mode the Skill is intended to prevent.

## Case A — Semantic local edit

Fixture:

```text
pilot/case-a-semantic.svg
```

Pre-edit brief:

```text
Intended meaning       = person is writing on paper
Current failure        = pen floats above paper; writing contact is unclear
Responsible geometry   = forearm endpoint + pen segment
Minimum affected parts = forearm / hand proxy + pen
Protected parts        = head, torso, paper position and size
```

Observed behavior:

```text
BEFORE = writing relationship is ambiguous
NAIVE  = contact improves, but paper/body geometry also moves
SKILL  = protected head/body/paper remain unchanged; only writing relation changes
```

Evaluation:

```text
scope containment          = PASS
protected-part retention   = PASS
semantic retention         = PASS
editability                = PASS
review evidence clarity    = PASS
Case A                     = PASS
```

## Case B — Curve local edit

Fixture:

```text
pilot/case-b-curve.svg
```

Pre-edit brief:

```text
Target contour                  = two-segment organic contour
Observed defect                 = visible tangent handoff at the join
Protected endpoints / junction  = both outer endpoints + join position
Protected relationship          = overall left-low → center-valley → right-high contour character
```

Observed behavior:

```text
BEFORE = join changes direction abruptly
NAIVE  = curve is smooth but collapses the intended local contour into a generic arc
SKILL  = join controls change while endpoints and join position are retained
```

Evaluation:

```text
scope containment          = PASS
protected-part retention   = PASS
semantic retention         = PASS
editability                = PASS
review evidence clarity    = PASS
Case B                     = PASS
```

The pilot uses visual continuity as primary evidence.
No numeric smoothness metric is treated as authority.

## Case C — Structural edit

Fixture:

```text
pilot/case-c-structure.svg
```

Pre-edit brief:

```text
Intended meaning       = simple symbol with head / connector / base
Current failure        = anonymous nesting + fragmented connector paths reduce editability
Responsible structure  = exporter-like nested groups + fragmentation
Protected parts        = rendered geometry, style, semantic part boundaries
```

Observed behavior:

```text
BEFORE = nested anonymous groups and split connector paths
NAIVE  = all geometry is collapsed into one giant path
SKILL  = rendered geometry stays equivalent while semantic groups remain independently editable
```

Evaluation:

```text
scope containment          = PASS
protected-part retention   = PASS
semantic retention         = PASS
editability                = PASS
review evidence clarity    = PASS
Case C                     = PASS
```

## Cross-case result

```text
Case A semantic local edit = PASS
Case B curve local edit    = PASS
Case C structural edit     = PASS

scope containment          = PASS
protected-part retention   = PASS
semantic retention         = PASS
editability                = PASS
review evidence clarity    = PASS
```

The pilot supports the hypothesis that the Skill improves SVG editing discipline by forcing the agent to identify meaning, minimum affected geometry, and protected relationships before cleanup.

## Important limit

This pilot proves process coherence on controlled fixtures.
It does not prove universal SVG quality, production backend suitability, or successful Human Visual Acceptance for every asset.

The fixtures intentionally isolate one failure class at a time.

## Gate result

```text
Agent Pilot Evaluation       = PASS / 3 of 3
Pilot execution              = COMPLETE
Human Pilot Acceptance       = HOLD
Existing SVG mutation        = NOT AUTHORIZED
Production backend selection = HOLD
Merge / Promotion            = HOLD
```

Next step is a fresh read-only Pilot Evidence Review followed by a Human Pilot Acceptance decision.
