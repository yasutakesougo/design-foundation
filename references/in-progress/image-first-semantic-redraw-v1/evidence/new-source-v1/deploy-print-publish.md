# EYE-SCALE-CORRECTION-V1 — Deploy / Print / Publish

## Gate

```text
Human Deploy / Print / Publish GO = GO / CONSUMED / COMPLETE
ACTIVE SVG authority = references/accepted/image-first-semantic-redraw-v1/assets/new-source-v1/person-*.svg
HVA authority = 0362b1720649288db8bb4072bb9fefdba48e5363
materialized commit = 4c2ed6f37961c9b2b23dc61f9c103e7902988512
Main promotion = GO / CONSUMED / COMPLETE (PR #144)
```

## What this GO authorizes

```text
Print / publish use of the ACTIVE IMAGE-FIRST new-source-v1 SVG identities
at references/accepted/image-first-semantic-redraw-v1/assets/new-source-v1/
```

Current pointer: `references/accepted/image-first-semantic-redraw-v1/active-authority.json`

Historical location at the original gate was `references/in-progress/image-first-semantic-redraw-v1/assets/accepted/new-source-v1/`.
That historical path is not current authority.

## Identities (unchanged; must remain MATCH @ 0362b17)

```text
THINK = 01f5d64396eb7c9569ad430f1b4ed0a96d03b0a428bf0531535e93bd2f3ad8cc
LOOK  = a96844e2bdf822a6e6b257c6c19b2424d7a55a92f8482d3902b32e87e4685e96
WRITE = 12fd790ec61f76e53811656a744f34522dff28515bc93648a6115bc60c1d86c7
```

## Explicitly NOT authorized by this GO

```text
HITOKOTO examples/person-*.svg mutation or replacement = NOT AUTHORIZED / PRESERVE
consumer / UI / poster / runtime reference switching = NOT AUTHORIZED
historical #114 assets/accepted/person-*.svg materialization = HOLD / ABSENT
candidates/new-source-v1/* mutation = HOLD
ACTIVE archive source PNG mutation = NONE
Foundation / Pattern / Prompt promotion = HOLD
HITOKOTO poster Real Trial / Hosting Deploy / Print-Post = separate gate
full stacked-base merge into main = NOT DONE
```

## Scope note

This gate authorizes Deploy / Print / Publish for the already-ACTIVE IMAGE-FIRST SVG authority.
The later consistency correction changes only the repository authority location and path-bearing metadata.
It does not change SVG bytes and does not switch HITOKOTO or other consumers.

## Post-merge readback

```text
PR #145 = MERGED
authorized PR head = dfbc3caad25d6bbebda0410d6f44a86767ae0fd8
merge commit / main tip = 426bf9481c26dbf83086c4146ba212d3d4a14c8b
accepted SVG SHA-256 = MATCH @ 0362b17 (3/3)
SVG bytes mutated by this gate = NONE
HITOKOTO / consumer switching = NOT AUTHORIZED / PRESERVE
historical #114 root = ABSENT
ACTIVE archive PNG = UNCHANGED
```
