# Implementation replay evidence

This evidence was produced after the Implementation Start authorization and exercises the repository candidate scripts end to end against the current pilot redraw sheet.

## Image-generation audit identity

```text
ChatGPT image generation gen_id = 14d29777-4250-47e2-b552-f009b97d24f7
sheet size                      = 2172 x 724
sheet SHA-256                   = f37ccec7f7a8b7146701c574a44ffcd35b3cdab82c557ff028beed2df523a85d
```

The `gen_id` is audit metadata only. The image stage is nondeterministic and cannot be rebuilt by hash from the prompt alone.

## Replay commands

```bash
python scripts/split_three_panel.py redraw-sheet.png panels/
python scripts/centerline_vectorize.py panels/person-thinking.png replay-svg/person-thinking.svg
python scripts/centerline_vectorize.py panels/person-looking.png replay-svg/person-looking.svg
python scripts/centerline_vectorize.py panels/person-writing.png replay-svg/person-writing.svg

python scripts/validate_svg.py replay-svg/person-thinking.svg
python scripts/validate_svg.py replay-svg/person-looking.svg
python scripts/validate_svg.py replay-svg/person-writing.svg

python scripts/render_review.py replay-svg/person-thinking.svg review/
python scripts/render_review.py replay-svg/person-looking.svg review/
python scripts/render_review.py replay-svg/person-writing.svg review/
```

## Replay result

```text
THINK paths = 67 / style validator PASS
LOOK  paths = 47 / style validator PASS
WRITE paths = 68 / style validator PASS
```

All three outputs preserve:

```text
viewBox          = 0 0 512 512
fill             = none
stroke           = currentColor
stroke-width     = 8
stroke-linecap   = round
stroke-linejoin  = round
transform count  = 0
```

512px and 64px renders were produced successfully with Inkscape for all three outputs.

## Frozen replay SVG hashes

```text
THINK = 8dcc10dd24ae8176b52bc91f0fc75ad6deb4d7899dde3770fddfae989f54378c
LOOK  = 261bd66b7303c6489dc14a1bb8ca8860c413c846343e05d8e0380f8412b4af35
WRITE = 23f1015abbb10421887b44b03ffe08bb04aad4cb862331c502c5ef0c22f40d9d
```

## Interpretation

The implementation confirms that the lane is operational without repository-wide dependency or CI mutation. The exact path counts differ slightly from the earlier proof (`63 / 47 / 67`) because the implementation makes crop/mask/trace behavior explicit rather than reproducing hidden local preprocessing steps.

This difference is expected evidence of a now-auditable pipeline, not a regression by itself.

```text
I1 Image semantic adequacy = PASS CANDIDATE / Human confirmation required
I2 SVG style validity      = PASS
I3 Structural editability  = PASS CANDIDATE / still more paths than hand-authored fixtures
I4 Render retention        = PASS CANDIDATE at 512px and 64px
I5 Human Semantic Review   = NOT CONSUMED
```

No production asset replacement, backend winner, merge, or promotion is authorized by this replay.
