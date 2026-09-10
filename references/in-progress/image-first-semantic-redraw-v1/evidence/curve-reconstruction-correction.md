# Curve Reconstruction Correction evidence

Target: `IMAGE-FIRST-SEMANTIC-REDRAW-V1` Curve Reconstruction Correction

Reference implementation: PR #88 @ `60fd695f1518efc94291867bfb68e1a101e0f74e`

Definition / Scope: Issue #90 / Fresh Review #91

## Human trigger

Human review found that the Image-first redraw preserves gesture and distant-view reproduction well, but the PR #88 SVG output still shows visible polyline kinks at closer inspection. The correction therefore keeps the Image-first raster stage unchanged and changes only post-centerline geometry reconstruction.

## Compared methods

```text
Baseline
  polyline
  RDP epsilon = 1.35 source px
  SVG = M + L commands

A
  bezier-fit
  recursive endpoint-preserving cubic Bézier fit
  split tangents shared across recursive boundaries
  fit error target = 1.10 source px

B
  spline-bezier
  2 passes light local smoothing, weight 0.18
  endpoint protection
  RDP epsilon after smoothing = 1.60 source px
  tangent-limited cubic Hermite → SVG cubic Bézier
```

All methods use the same Image-first replay panels and the same skeleton/topology extraction. Short spans below 12 source pixels remain linear to avoid artificial curvature in intentional small cues.

## Protected geometry behavior

The implementation preserves each traced topology span's start/end coordinates exactly. Graph junctions remain span boundaries. The two curve methods therefore do not freely smooth across topology junctions.

Human semantic contacts remain a separate review gate. Endpoint equality does not by itself prove that every semantic relationship is visually acceptable.

## Structural / curve metrics

### THINK

| metric | polyline | bezier-fit | spline-bezier |
|---|---:|---:|---:|
| paths | 67 | 67 | 67 |
| segments | 178 | 211 | 164 |
| L commands | 178 | 16 | 16 |
| C commands | 0 | 195 | 148 |
| control points | 0 | 390 | 296 |
| join angle p95 | 48.0432° | 0.3919° | 0.3824° |
| join angle max | 61.7178° | 0.8124° | 0.5230° |
| internal joins >10° | 95 | 0 | 0 |
| endpoint drift max | 0 | 0 | 0 |
| centerline deviation mean | 0.3959 px | 0.4700 px | 0.6869 px |
| centerline deviation max | 1.3744 px | 1.6211 px | 3.6446 px |
| 512px render stroke proximity | 0.0738 px | 0.0707 px | 0.0813 px |
| style validator | PASS | PASS | PASS |

### LOOK

| metric | polyline | bezier-fit | spline-bezier |
|---|---:|---:|---:|
| paths | 47 | 47 | 47 |
| segments | 166 | 191 | 149 |
| L commands | 166 | 6 | 6 |
| C commands | 0 | 185 | 143 |
| control points | 0 | 370 | 286 |
| join angle p95 | 50.8127° | 0.5645° | 0.3533° |
| join angle max | 134.5937° | 0.7099° | 1.0105° |
| internal joins >10° | 107 | 0 | 0 |
| endpoint drift max | 0 | 0 | 0 |
| centerline deviation mean | 0.3959 px | 0.5219 px | 0.6707 px |
| centerline deviation max | 1.3744 px | 2.1330 px | 2.9439 px |
| 512px render stroke proximity | 0.0781 px | 0.0733 px | 0.0789 px |
| style validator | PASS | PASS | PASS |

### WRITE

| metric | polyline | bezier-fit | spline-bezier |
|---|---:|---:|---:|
| paths | 68 | 68 | 68 |
| segments | 226 | 240 | 205 |
| L commands | 226 | 9 | 9 |
| C commands | 0 | 231 | 196 |
| control points | 0 | 462 | 392 |
| join angle p95 | 43.4656° | 0.3731° | 0.2852° |
| join angle max | 74.6098° | 0.4880° | 0.4739° |
| internal joins >10° | 132 | 0 | 0 |
| endpoint drift max | 0 | 0 | 0 |
| centerline deviation mean | 0.3987 px | 0.5372 px | 0.7469 px |
| centerline deviation max | 1.3333 px | 2.1686 px | 4.1236 px |
| 512px render stroke proximity | 0.0577 px | 0.0591 px | 0.0650 px |
| style validator | PASS | PASS | PASS |

`centerline deviation` is measured in the 724px source-panel coordinate system. `render stroke proximity` is a symmetric 512px stroke-distance diagnostic; lower is closer to the Image-first raster centerline. These metrics are supporting evidence only.

## Readback

Both curve methods materially remove the RDP/polyline tangent discontinuities:

```text
polyline p95 join angle = about 43–51 degrees
bezier-fit p95          = below 0.57 degrees
spline-bezier p95       = below 0.39 degrees

polyline joins >10°      = 95 / 107 / 132
bezier-fit joins >10°    = 0 / 0 / 0
spline-bezier joins >10° = 0 / 0 / 0
```

Both curve modes preserve the measured path endpoints exactly and retain the locked SVG style contract.

### A — bezier-fit interpretation

`bezier-fit` stays closer to the extracted centerline and the 512px raster. Its tradeoff is structural density: segment count rises above the polyline baseline in all three fixtures.

### B — spline-bezier interpretation

`spline-bezier` is visually the smoothest of the two curve candidates in the 200–400% inspection and reduces total segment count relative to the polyline baseline for all three fixtures:

```text
THINK 178 → 164
LOOK  166 → 149
WRITE 226 → 205
```

Its tradeoff is a slightly larger centerline deviation than `bezier-fit`, so semantic contact/shape retention must remain under Human review.

## Agent candidate

For the Human curve-quality review, the preferred visual candidate is:

```text
spline-bezier
--epsilon 1.60
--smooth-passes 2
--smooth-weight 0.18
--spline-tension 0.70
```

This is **not** backend selection or promotion. `bezier-fit --bezier-error 1.10` remains the conservative comparison candidate because it follows the extracted centerline more closely.

## Gate interpretation

```text
C1 Topology preserved             = PASS CANDIDATE
C2 Semantic anchors preserved     = PASS CANDIDATE / HUMAN CONFIRMATION REQUIRED
C3 Curve continuity improved      = PASS CANDIDATE
C4 SVG style contract             = PASS
C5 Structural editability         = PASS CANDIDATE
C6 512px / 64px render retention  = PASS CANDIDATE
C7 Magnified Human Curve Review   = NOT CONSUMED

Human Semantic / Visual Acceptance = HOLD
Asset replacement                  = NOT AUTHORIZED
Backend selection                  = HOLD
Merge / Promotion                  = HOLD
```

The correction evidence does not consume Human Semantic / Visual Acceptance.
