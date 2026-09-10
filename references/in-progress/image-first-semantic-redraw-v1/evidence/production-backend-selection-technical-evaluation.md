# Production Backend Selection — Technical Evaluation

Target: `IMAGE-FIRST-SEMANTIC-REDRAW-V1`

## Authority

```text
Definition / Scope Issue            = #102 / Human LOCKED
Fresh Definition / Scope Review     = #103 / PASS
Target PR                            = #100
Exact target HEAD                   = 3a856d94450bcf413afb67063b375c85a161afc0
Technical Evaluation Implementation = GO / CONSUMED
Production Backend Selection        = HOLD / NOT AUTHORIZED
Asset replacement                   = NOT AUTHORIZED
Merge / Promotion                   = HOLD / NOT AUTHORIZED
```

This evaluation may recommend `SOURCE-GUIDED`, `JOIN-CONTINUITY`, or `HOLD`. It does not itself select a production backend.

## SOURCE lifecycle

`SOURCE-GUIDED` does not open or depend on a second external SOURCE file. Both candidates begin with the same raster-derived topology. `curvature_aware_geometry(points)` derives an in-process low-frequency reference (`ref`) from centerline points traced from the current input raster. `SOURCE-GUIDED` then adjusts bounded Bézier handle magnitudes toward that reference.

```text
generation:
input raster
→ semantic stroke mask
→ skeleton / centerline points
→ low-frequency reference
→ SOURCE-GUIDED refinement
→ final SVG

after SVG finalization:
source raster is NOT required for rendering/use

exact audit replay:
exact input raster bytes
+ SHA-256
+ parameter set
+ compatible runtime/library versions
are required
```

A hash proves identity but cannot regenerate the SVG. Production audit therefore needs the exact accepted input raster bytes to remain retained or recoverable.

## Runtime / dependencies

Tested runtime:

```text
Python       = 3.13.5
NumPy        = 2.3.5
scikit-image = 0.26.0
Pillow       = 12.3.0
Inkscape     = 1.4 / review rendering only
Platform     = Linux x86_64
```

SOURCE-GUIDED and JOIN-CONTINUITY have the same generation dependency set: Python + Pillow + NumPy + scikit-image. SOURCE-GUIDED adds no external file lookup, network operation, external executable, or new library. Cross-version byte determinism is not claimed; audit replay must record or pin the compatible runtime fingerprint.

## Same-input determinism

Base input SHA-256:

| Gesture | SHA-256 |
|---|---|
| THINK | `0ee03712a4160422e9daaae9869f8112a1d899df884564f80cbb6fdc8a6a774c` |
| LOOK | `edfd7511321a3b7ce5aaa9495b70f2cc5b68289e65ef10bbc6cc5f8c9bba1e46` |
| WRITE | `ad016ad24319f2e7cd59c6eb275fee25fda2bac94adc5a4910e48f6681a3af94` |

Each mode was replayed 5 times per gesture in the same runtime. SVG and metrics JSON were byte-identical in every set.

```text
SOURCE-GUIDED THINK = 5/5 byte-identical
SOURCE-GUIDED LOOK  = 5/5 byte-identical
SOURCE-GUIDED WRITE = 5/5 byte-identical

JOIN-CONTINUITY THINK = 5/5 byte-identical
JOIN-CONTINUITY LOOK  = 5/5 byte-identical
JOIN-CONTINUITY WRITE = 5/5 byte-identical
```

SOURCE-GUIDED SVG SHA-256:

```text
THINK d344b3e28f52976e7e4e4c6d25b11e8491cf9749b0a04b8101f0f620a8f0ab92
LOOK  31913de84893a0d230aaa7614aef8a25684a1b1b7281cb57e184be47e04a47db
WRITE 949217ea6f9786cf4d16563ce87d2a8d9218e1d6827dd83b04732286cf85f5bd
```

Result: `TIE / PASS in tested runtime`.

## SOURCE fidelity vs curvature continuity

Correction-3 targeted evidence:

| Gesture | Metric | JOIN-CONTINUITY | SOURCE-GUIDED | Better |
|---|---|---:|---:|---|
| THINK | low-frequency curvature RMSE | 0.003189 | **0.003077** | SOURCE-GUIDED |
| THINK | geometry RMS to SOURCE lowpass | 0.428647 | **0.420096** | SOURCE-GUIDED |
| LOOK | low-frequency curvature RMSE | 0.004305 | **0.004172** | SOURCE-GUIDED |
| LOOK | geometry RMS to SOURCE lowpass | 0.431326 | **0.427556** | SOURCE-GUIDED |
| WRITE | low-frequency curvature RMSE | 0.001825 | **0.001789** | SOURCE-GUIDED |
| WRITE | geometry RMS to SOURCE lowpass | 1.096070 | **1.095054** | SOURCE-GUIDED |

SOURCE-GUIDED has the stronger SOURCE-character match on all three fixtures and matches the Human visual preference.

JOIN-CONTINUITY is stronger on the narrow numeric objective of same-sign join-curvature equality:

| Gesture | CURVATURE-AWARE | JOIN-CONTINUITY | SOURCE-GUIDED |
|---|---:|---:|---:|
| THINK | 0.049192 | **0.009177** | 0.014484 |
| LOOK | 0.042955 | **0.022159** | 0.034815 |
| WRITE | 0.032366 | **0.018553** | 0.019177 |

Both already passed Human smoothness review. JOIN optimizes join equality more directly; SOURCE-GUIDED better preserves gradual SOURCE-specific curvature progression.

## Input-variation robustness

Four deterministic mild perturbations were used on all three inputs:

```text
reencode           = same pixels, PNG re-encoding
brightnessplus3pct = +3% brightness
resample98         = 98% LANCZOS down/up round-trip
blur0.35           = Gaussian blur radius 0.35
```

All 24 candidate outputs (2 modes × 3 gestures × 4 variants) passed fail-closed SVG/metrics validation.

| Worst-case metric | SOURCE-GUIDED | JOIN-CONTINUITY |
|---|---:|---:|
| minimum 64px SSIM | 0.999093 | 0.999094 |
| minimum 512px SSIM | **0.996102** | 0.996081 |
| maximum 2048px normalized MAE | **0.001543** | 0.001559 |
| max absolute path-count delta | 2 | 2 |
| max absolute segment-count delta | 7 | 7 |
| max refined-path-count delta | 1 | 1 |

Pixel-identical PNG re-encoding produced identical SVGs. Mild blur/resampling can change skeleton topology slightly before either refinement runs; this sensitivity belongs primarily to the shared raster→skeleton stage, not SOURCE-GUIDED specifically. Evidence is limited to this mild perturbation range.

Result: `TIE / PASS CANDIDATE within tested range`.

## Fail-closed / explicit fallback

Evaluation-only `backend_selection_gate.py` rejects missing/malformed output, invalid XML/style, forbidden elements/transforms, non-finite coordinates, path-count mismatch, source-topology count mismatch, non-positive segments, and non-finite deviation metrics.

Fallback policy:

```text
SOURCE-GUIDED failure + no --allow-fallback
→ HOLD
→ fallback not attempted

SOURCE-GUIDED failure + explicit --allow-fallback
→ attempt JOIN-CONTINUITY
→ record primary failure class
→ record fallback_used=true
→ accept JOIN only if it also validates

both fail
→ HOLD
```

Contract tests: `8/8 PASS`.

Actual failure probes against the exact vectorizer:

```text
blank white PNG / no fallback       → HOLD / one failed attempt
blank white PNG / fallback allowed  → HOLD / both failed attempts recorded
malformed bytes / no fallback       → HOLD / one failed attempt
malformed bytes / fallback allowed  → HOLD / both failed attempts recorded
```

An integration test with deliberate primary failure and valid fallback resolves to `JOIN-CONTINUITY`, records `fallback_used=true`, and preserves the primary failure class. Silent fallback is prohibited.

The gate is evaluation-only/additive; it does not silently modify the existing production pipeline. Later Asset Replacement scope should require this contract or an equivalent production integration.

## Pipeline impact / testability

Technical evaluation is ADD-only relative to PR #100. It does not change `centerline_vectorize.py`, `curve_quality.py`, existing SVGs, prompts, package/lock files, CI, or production assets. Both candidate modes already exist at the target HEAD and preserve the same SVG output contract.

## Selection matrix

| # | Criterion | Result |
|---|---|---|
| 1 | SOURCE fidelity | **SOURCE-GUIDED advantage** |
| 2 | same-input determinism | tie / PASS in tested runtime |
| 3 | long-contour curvature continuity | JOIN numeric advantage; SOURCE-GUIDED Human accepted |
| 4 | 64px / normal / magnified stability | both PASS; Human preference SOURCE-GUIDED |
| 5 | mild input-variation robustness | tie / PASS candidate |
| 6 | fail-closed behavior | PASS with explicit gate contract |
| 7 | dependency burden | tie; SOURCE-GUIDED adds no external dependency |
| 8 | testability | PASS / 8 contract tests |
| 9 | existing pipeline impact | low |
| 10 | fallback viability | PASS / explicit JOIN-CONTINUITY fallback |

## Technical recommendation

```text
Required-result recommendation = SOURCE-GUIDED
Fallback                       = JOIN-CONTINUITY
Production Backend Selection   = HOLD / HUMAN DECISION REQUIRED
```

Rationale: SOURCE-GUIDED is the Human-accepted visual winner and has the strongest SOURCE-fidelity evidence, while matching JOIN-CONTINUITY on tested determinism, mild-input robustness, dependency burden, and pipeline impact. JOIN-CONTINUITY remains a sound explicit fallback and has the stronger direct join-curvature-equality metric.

Conditions to carry into later Asset Replacement scope if SOURCE-GUIDED is selected:

```text
- retain/recover exact source-raster bytes for audit replay
- record source SHA-256
- record parameter set
- record or pin runtime/library fingerprint
- apply fail-closed candidate validation
- permit JOIN-CONTINUITY fallback only explicitly
- persist fallback reason and actual backend used
```

## Current gate

```text
Technical Evaluation Implementation = COMPLETE CANDIDATE
Technical recommendation            = SOURCE-GUIDED
Fallback recommendation             = JOIN-CONTINUITY
Fresh Technical Review              = REQUIRED
Production Backend Selection        = HOLD / NOT AUTHORIZED
Asset Replacement                   = NOT AUTHORIZED
Merge / Promotion                   = HOLD / NOT AUTHORIZED
```
