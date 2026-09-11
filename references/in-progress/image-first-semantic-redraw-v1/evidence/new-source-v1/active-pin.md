# EYE-SCALE-CORRECTION-V1 — Human ACTIVE Pin

## Gate

```text
Human ACTIVE Pin GO = GO / CONSUMED
PR = #143
Authorized pin-content HEAD = 9271cb3d09f719c3529eef5eaacd6f4cef2860fa
Current PR tip = 3692b43be638ac243a2d8c5a6d04b6017cc88510
authority (HVA) = 0362b1720649288db8bb4072bb9fefdba48e5363
materialized commit = 4c2ed6f37961c9b2b23dc61f9c103e7902988512
ACTIVE SVG authority = assets/accepted/new-source-v1/person-*.svg
```

## What this pin does

Points the already-materialized accepted SVG identities as the **ACTIVE SVG authority** for this lane:

```text
assets/accepted/new-source-v1/person-thinking.svg
assets/accepted/new-source-v1/person-looking.svg
assets/accepted/new-source-v1/person-note-taking.svg
```

Pointer record: `assets/accepted/new-source-v1/active-authority.json`

## Identities (must match HVA PASS @ 0362b17)

```text
THINK = 01f5d64396eb7c9569ad430f1b4ed0a96d03b0a428bf0531535e93bd2f3ad8cc
LOOK  = a96844e2bdf822a6e6b257c6c19b2424d7a55a92f8482d3902b32e87e4685e96
WRITE = 12fd790ec61f76e53811656a744f34522dff28515bc93648a6115bc60c1d86c7
```

## Scope boundary

```text
Historical accepted (#114) mutation = HOLD / NOT MUTATED
candidate SVG mutation              = HOLD / NOT MUTATED
ACTIVE archive source PNG mutation  = NONE
Human Merge / Promotion GO          = GO / CONSUMED
Deploy / Print / Publish            = HOLD
```

## Readback

```text
PR #143 = OPEN / Draft
base = work/image-first-new-source-generation-revalidation-v1
diff = pointer + evidence only (no SVG/PNG byte mutations)
accepted SVG SHA-256 = MATCH @ 0362b17 (3/3)
ACTIVE archive PNG blob vs main = MATCH
historical assets/accepted/person-*.svg = ABSENT (not mutated)
```

## Merge / Promotion

```text
Human Merge / Promotion GO = GO / CONSUMED
PR = #143
Authorized PR head = 3692b43be638ac243a2d8c5a6d04b6017cc88510
Merge target / base = work/image-first-new-source-generation-revalidation-v1
Deploy / Print / Publish = HOLD
main / default-branch promotion = NOT IMPLIED
```
