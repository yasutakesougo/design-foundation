# EYE-SCALE-CORRECTION-V1 — Implementation Record

## Authority

```text
Definition PR = #135
Definition HEAD = 1e3591ca9c10eea6187192b5dc2cec87f785d1ac
Human Definition / Scope Lock = GO / CONSUMED
Human Implementation Start = GO / CONSUMED
Authorized candidate start = fe037894ffad4eeb1e79dd6442214923afe8f3d5
```

## Exact implementation scope

```text
references/in-progress/image-first-semantic-redraw-v1/candidates/new-source-v1/person-thinking.svg
references/in-progress/image-first-semantic-redraw-v1/candidates/new-source-v1/person-looking.svg
references/in-progress/image-first-semantic-redraw-v1/candidates/new-source-v1/person-note-taking.svg
references/in-progress/image-first-semantic-redraw-v1/evidence/new-source-v1/eye-scale-correction-v1-implementation.md
```

No ACTIVE archive source bytes are modified.

No backend selection, consumer reference, promoted asset, dependency, CI, deploy, print, or publish path is changed.

## Method

Each identified eye-mark path is enlarged about its local center while keeping the global `stroke-width=8` monoline contract unchanged.

Target scale factor for this implementation candidate:

```text
eye path geometric span = 1.60x
stroke width = unchanged
non-eye path data = unchanged
```

The scale factor is an implementation candidate, not an HVA acceptance rule.

Human Visual Acceptance remains authoritative.

## Eye path changes

### THINK

```text
left/before  M 269.44 211.45 L 270.14 214.98
left/after   M 269.23 210.39 L 270.35 216.04

right/before M 341.57 201.55 L 342.28 206.5
right/after  M 341.36 200.07 L 342.49 207.99
```

### LOOK

```text
near/before M 254.59 195.18 L 257.41 200.84
near/after  M 253.74 193.48 L 258.26 202.54

far/before  M 311.87 173.26 C 312.85 176.35 313.93 178.86 315.4 181.75
far/after   M 310.81 170.71 C 312.38 175.66 314.11 179.67 316.46 184.30
```

The LOOK curve is expanded around the original endpoint midpoint so its directional character is retained.

### WRITE

```text
left/before  M 144.27 204.38 L 144.27 211.45
left/after   M 144.27 202.26 L 144.27 213.57

right/before M 208.62 193.77 L 210.03 198.72
right/after  M 208.20 192.29 L 210.45 200.21
```

## Protected invariants

```text
viewBox = 0 0 512 512
fill = none
stroke = currentColor
stroke-width = 8
stroke-linecap = round
stroke-linejoin = round
```

The implementation is intended to preserve all non-eye path geometry byte-for-byte at the SVG path-data level.

Protected semantic cues remain outside the correction target:

```text
THINK = hand ↔ face contact and visible forearm
LOOK = modest head turn, both eyes open, lateral gaze
WRITE = notepad, long diagonal pen, writing hand, pen ↔ paper contact
```

## Review requirements

Before any HVA PASS can be declared:

```text
1. Fresh implementation diff review
2. Confirm only intended eye path data + this evidence record changed
3. Confirm SVG structural contract remains valid
4. Produce / inspect 512px review render
5. Produce / inspect 64px practical-size render
6. Fresh Human Visual Acceptance on corrected candidate identities
```

## Current gate

```text
Human Implementation Start = GO / CONSUMED
Implementation candidate = CREATED
Fresh Implementation Review = PENDING
Human Visual Acceptance PASS = NOT DECLARED
Accepted SVG Materialization = HOLD
Merge / Promotion = HOLD
Deploy / Print / Publish = HOLD
```
