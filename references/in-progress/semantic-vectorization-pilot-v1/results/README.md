# Baseline Evidence

## Fixed fixture source

```text
Fixture source PR   = #71
Fixture source HEAD = 4acdefca152dd3f4fd1c69424b3f4f79f9b78004
note-taking blob    = 9edda32fc6b96ca5226ba7f3922b30a2cd52c526
thinking blob       = 8700cc1ccf679f7e4f43dcc93a0f222a088af1e9
looking blob        = 918f9ea48cbb2778d2f3dd8ba1051158ee1fd52b
```

`validate_fixture.py` reproduced all three pinned Git blob SHAs.

```text
Fixture integrity = PASS / all 3
note-taking       = 32 source paths
thinking          = 36 source paths
looking           = 29 source paths
```

The original source SVGs were not mutated.

## Shared execution environment

The same deterministic raster and evaluation path was used for both backends.

```text
Python       = 3.13.5
Inkscape     = 1.4
NumPy        = 2.3.5
scikit-image = 0.26.0
Pillow       = 12.3.0
Raster sizes = 512px / 64px
```

The normalizer enforces:

```text
viewBox          = 0 0 512 512
fill             = none
stroke           = currentColor
stroke-width     = 8
stroke-linecap   = round
stroke-linejoin  = round
```

## Initial skeleton / polyline baseline

The first run was completed before AutoTrace provisioning.

| Fixture | Source paths | Skeleton paths | SSIM 512 | SSIM 64 |
| --- | ---: | ---: | ---: | ---: |
| note-taking / WRITE | 32 | 125 | 0.9514 | 0.9864 |
| thinking / THINK | 36 | 98 | 0.9444 | 0.9681 |
| looking / LOOK | 29 | 99 | 0.9518 | 0.9813 |

`light-open-close` and `morphology-variant` were also executed.

They did not materially solve the structural fragmentation problem.

```text
Skeleton visual similarity = promising
Skeleton editability        = WARNING / fragmented
Default backend             = NOT SELECTED
```

## AutoTrace Local Dependency Provision

Human authority:

```text
SEMANTIC-VECTORIZATION-PILOT-V1
AutoTrace Local Dependency Provision GO
— PR #78 @ 138370a73126361481bb2d33815239103af7f6c3
```

The runtime had no direct outbound package-download path.

A non-expired upstream PyAutoTrace GitHub Actions wheel artifact was therefore retrieved through the GitHub connector and installed only into an isolated temporary local target.

```text
Upstream repository = lemonyte/pyautotrace
CI run              = 34120876256
CI head             = 2b7ad73889c632f4a558ff1774dc72e335ef5244
Artifact id         = 10018337990
Artifact name       = wheels
Artifact digest     = sha256:080ddfbc72ce1f577e4d070c3533c61cf1f5cedab7ee0b785c4cf4b418add496
Package             = pyautotrace 0.0.7
Wheel               = pyautotrace-0.0.7-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl
Wheel SHA-256        = 1f1ad4825175b91e277c1c39402b33ff76ef3253a10884f55e1fccf8e3f4c397
Install scope        = /tmp isolated target only
Repository deps     = unchanged
CI files            = unchanged
System packages     = unchanged
```

The current upstream `.gitmodules` still pins the bundled AutoTrace source to commit prefix `c250135`.

The Pilot runner expects the classic AutoTrace command shape.

A temporary local compatibility wrapper translated that command into PyAutoTrace `Bitmap.trace(centerline=True)`.

The wrapper also supplied white as the background color because the deterministic Pilot raster uses a white background.

No wrapper file was added to the repository.

## Two-backend comparison

The existing `run_baseline.py` was rerun without changing fixture input or evaluation logic.

Overall runner status:

```text
EVIDENCE_READY
```

### AutoTrace centerline vs skeleton/raw-denoise

| Fixture | Source paths | AutoTrace paths | AutoTrace SSIM 512 | AutoTrace SSIM 64 | Skeleton paths | Skeleton SSIM 512 | Skeleton SSIM 64 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| note-taking / WRITE | 32 | 174 | 0.9205 | 0.9387 | 125 | 0.9514 | 0.9864 |
| thinking / THINK | 36 | 95 | 0.9229 | 0.9384 | 98 | 0.9444 | 0.9681 |
| looking / LOOK | 29 | 128 | 0.9274 | 0.9386 | 99 | 0.9518 | 0.9813 |

Both required centerline lanes now executed against the same three fixed fixtures.

The former evidence blocker `B1 / AutoTrace not executed` is resolved.

## Interpretation

The AutoTrace baseline is valid evidence, but it is not a default-backend recommendation.

After the shared normalization contract is applied, AutoTrace produces 95–174 paths for source drawings containing 29–36 paths.

The rendered output also shows visible endpoint / junction bead artifacts in the current normalized stroke style.

The skeleton baseline has higher SSIM on all three fixtures and looks cleaner in this first comparison, but it still produces 98–125 paths and remains structurally fragmented.

Therefore:

```text
AutoTrace execution       = PASS
Skeleton execution        = PASS
2-backend comparison      = COMPLETE
AutoTrace default         = NOT RECOMMENDED from baseline alone
Skeleton default          = NOT YET ACCEPTABLE
Backend winner            = HOLD
Reason                    = both need editability / semantic review
```

No score is allowed to override semantic failure.

## Semantic and Human gates

The runner carries the fixture-specific semantic contracts forward:

```text
WRITE = paper + diagonal pen + writing-hand interaction
THINK = hand-to-face + visible forearm + arm/face relationship
LOOK  = head direction + lateral gaze + face-direction cues
```

The automated runner does not infer these labels from SSIM.

```text
G1 SVG VALID        = PASS for generated candidates
G2 STYLE VALID      = PASS for normalized candidates
G3 STRUCTURE        = REQUIRES REVIEW / fragmentation warning
G4 VISUAL           = MEASURED
G5 SEMANTIC GESTURE = REQUIRES HUMAN
Human Visual Acceptance = NOT CONSUMED
```

## Evidence verdict after AutoTrace provision

```text
fixture pin / integrity       = PASS
normalizer                    = PASS
static evaluator              = PASS for implemented checks
AutoTrace backend execution   = PASS
skeleton backend execution    = PASS
2-backend comparison          = COMPLETE
B1                             = RESOLVED
Pilot evidence completeness   = READY FOR FRESH REVIEW
Semantic Gesture Check        = REQUIRES HUMAN
Backend selection             = HOLD
Human Visual Acceptance       = NOT CONSUMED
Merge / Promotion             = HOLD
```

This evidence does not authorize a backend promotion, source SVG replacement, Merge, or production use.
