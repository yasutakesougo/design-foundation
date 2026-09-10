# Curve Reconstruction Correction-2 evidence

Target: `IMAGE-FIRST-SEMANTIC-REDRAW-V1` Curve Reconstruction Correction-2

Authority:

```text
Definition / Scope = Issue #94 / LOCKED
Fresh Definition Review = Issue #95 / PASS
Reference Correction-1 = PR #92 @ 2fe58d3852a61532629b2459ca810c2cf316b09f
Implementation branch = work/image-first-curve-reconstruction-v2
Human Implementation Start = GO / CONSUMED
```

## Human trigger

Human review of Correction-1 rated `SPLINE BEZIER 1.60` as the strongest current candidate but kept Human Visual Acceptance on HOLD. The remaining problem is curvature character rather than simple tangent continuity:

```text
SOURCE              = 10/10 reference
POLYLINE            = 5/10     / FAIL
BEZIER FIT 1.10     = 6.5/10   / FAIL
SPLINE BEZIER 1.60  = 8–8.5/10 / HOLD / best current comparison baseline
```

The Correction-2 objective is therefore:

```text
remove high-frequency curvature noise
+ preserve SOURCE low-frequency curvature character
+ avoid mechanical circularization / over-regularization
```

## Compared modes

### Baseline — SPLINE BEZIER 1.60

```text
curve-mode       = spline-bezier
RDP epsilon      = 1.60 source px
smooth passes    = 2
smooth weight    = 0.18
spline tension   = 0.70
```

### A — Scale-aware spline

```text
curve-mode       = scale-aware-spline
arc-length resample = 1 source px
local polynomial smoothing = quadratic / adaptive radius
minimum radius   = 4 samples
maximum radius   = 10 samples
knot epsilon     = 1.05 source px
minimum knot spacing = 9 samples
maximum knot gap = 30 samples
tangent window   = 8 samples
tension          = 0.98
```

The smoothing radius decreases around broad curvature changes and increases on near-smooth spans. Endpoints and topology-span boundaries remain fixed.

### B — Curvature-aware spline

```text
curve-mode       = curvature-aware-spline
arc-length resample = 1 source px
local polynomial smoothing = quadratic / radius 7
curvature window = 10 samples
knot epsilon     = 1.15 source px
curvature retention quantile = 0.50
minimum knot spacing = 12 samples
maximum knot gap = 34 samples
tangent window   = 9 samples
tension          = 0.98
```

This mode combines low-pass/RDP knots with broad curvature extrema and inflection candidates. It is intentionally denser where broad shape transitions need preservation.

No mode is selected as a production backend by this evidence.

## Regression boundary

The existing `polyline`, `bezier-fit`, and `spline-bezier` modes were replayed before accepting the Correction-2 implementation. For THINK / LOOK / WRITE, the Correction-1 `spline-bezier 1.60` output remained byte-identical with the extended script.

```text
old-mode regression = PASS
PR #92 behavior      = preserved
```

## SVG style / topology checks

All 9 final comparison SVGs (3 gestures × 3 modes) passed the existing style validator:

```text
viewBox          = 0 0 512 512
fill             = none
stroke           = currentColor
stroke-width     = 8
stroke-linecap   = round
stroke-linejoin  = round
transform count  = 0
style validator  = PASS
```

Path count is unchanged within each gesture across the compared modes:

```text
THINK = 67 paths
LOOK  = 47 paths
WRITE = 68 paths
```

Measured endpoint drift remains `0` for both Correction-2 candidates. Graph topology extraction and span boundaries are unchanged.

## Structural / tangent evidence

| Gesture | Metric | SPLINE 1.60 | Scale-aware | Curvature-aware |
|---|---|---:|---:|---:|
| THINK | segments | 164 | 190 | 198 |
| THINK | join angle p95 | 0.3824° | 0.2161° | 0.2067° |
| THINK | joins >10° | 0 | 0 | 0 |
| THINK | endpoint drift max | 0 | 0 | 0 |
| LOOK | segments | 149 | 170 | 176 |
| LOOK | join angle p95 | 0.3533° | 0.2188° | 0.2059° |
| LOOK | joins >10° | 0 | 0 | 0 |
| LOOK | endpoint drift max | 0 | 0 | 0 |
| WRITE | segments | 205 | 242 | 258 |
| WRITE | join angle p95 | 0.2852° | 0.2167° | 0.1965° |
| WRITE | joins >10° | 0 | 0 | 0 |
| WRITE | endpoint drift max | 0 | 0 | 0 |

Correction-2 does not regress the kink-removal result from Correction-1. The trade-off is higher segment/control-point density than SPLINE 1.60, especially for the curvature-aware candidate. That structural cost remains part of Human/backend review.

## Scale-separated curvature-character evidence

The evaluator compares each candidate against a low-frequency proxy built from the same SOURCE centerline. This is evidence only, not an acceptance authority.

### THINK

| Metric | SPLINE 1.60 | Scale-aware | Curvature-aware |
|---|---:|---:|---:|
| low-frequency curvature RMSE | 0.004038 | **0.003160** | 0.003388 |
| high-frequency curvature RMS | 0.018441 | **0.009785** | 0.011654 |
| SOURCE high-frequency RMS | 0.013736 | 0.013736 | 0.013736 |
| low-frequency std ratio | 1.0532 | 0.8914 | 0.8597 |
| geometry RMS to SOURCE lowpass | 0.4410 | 0.3330 | **0.3273** |
| broad sign-change delta | 22 | **16** | **16** |
| broad curvature-extrema delta | 97 | 88 | **85** |

### LOOK

| Metric | SPLINE 1.60 | Scale-aware | Curvature-aware |
|---|---:|---:|---:|
| low-frequency curvature RMSE | 0.005433 | **0.003597** | 0.004024 |
| high-frequency curvature RMS | 0.024768 | **0.015356** | 0.015690 |
| SOURCE high-frequency RMS | 0.017053 | 0.017053 | 0.017053 |
| low-frequency std ratio | 1.2159 | 0.9700 | 0.9387 |
| geometry RMS to SOURCE lowpass | 0.4160 | **0.3479** | 0.3485 |
| broad sign-change delta | 9 | 6 | **4** |
| broad curvature-extrema delta | 97 | 88 | **81** |

### WRITE

| Metric | SPLINE 1.60 | Scale-aware | Curvature-aware |
|---|---:|---:|---:|
| low-frequency curvature RMSE | 0.004367 | **0.003238** | 0.003462 |
| high-frequency curvature RMS | 0.022486 | **0.013952** | 0.016730 |
| SOURCE high-frequency RMS | 0.015459 | 0.015459 | 0.015459 |
| low-frequency std ratio | 1.0150 | 0.9370 | 0.9269 |
| geometry RMS to SOURCE lowpass | 0.7663 | 0.7061 | **0.6967** |
| broad sign-change delta | 15 | 7 | **6** |
| broad curvature-extrema delta | 130 | 115 | **107** |

## Interpretation

Both new methods improve the specific Correction-2 target relative to SPLINE 1.60:

- `joins >10°` remains zero, so D1/polyline kink is not reintroduced.
- high-frequency curvature RMS is materially lower, which supports reduction of D2/micro-wave.
- low-frequency curvature RMSE and SOURCE-lowpass geometry distance improve, supporting better retention of broad contour character.
- neither result is accepted automatically; SOURCE is intentionally non-uniform and numerical smoothness can still hide D3/over-regularization.

### Scale-aware candidate

The scale-aware mode is the current **agent visual candidate** because it gives the strongest overall balance:

- lowest high-frequency RMS for all three gestures;
- lower low-frequency curvature RMSE for all three gestures;
- visibly preserves the broad head/hair contour while avoiding the mechanically even SPLINE 1.60 arc;
- lower structural density than the curvature-aware mode.

### Curvature-aware candidate

The curvature-aware mode tends to retain more measured broad sign/extrema structure, but it is denser and retains somewhat more high-frequency energy. It remains a useful conservative comparison for SOURCE shape-transition preservation.

This evidence **does not select a backend**. Human visual inspection remains authoritative.

## Human review images

Exact locally produced comparison evidence:

```text
512px comparison
SHA-256 = 7e4ed21ca821b088dce643a4f85976f6fd29a2659ee6eb9f91b885be0da3e3a4

64px comparison
SHA-256 = 015c9bae9bd7ddaa1cb24af96579d8e1c751b6ed515af842a676bb5557b59b99

400% priority-region comparison
SHA-256 = 8dc9d996eab5b0566211391c95ca5912744ea20ba7719f05a69658080caef6e5
```

The 400% sheet compares:

```text
SOURCE | SPLINE 1.60 | SCALE-AWARE | CURVATURE-AWARE
```

for THINK / LOOK / WRITE, focusing on crown, back-of-head, cheek/jaw and long outer-hair regions.

## Acceptance readback

```text
C2-1 Topology preserved                    = PASS CANDIDATE
C2-2 Semantic anchors preserved            = PASS CANDIDATE / HUMAN CONFIRMATION REQUIRED
C2-3 Polyline kink remains removed         = PASS CANDIDATE
C2-4 Micro-wave materially reduced         = PASS CANDIDATE
C2-5 SOURCE low-frequency curvature        = PASS CANDIDATE / HUMAN CONFIRMATION REQUIRED
C2-6 No obvious circularization            = READY FOR HUMAN DECISION
C2-7 SVG style contract                    = PASS
C2-8 Structural editability                = PASS CANDIDATE / density trade-off recorded
C2-9 64px / 512px retention                = PASS CANDIDATE
C2-10 400% Human Curve Review              = NOT CONSUMED

Agent visual candidate                     = scale-aware-spline
Backend selection                          = HOLD
Human Visual Acceptance                    = NOT CONSUMED / HOLD
Asset replacement                          = NOT AUTHORIZED
Merge / Promotion                          = HOLD
```

Correction-2 evidence is sufficient for Fresh Implementation / Scope review. It does not consume Human Ready or Human Visual Acceptance.
