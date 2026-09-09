# Fixture Contract

## Pinned source

```text
Repository  = yasutakesougo/design-foundation
Source PR   = #71
Source ref  = work/hitokoto-person-line-style-v1
Source HEAD = 4acdefca152dd3f4fd1c69424b3f4f79f9b78004
```

The source HEAD is pinned for all evidence generated in this implementation slice.

If the source PR moves, the new HEAD must not silently replace these fixtures.

A later fixture refresh requires a fresh scope readback.

## Immutable fixture copies

The following files are copied byte-for-byte from the pinned source HEAD.

```text
fixtures/source-svg/person-note-taking.svg
fixtures/source-svg/person-thinking.svg
fixtures/source-svg/person-looking.svg
```

These copies are ground truth for the round-trip experiment.

Scripts must write generated material outside `fixtures/source-svg/`.

## Semantic labels

### WRITE

Fixture: `person-note-taking.svg`

Required cues:

```text
paper / notebook
pen
writing hand
pen / hand / paper interaction
```

### THINK

Fixture: `person-thinking.svg`

Required cues:

```text
hand-to-face relationship
visible forearm gesture
arm / face relationship survives reduction
```

### LOOK

Fixture: `person-looking.svg`

Required cues:

```text
head direction
lateral gaze
face-direction cue
shoulder-direction cue where present
```

## Deterministic raster input

The raster input must be generated from the pinned SVG copy rather than from a screenshot.

Default target sizes are:

```text
512 × 512 px = reconstruction input and detailed evidence
64 × 64 px   = semantic reduction evidence
```

The exact rasterizer executable and version must be recorded with each result.

If no approved local rasterizer is available, the runner reports `SKIP` and does not substitute an undocumented renderer.

## Source protection

The Pilot must not modify:

```text
references/in-progress/hitokoto-person-line-style-v1/examples/person-note-taking.svg
references/in-progress/hitokoto-person-line-style-v1/examples/person-thinking.svg
references/in-progress/hitokoto-person-line-style-v1/examples/person-looking.svg
```

The Pilot may only read from the pinned source and write under its own Pilot directory.
