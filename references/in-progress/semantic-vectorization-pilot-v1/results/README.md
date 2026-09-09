# Baseline Evidence

## Execution context

This file records the first local implementation run after Human Implementation Start GO.

No dependency was installed for this run.

```text
Fixture source HEAD = 4acdefca152dd3f4fd1c69424b3f4f79f9b78004
Python              = 3.13.5
Inkscape            = 1.4
NumPy               = 2.3.5
scikit-image        = 0.26.0
Pillow              = 12.3.0
AutoTrace           = NOT INSTALLED / SKIP
```

The executable environment is evidence only.

It is not added to repository dependency files by this Pilot.

## Fixture validation

`validate_fixture.py` was run against the pinned copies.

```text
Overall     = PASS
note-taking = PASS / 32 paths / blob match
thinking    = PASS / 36 paths / blob match
looking     = PASS / 29 paths / blob match
```

Pinned source blob SHAs matched all three copied SVG files.

## SVG normalization smoke test

The normalizer was run against the note-taking fixture as a structural smoke test.

```text
XML / SVG parse = PASS
output paths    = 32
viewBox         = 0 0 512 512
fill            = none
stroke          = currentColor
stroke-width    = 8
linecap / join  = round
```

The static evaluator returned:

```text
G1 SVG VALID   = PASS
G2 STYLE VALID = PASS
G3 STRUCTURE   = REQUIRES_HUMAN
G4 VISUAL      = NOT_MEASURED in isolated normalizer smoke test
G5 SEMANTIC    = REQUIRES_HUMAN
Overall        = INCOMPLETE
```

This is expected because static validation does not consume Human review gates.

## Skeleton / polyline baseline

The baseline runner used deterministic Inkscape rasterization at 512px and 64px.

The `raw-denoise` skeleton variant produced the following first-pass evidence.

| Fixture | Source paths | Candidate paths | SSIM 512 | SSIM 64 |
| --- | ---: | ---: | ---: | ---: |
| note-taking / WRITE | 32 | 125 | 0.9514 | 0.9864 |
| thinking / THINK | 36 | 98 | 0.9444 | 0.9681 |
| looking / LOOK | 29 | 99 | 0.9518 | 0.9813 |

The `light-open-close` and `morphology-variant` candidates were also generated.

Their visual scores remained close to the raw-denoise baseline, but they did not solve the structural fragmentation problem.

## First implementation finding

The skeleton/polyline baseline preserves the broad raster appearance well enough to be useful as a centerline experiment.

However, it currently expands the original 29–36 path drawings into roughly 98–125 paths.

This is a material editability warning.

The current simple 8-neighbour graph tracing splits many small skeleton junctions into separate paths.

Therefore:

```text
Visual similarity = promising baseline evidence
Editability        = not yet acceptable as a default
Semantic cues      = requires Human review
Default backend    = NOT SELECTED
```

No smoothing or path merging is allowed to hide this fragmentation without a later structural check.

## AutoTrace baseline status

The local execution environment did not contain the `autotrace` executable.

The runner therefore reported:

```text
Backend A = autotrace-centerline
Execution = SKIP
Reason    = executable not found; dependency installation is outside current Pilot authority
```

The runner did not silently replace AutoTrace with another engine.

Because Backend A is not yet measured, the required two-backend comparison is incomplete.

No backend winner may be declared at this stage.

## Current evidence verdict

```text
fixture pin / integrity        = PASS
normalizer smoke               = PASS
static evaluator               = PASS for implemented checks
skeleton backend execution     = PASS
skeleton visual evidence       = GENERATED
skeleton structural quality    = WARNING / fragmented
AutoTrace execution            = SKIP / dependency unavailable
2-backend comparison           = INCOMPLETE
Semantic Gesture Check         = REQUIRES_HUMAN
Human Visual Acceptance        = NOT CONSUMED
```

The implementation is suitable for Fresh Implementation / Scope Review.

It is not yet sufficient for backend selection or promotion.
