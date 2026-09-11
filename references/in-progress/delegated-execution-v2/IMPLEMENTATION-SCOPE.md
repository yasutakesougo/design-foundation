# DELEGATED-EXECUTION-V2 — Implementation Scope

## Authority binding

```text
Workstream = DELEGATED-EXECUTION-V2
Canonical Definition = references/in-progress/delegated-execution-v2/DEFINITION.md
Definition-Content-SHA256 = 8d43a862b058ef0e1a97602608c061b201501403d72485b148913673290e476d
Definition Reviewed-SHA = a198de8e903075f507e8fb29bbc7610659726d7a
Independent Definition Re-Review-2 = PASS / evidence/definition-ir2.md
Human Delegation Activation GO = GO / CONSUMED
Implementation-PR = #227
Branch = cursor/delegated-execution-v2-c169
Baseline main = b8e3e5d655008de189bb09f9096962883107336e
```

## Purpose of this Scope

Fix the exact files and non-goals for Implementation after Definition PASS.

This Scope does not mint Human Ready / Merge GO. Ready / Merge remain authorized only by the consumed Human Delegation Activation GO whose IN includes merge of this in-progress candidate, after later Independent Implementation Review PASS and auto-continue conditions.

## Authorized path mutations

### ADD (required)

```text
references/in-progress/delegated-execution-v2/README.md
references/in-progress/delegated-execution-v2/delegated-execution-contract.md
references/in-progress/delegated-execution-v2/human-gate-model.md
references/in-progress/delegated-execution-v2/correction-loop-contract.md
references/in-progress/delegated-execution-v2/visual-evidence-path.md
references/in-progress/delegated-execution-v2/compatibility.md
```

### KEEP / UPDATE as evidence (already present)

```text
references/in-progress/delegated-execution-v2/DEFINITION.md
references/in-progress/delegated-execution-v2/evidence/definition-ir1.md
references/in-progress/delegated-execution-v2/evidence/definition-ir2.md
references/in-progress/delegated-execution-v2/evidence/scope-ir*.md   (to be added by reviews)
references/in-progress/delegated-execution-v2/evidence/impl-ir*.md    (to be added by reviews)
references/in-progress/delegated-execution-v2/IMPLEMENTATION-SCOPE.md (this file)
```

### Optional discovery pointer (IN, bounded)

ADD exactly one short paragraph to `references/README.md` only:

```markdown
## Delegated execution candidate

委任実行の候補契約は `in-progress/delegated-execution-v2/` にあります。

このパスは in-progress candidate であり、accepted authority ではありません。
```

```text
Pointer target = references/README.md only
Root README.md = UNCHANGED in this Implementation
Must not replace basic-flow / gate vocabulary sections
Must not imply Promotion or accepted Operating Foundation amendment
```

## Document content requirements

### README.md

- Status block: authority class, Activation consumed, Promotion HOLD, Visual N/A, Live not required
- Pointers to the five contract files + DEFINITION.md + evidence/
- Explicit: candidate ≠ accepted authority; Review PASS ≠ Human GO

### delegated-execution-contract.md

- Core flow
- Auto-continue conditions including Reviewed-HEAD / applicable CI binding
- Required evidence minimum
- Forced stop conditions
- MAX_CORRECTION_LOOPS reference
- Non-goals / production boundary

### human-gate-model.md

- Three standard Human Gates only
- Abolished ordinary stop points
- Authority source for Ready / Merge (Activation sole Human authority; Review PASS = condition)
- Case matrix: internal / visual / visual+live

### correction-loop-contract.md

- Review → Finding → Correction → Fresh Re-Review
- MAX_CORRECTION_LOOPS = 3
- Escalation rule
- P2 carry-forward

### visual-evidence-path.md

- Render → Desktop / Mobile / Print evidence → Agent Visual Review → Visual Correction → Human Visual Acceptance
- Agent Visual Review checklist
- Post-acceptance fixed asset / SHA / HEAD path
- N/A rule for non-visual workstreams

### compatibility.md

- Preserved accepted Operating Foundation invariants
- Pre-Promotion vocabulary rule
- Outside Activation: existing gates unchanged
- Candidate must not be cited as accepted merge authority for unrelated workstreams
- No accepted/* mutation in this V2 Implementation

## Explicit UNCHANGED / OUT

```text
references/accepted/**
foundations/**
patterns/**
prompts/**
review/**
skills/**
root README.md
root AGENTS.md
.github/**
CI / Actions
telemetry
secrets / credentials
Deploy / Print / Publish / Live mutation
unrelated workstream Issue/PR gate rewrites
```

## Acceptance criteria for Implementation

1. All required ADD paths exist and match Definition semantics (Correction-1 included).
2. Optional pointer matches the exact paragraph above and only touches `references/README.md`.
3. No OUT path is modified.
4. Documents do not instruct Agent/Skill to generate/infer/proxy-consume Human GO.
5. UNKNOWN ≠ PASS and HEAD/CI bindings remain visible.
6. Evidence files for Definition IR1/IR2 remain readable.
7. README status remains reconstructible without conversation history.

## Independent Scope Review questions

1. Does any required deliverable expand beyond Definition IN?
2. Is the optional pointer exactly bounded and non-rewriting?
3. Are Ready/Merge authority semantics preserved (Activation sole Human authority)?
4. Are accepted OF / AGENTS.md / patterns left untouched as required?
5. Is evidence retention sufficient for readback?
6. Any ambiguity that would force Authority interpretation / Scope expansion mid-implementation?

## Current gate state

```text
Human Delegation Activation GO     = GO / CONSUMED
Independent Definition Re-Review-2 = PASS
Implementation Scope               = DEFINED
Independent Scope Review           = REQUIRED
Implementation                     = HOLD
Human Visual Acceptance            = N/A
Human Live GO                      = NOT REQUIRED
Promotion                          = HOLD
```

## Permitted next action

```text
Independent Implementation Scope Review on this IMPLEMENTATION-SCOPE.md
bound to the locked Definition-Content-SHA256 above
```
