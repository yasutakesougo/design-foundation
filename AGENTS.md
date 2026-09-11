# Repository Agent Bootstrap

This file is the repository-level bootstrap pointer for agents that support `AGENTS.md` instruction discovery.

It is not a second Operating Foundation authority.

## Canonical Operating Foundation

Use the accepted repository authority at:

`references/accepted/agent-operating-foundation-v1/`

Read these first:

1. `references/accepted/agent-operating-foundation-v1/README.md`
2. `references/accepted/agent-operating-foundation-v1/operating-contract.md`
3. `references/accepted/agent-operating-foundation-v1/readback-contract.md`

Read these when applicable:

- `references/accepted/agent-operating-foundation-v1/applicability-model.md`
- `references/accepted/agent-operating-foundation-v1/refinement-routing.md`
- `references/accepted/agent-operating-foundation-v1/observability-boundary.md`

## Human authority and mutation boundary

Human GO comes only from explicit Human input.

Agent / Skill does not generate, infer, or proxy-consume Human GO.

Write / merge / publish / print / deploy / promotion require explicit authority for the corresponding action.

Missing, conflicting, or unavailable evidence remains `UNKNOWN / HOLD`.

## Bootstrap readback

Before changing repository state, reconstruct the target workstream from fresh evidence.

At minimum, identify:

- current `main` and the relevant branch or PR;
- canonical Definition and latest independent Review chain;
- consumed Human Gates;
- next unconsumed Human Gate;
- exact HEAD when mutation authority is SHA-bound;
- applicable CI status and conclusion when CI exists;
- unresolved findings, missing evidence, and `UNKNOWN` state.

Use `references/accepted/agent-operating-foundation-v1/readback-contract.md` for the detailed reconstruction contract.

## Runtime activation boundary

The presence of this file does not mean runtime activation is `ACTIVE`.

Merging this file does not mean runtime activation is `ACTIVE`.

`ACTIVE(runtime = X)` requires actual fresh-runtime bootstrap evidence for that runtime, independent runtime-evidence review, and explicit Human Activation GO.

Do not infer activation for runtimes whose repository instruction discovery was not actually observed.
