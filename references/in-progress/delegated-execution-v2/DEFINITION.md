# DELEGATED-EXECUTION-V2 — Definition / Scope

## Purpose

委任作業をHuman Gateごとに停止させず、承認済み境界の中では自律的に最後まで進めるためのRepository Operating Modeを定義する。

人間は工程遷移の許可ではなく、委任範囲・視覚的採否・本番反映を判断する。

このV2はaccepted Operating Foundationを置き換えない。workstreamに対して明示的なHuman Delegation Activation GOが消費されたときだけ適用する候補契約である。

## Fresh baseline

```text
Repository = yasutakesougo/design-foundation
main = b8e3e5d655008de189bb09f9096962883107336e
Accepted Operating Foundation = references/accepted/agent-operating-foundation-v1/
Root AGENTS.md = PRESENT
Runtime activation (Cursor Cloud Agents API / instruction discovery) = ACTIVE for observed runtimes with prior Activation evidence; do not infer for unobserved runtimes
Authority class for this candidate = references/in-progress/
Promotion = HOLD
Production / Deploy / External release = HOLD
```

## Human Delegation Activation GO — this workstream

```text
Workstream = DELEGATED-EXECUTION-V2
Human Delegation Activation GO = GO / CONSUMED
Source = explicit Human Cloud Agent task「委任実行プロセス」with DELEGATED-EXECUTION-V2 body
Observation = Cursor Cloud run bc-01a09169-7d2d-7262-b642-1a1f39cbc169
```

Approved mutation boundary for this Activation:

```text
IN
- materialize DELEGATED-EXECUTION-V2 under references/in-progress/delegated-execution-v2/
- create Implementation PR on branch cursor/delegated-execution-v2-c169
- record Definition / Independent Review / Correction / Implementation evidence in-repo and on the PR
- merge the in-progress candidate after Independent Reviews PASS and auto-continue conditions hold
- optional minimal discovery pointer under references/README.md or root README.md that does not rewrite accepted Operating Foundation contracts

OUT / HOLD
- references/accepted/** mutation or Promotion
- rewriting accepted Operating Foundation contract bodies
- foundations/* / patterns/* / prompts/* / review/* / skills/* content rewrite
- root AGENTS.md rewrite that changes Human Gate authority semantics
- CI / GitHub Actions mutation
- telemetry / tracing
- secret / credential mutation
- production deploy / external publish / print / irreversible external action
- automatic Human GO generation / inference / proxy consumption
- retrospective rewrite of unrelated open workstreams' gate state
```

This Activation authorizes autonomous progress inside the IN boundary through Ready / Merge for the in-progress candidate. It does not authorize Human Live GO actions.

## Core flow

```text
Human Delegation Activation GO
        ↓
Definition
        ↓
Independent Definition Review
        ↓
Correction Loop
        ↓
Implementation Scope
        ↓
Independent Scope Review
        ↓
Correction Loop
        ↓
Implementation
        ↓
Build / Test / CI
        ↓
Independent Implementation Review
        ↓
Correction Loop
        ↓
Rendered Evidence          (visual workstreams only)
        ↓
Agent Visual Review        (visual workstreams only)
        ↓
Visual Correction Loop     (visual workstreams only)
        ↓
Human Visual Acceptance    (visual workstreams only)
        ↓
Finalization
        ↓
Ready / Merge
        ↓
Human Live GO              (production / external release only)
        ↓
Production / External Release
```

## Auto-continue conditions

Within an active Human Delegation Activation boundary, stage transitions do not require additional Human GO when all of the following hold:

```text
P0 = 0
P1 = 0
Independent Review = PASS
Authority boundary = unchanged
Scope boundary = unchanged
Required evidence = observable
No production mutation
No secret / credential mutation
No irreversible external action
```

P2 findings may be recorded and carried forward.

## Automatic Correction

When Independent Review finds correctable defects inside the approved boundary:

```text
Review
↓
Finding
↓
Correction
↓
Fresh Re-Review
```

```text
MAX_CORRECTION_LOOPS = 3
```

Escalate to Human only when 3 loops do not reach PASS, or when a forced-stop condition applies.

## Standard Human Gates

Under DELEGATED-EXECUTION-V2, ordinary Human Gates are limited to:

1. Human Delegation Activation GO
2. Human Visual Acceptance GO — only when visual deliverables exist
3. Human Live GO — only when production / external release is required

Therefore:

```text
Internal document / Foundation candidate
→ 1 Human Gate

Visual deliverable
→ 2 Human Gates

Visual deliverable + production release
→ at most 3 Human Gates
```

## Abolished ordinary stop points

Inside an active Delegation Activation boundary, the following are not independent Human Gates:

```text
Human Definition / Scope Lock GO
Human Implementation Start GO
Human Ready GO
Human Merge GO
```

Their assurance is provided by the consumed Delegation Activation contract plus Independent Review PASS.

Outside an active Delegation Activation, existing Operating Foundation / workstream gate vocabulary remains unchanged.

## Visual evidence path

For UI / SVG / poster / print and similar visual artifacts, Implementation complete is not a Human stop.

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

Agent Visual Review must at least check:

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

Human Visual Acceptance retains only judgments that rules alone cannot decide (e.g. tone, candidate A/B choice, posting suitability). Technical defects and known rule violations must be cleared before that Gate.

After Human Visual Acceptance GO:

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

## Human Live GO

Required only for:

```text
本番Deploy
外部公開
実利用者への公開
不可逆な外部変更
Production data mutation
```

Not required for internal documents, Foundation / Pattern / Prompt candidates, or SVG authority that does not externally publish.

## Forced stop conditions

Stop autonomous progress when any of the following occurs:

```text
P0 >= 1 and not safely correctable inside boundary
P1 >= 1 and not safely correctable inside boundary
Review = HOLD / FAIL
Required evidence = UNKNOWN
Authority interpretation required
Authority boundary change required
Scope expansion required
Human judgment explicitly required
Production / external mutation required
Correction loop limit exceeded
```

UNKNOWN must not be treated as PASS.

Human Gates must not be inferred, generated, or substituted by Agent / Skill.

## Relationship to accepted Operating Foundation

```text
Preserved
- Human GO comes only from explicit Human input
- Agent / Skill does not generate / infer / proxy-consume Human GO
- UNKNOWN / HOLD fail-closed
- write / merge / publish / print / deploy / promotion require corresponding authority
- readback / applicability / refinement / observability contracts remain canonical

Added by this candidate
- workstream-scoped Delegation Activation mode
- reduced ordinary Human Gate set inside that mode
- automatic correction loop with hard limit
- visual evidence completion before Human Visual Acceptance
```

This candidate does not mutate `references/accepted/agent-operating-foundation-v1/*` in V2 Implementation.

Promotion to accepted authority is a separate later decision and is OUT for this Activation.

## Implementation deliverables

ADD under `references/in-progress/delegated-execution-v2/`:

```text
README.md
delegated-execution-contract.md
human-gate-model.md
correction-loop-contract.md
visual-evidence-path.md
compatibility.md
DEFINITION.md          (this locked Definition; retained as evidence)
```

Optional ADD/UPDATE (minimal pointer only, no contract rewrite):

```text
references/README.md
and/or root README.md
```

Exact optional pointer text is fixed in Implementation Scope after Independent Definition Review PASS.

## Explicit non-goals

```text
accepted Operating Foundation rewrite
Promotion to references/accepted/
patterns/flyer.md or root README basic-flow replacement beyond optional pointer
CI enforcement of Delegation Activation
automatic reviewer spawning platform
runtime daemon / telemetry
secret management changes
Deploy / Print / Publish / Live mutation
rewriting unrelated workstream Issues to V2 gates
```

## Acceptance criteria

1. DELEGATED-EXECUTION-V2 is materializable as an in-progress candidate without weakening Human GO authority.
2. The three standard Human Gates and abolished ordinary stop points are explicit.
3. Auto-continue and forced-stop conditions are fail-closed and do not treat UNKNOWN as PASS.
4. Correction loops are capped at 3 and escalate thereafter.
5. Visual workstreams reach Human Visual Acceptance only after Agent Visual Review and technical clearance.
6. Human Live GO remains mandatory for production / external release.
7. Compatibility with accepted Operating Foundation is documented without rewriting accepted files.
8. This workstream's Activation boundary (IN/OUT) is reconstructible from repository evidence.
9. Implementation remains limited to the authorized paths.
10. Independent Reviews are required at Definition, Scope, and Implementation stages before Ready / Merge.

## Independent Definition Review questions

1. Does this Definition expand authority beyond the consumed Human Delegation Activation GO?
2. Does abolishing ordinary stop points create a path to infer Human GO?
3. Is compatibility with accepted Operating Foundation fail-closed enough?
4. Are visual and Live gates preserved where required?
5. Are OUT items sufficient to prevent accepted-authority or production mutation?
6. Is optional README pointer scope left too ambiguous?
7. Are auto-continue conditions missing required evidence bindings (exact HEAD / CI)?
8. Does merge-without-Human-Merge-GO conflict with still-accepted Operating Foundation vocabulary in a way that must HOLD until Promotion?

## Current gate state

```text
Human Delegation Activation GO = GO / CONSUMED
Definition                     = DEFINED
Independent Definition Review  = REQUIRED
Implementation Scope           = NOT YET LOCKED
Implementation                 = HOLD until Definition Review PASS + Scope Review PASS
Human Visual Acceptance        = NOT APPLICABLE (non-visual candidate)
Human Live GO                  = NOT REQUIRED for this candidate
Promotion                      = HOLD
```

## Permitted next action

```text
Independent Definition Review on this DEFINITION.md
```
