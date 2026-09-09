# Fixture Correction V1 — Implementation Evidence

## Authority

```text
Parent Pilot                  = SEMANTIC-VECTORIZATION-PILOT-V1
Definition                    = Issue #82
Fresh Definition Review       = Issue #83 / PASS
Human Definition / Scope Lock = GO / CONSUMED
Human Implementation Start    = GO / CONSUMED
Parent PR                     = #78 @ a6054946cde471205894e4726ce07e73d6fa18d0
Correction scope              = WRITE / LOOK only
```

This correction is intentionally isolated from PR #78.

The existing Pilot fixture files under `fixtures/source-svg/` are not changed in this slice.

Corrected files are candidates only and must not be treated as an automatic re-pin.

## Candidate files

```text
WRITE
fixture baseline blob = 9edda32fc6b96ca5226ba7f3922b30a2cd52c526
baseline paths        = 32
candidate path        = fixture-correction-v1/candidates/person-note-taking.svg
candidate Git blob    = c3c7ddf75d6ce56202bbfd05053f2595fdb66f95
candidate SHA-256     = 74bb9824399e41dacc11fe9a9033c4b0e47e504fe1f679a15315942d63a34280
candidate paths       = 31

LOOK
fixture baseline blob = 918f9ea48cbb2778d2f3dd8ba1051158ee1fd52b
baseline paths        = 29
candidate path        = fixture-correction-v1/candidates/person-looking.svg
candidate Git blob    = 7c8370b28571c76a9f24a87ff03123e79af5e428
candidate SHA-256     = c41b3ff0afd107f707e5ab4238b144999e152bd56b8a9d9039e6fd2017f90613
candidate paths       = 31
```

## Scope verification

THINK remains the inherited Pilot source fixture and was not edited.

```text
THINK blob = 8700cc1ccf679f7e4f43dcc93a0f222a088af1e9
```

No AutoTrace, skeleton, VLM, Foundation, Pattern, Prompt, CI, package, lockfile, or production asset is changed by this correction.

## WRITE correction

The correction changes the action zone rather than redrawing the whole figure.

```text
paper
- moved slightly lower to create separation between torso, hand, and writing action
- remains a single simple outlined sheet

pen
- one long diagonal axis
- detached from shoulder contour
- short rear-cap mark retained
- pen tip extends to the paper surface

writing hand
- small hand loop sits around the pen axis
- forearm approaches the hand but does not become the pen itself
```

Semantic pre-check:

```text
paper               = CLEAR
elongated pen       = CLEAR CANDIDATE
writing hand        = PRESENT
pen-hand relation   = PRESENT
pen-paper contact   = PRESENT
active writing read = READY FOR HUMAN REVIEW
```

This is not a consumed Human Semantic Gesture PASS.

## LOOK correction

The correction keeps the existing modest head turn and changes the eye/face cues.

```text
eyes
- both eyes use visible upper and lower contours
- both remain open rather than wink/closed-eye arcs
- gaze marks are displaced toward the same lateral side

face
- nose is shifted further with the existing head turn
- mouth placement follows the same directional construction
- shoulder asymmetry remains supporting evidence only
```

Semantic pre-check:

```text
non-frontal head    = CLEAR
face direction      = CLEAR CANDIDATE
both eyes open      = CLEAR CANDIDATE
lateral gaze        = PRESENT / SAME DIRECTION
LOOK read           = READY FOR HUMAN REVIEW
```

This is not a consumed Human Semantic Gesture PASS.

## Static evaluation

The Pilot static evaluator contract was applied to both candidate structures.

```text
WRITE
G1 SVG VALID          = PASS
G2 STYLE VALID        = PASS
path_count            = 31
segment_token_count   = 40
very_short_path_count = 2
transform_count       = 0
anonymous_group_count = 1

LOOK
G1 SVG VALID          = PASS
G2 STYLE VALID        = PASS
path_count            = 31
segment_token_count   = 36
very_short_path_count = 2
transform_count       = 0
anonymous_group_count = 1
```

The one anonymous group is the same simple inherited style-wrapper pattern used by the baseline fixtures; no nested exporter-only group structure was introduced.

## Style contract

Both candidates preserve:

```text
viewBox          = 0 0 512 512
fill             = none
stroke           = currentColor
stroke-width     = 8
stroke-linecap   = round
stroke-linejoin  = round
```

No raster embedding, filter, mask, clipPath, gradient, transform, or hard-coded paint color is present.

## Render evidence

Local deterministic review renders were generated with Inkscape 1.4 at 512px and 64px.

```text
WRITE corrected 512 SHA-256 = 4885d4e6526f7298482f535c960fa55f7d205f4b8cd23aee13c98fcd6a463ec4
WRITE corrected  64 SHA-256 = d56138622a51083ee5be32a1278438796d78f769224a90454514fd857cb7edac
LOOK corrected  512 SHA-256 = 5594cc8b254c5820692ddeaba7800ff1fcefb3585caca448bd80d7aedb453fc6
LOOK corrected   64 SHA-256 = 354bfae320f9477a919522bf334633ca3d2ea8bb13047566becfaf756aa4ef69
```

Human review contact sheets were also generated for baseline/corrected comparison at both scales.

The binary render files are execution evidence and are not committed through this text-only correction PR.

## Implementation-gate status

```text
F1 Scope                       = PASS / WRITE + LOOK only
F2 Style                       = PASS
F3 Structural editability      = PASS CANDIDATE / no material fragmentation regression
F4 WRITE semantic adequacy     = READY FOR HUMAN REVIEW
F5 LOOK semantic adequacy      = READY FOR HUMAN REVIEW
F6 Ambiguity rejection         = REQUIRES HUMAN

Human Ready                    = HOLD
Human Semantic Gesture Review  = NOT CONSUMED for corrected candidates
Backend selection              = HOLD
PR #78 re-pin                  = NOT AUTHORIZED
PR #78 Merge                   = HOLD
Foundation / Promotion         = HOLD
```

The next step is Fresh Implementation / Semantic Review of this correction PR, followed by a Human Ready decision. No candidate becomes the Pilot fixture automatically.
