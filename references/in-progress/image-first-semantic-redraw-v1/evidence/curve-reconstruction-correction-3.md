# Curve Reconstruction Correction-3 evidence

Target: `IMAGE-FIRST-SEMANTIC-REDRAW-V1` Curve Reconstruction Correction-3

Authority:

```text
Definition / Scope          = Issue #98 / LOCKED
Fresh Definition Review     = Issue #99 / PASS
Reference Correction-2 PR  = #96 @ 2f56df5f8aa92e30d3d417e263b57d125ce23a16
Implementation branch      = work/image-first-curve-reconstruction-v3
Human Implementation Start = GO / CONSUMED
```

## Human trigger

Correction-2 Human review concluded:

```text
SOURCE          = 10/10 reference
SPLINE 1.60     = 8.4–8.6 / HOLD
SCALE-AWARE     = ~9.0 / HOLD
CURVATURE-AWARE = 9.1–9.3 / HOLD / best Human-rated candidate
```

Correction-2 materially removed kink and micro-wave. The remaining Human-visible defect is a subtle handoff between individually smooth Bézier sections on long organic contours.

Correction-3 therefore keeps `CURVATURE-AWARE` as the comparison baseline and changes only handle magnitudes at joins on long topology spans. It does not add a new global smoothing family.

## Compared local refinements

### A — JOIN-CONTINUITY

```text
curve-mode = curvature-aware-join
long-path threshold = 80 SOURCE px
max handle scale = ±18%
```

For same-sign non-trivial curvature joins, retain knot positions and tangent directions and apply the minimum paired handle-length scaling that moves left/right cubic curvature toward continuity. Near inflections / sign disagreement, leave the join unchanged.

### B — SOURCE-GUIDED

```text
curve-mode = curvature-aware-source-guided
long-path threshold = 80 SOURCE px
SOURCE target window = 9 resampled points
max handle scale = ±18%
blend = 0.85
```

Use the existing curvature-aware low-frequency reference and a wide three-point signed-curvature estimate. Retain knots and tangent directions; adjust only neighboring handle magnitudes toward the SOURCE low-frequency target. Near inflections or sign disagreement, leave the join unchanged.

Neither method is selected as a production backend by this evidence.

## Scope / regression boundary

Exactly the locked implementation surface is used:

```text
UPDATE scripts/centerline_vectorize.py
UPDATE scripts/curve_quality.py
ADD    evidence/curve-reconstruction-correction-3.md
```

No image-redraw prompt, generated source raster, existing asset, Foundation, Pattern, CI, package file, lockfile, PR #96, PR #92, PR #88, PR #84 or PR #78 implementation commit is changed.

Existing `curvature-aware-spline` replay is byte-identical before/after Correction-3 for THINK / LOOK / WRITE:

```text
THINK old-mode byte regression = PASS
LOOK  old-mode byte regression = PASS
WRITE old-mode byte regression = PASS
```

## Structural / style evidence

All compared candidates retain:

```text
viewBox          = 0 0 512 512
fill             = none
stroke           = currentColor
stroke-width     = 8
stroke-linecap   = round
stroke-linejoin  = round
transform count  = 0
```

Path / segment structure is unchanged by the two refinements:

```text
THINK = 67 paths / 198 segments
LOOK  = 47 paths / 176 segments
WRITE = 68 paths / 258 segments
```

Endpoint positions are unchanged (`endpoint drift max = 0`) because Correction-3 changes only cubic handle magnitudes.

## Major-contour curvature handoff evidence

`curve_quality.py` adds an evidence-only metric for absolute left/right cubic curvature jump on the same long-upper-contour geometry gate used by Correction-3. Opposite-sign joins are counted separately instead of being forced toward equal curvature across true inflections.

| Gesture | Metric | CURVATURE-AWARE | JOIN-CONTINUITY | SOURCE-GUIDED |
|---|---|---:|---:|---:|
| THINK | same-sign join curvature jump p95 | 0.049192 | **0.009177** | 0.014484 |
| LOOK | same-sign join curvature jump p95 | 0.042955 | **0.022159** | 0.034815 |
| WRITE | same-sign join curvature jump p95 | 0.032366 | **0.018553** | 0.019177 |

JOIN-CONTINUITY gives the stronger direct reduction in Bézier handoff magnitude. SOURCE-GUIDED also reduces the handoff while prioritizing SOURCE low-frequency curvature behavior. These metrics are evidence only and cannot consume Human Visual Acceptance.

## Targeted SOURCE-character evidence

The SOURCE-character diagnostic is restricted to the exact primary-contour gate instead of averaging all long paths. This makes it directly aligned with the Human-locked Correction-3 scope.

| Gesture | Mode | Primary paths | Low-frequency curvature RMSE | Curvature-derivative RMSE | High-frequency RMS | Geometry RMS to SOURCE lowpass |
|---|---|---:|---:|---:|---:|---:|
| THINK | CURVATURE-AWARE | 7 | 0.003571 | 0.001612 | 0.008885 | 0.438294 |
| THINK | JOIN-CONTINUITY | 7 | 0.003189 | 0.001525 | 0.009049 | 0.428647 |
| THINK | SOURCE-GUIDED | 7 | **0.003077** | **0.001471** | 0.008907 | **0.420096** |
| LOOK | CURVATURE-AWARE | 6 | 0.004321 | 0.001503 | **0.018225** | 0.434161 |
| LOOK | JOIN-CONTINUITY | 6 | 0.004305 | 0.001480 | 0.018857 | 0.431326 |
| LOOK | SOURCE-GUIDED | 6 | **0.004172** | **0.001437** | 0.018386 | **0.427556** |
| WRITE | CURVATURE-AWARE | 6 | 0.001843 | **0.000726** | **0.010385** | 1.099111 |
| WRITE | JOIN-CONTINUITY | 6 | 0.001825 | 0.000751 | 0.010897 | 1.096070 |
| WRITE | SOURCE-GUIDED | 6 | **0.001789** | 0.000747 | 0.011027 | **1.095054** |

Interpretation:

- SOURCE-GUIDED gives the strongest low-frequency SOURCE-shape match overall;
- JOIN-CONTINUITY gives the strongest direct join-curvature continuity;
- WRITE shows a small high-frequency cost in both local refinements, so Correction-2 micro-wave quality remains a Human visual check rather than an automatic PASS;
- neither numerical advantage selects a production backend.

## Primary-contour gate audit

The refinement is conservative and geometry-gated to upper long contours. Final refined path indices are:

```text
THINK = [5, 6, 20, 26, 53, 55, 61]  / 7 paths
LOOK  = [1, 5, 9, 25, 32, 38]        / 6 paths
WRITE = [4, 7, 9, 10, 50, 58]       / 6 paths
```

Gate conditions:

```text
minimum source-path length = 80 px
centroid y                 <= 0.62 × image height
vertical span              >= 0.07 × image height
OR horizontal span         >= 0.14 × image width
```

This excludes lower shoulders, hand/notebook/pen regions and short facial marks from Correction-3 refinement while keeping the intended crown, face-side and long-hair contours.

## Human comparison evidence

Exact local comparison sheets:

```text
512px full comparison
SHA-256 = cd5d959006ca78fd4a3d737333ff1a8ced6025426da26519afad8e552da0868a

64px comparison
SHA-256 = 490da711eea540a657ea1f50289793b3013df7522149a17d558111bc0ee88e3b

400% priority-region comparison
SHA-256 = 5dd635413b8bf4814d4ed774b05f647724dd4477270d02c2835d9e866af76a83
```

Column order:

```text
SOURCE | CURVATURE-AWARE | JOIN-CONTINUITY | SOURCE-GUIDED
```

Priority Human question:

```text
Can I still feel where one smooth section hands off to the next?
```

The agent does not consume that answer.

## Acceptance readback

```text
C3-1 Topology preserved                         = PASS CANDIDATE
C3-2 Semantic anchors preserved                 = PASS CANDIDATE / HUMAN CONFIRMATION REQUIRED
C3-3 Correction-2 micro-wave suppression        = HOLD FOR HUMAN VISUAL CHECK
C3-4 Major-contour curvature handoff reduced    = PASS CANDIDATE
C3-5 SOURCE low-frequency progression retained  = PASS CANDIDATE / HUMAN CONFIRMATION REQUIRED
C3-6 No circularization / mechanical regularity = READY FOR HUMAN DECISION
C3-7 SVG style contract                         = PASS
C3-8 Structural editability                     = PASS CANDIDATE / no segment-count increase
C3-9 64px / 512px retention                     = PASS CANDIDATE
C3-10 400% Human Curve Review                   = NOT CONSUMED
C3-11 Human Visual Acceptance                   = NOT CONSUMED / HOLD

Direct handoff candidate   = JOIN-CONTINUITY
Agent visual candidate     = SOURCE-GUIDED / not backend selection
Production backend         = HOLD
Asset replacement          = NOT AUTHORIZED
Merge / Promotion          = HOLD
```

Correction-3 implementation evidence is sufficient for Fresh Implementation / Scope review. It does not consume Human Ready or Human Visual Acceptance.
