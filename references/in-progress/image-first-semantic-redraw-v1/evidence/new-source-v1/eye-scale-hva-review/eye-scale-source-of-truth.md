# EYE-SCALE-CORRECTION-V1 — SVG / source-of-truth

```text
SVG candidate source of truth = git tree objects for candidates/new-source-v1/*.svg at the pinned candidate commit, not HVA render/evidence commits.
```

Resolution of the earlier UNCHANGED confusion:

```text
2eba5b1 = 1.60x Implementation candidate identities (SVG truth for that review)
evidence-only commits before mid revision = renders/docs only; SVG bytes intentionally UNCHANGED vs 2eba5b1
0362b17 = mid-point candidate revision (SVG bytes intentionally CHANGED: THINK/LOOK 1.30x, WRITE 1.20x)
98374f6 = decision-package text only; no further SVG identity change
working tree / HEAD package commits after 0362b17 must keep mid SVG SHA-256 identical to 0362b17 unless a new candidate revision is explicitly declared
ACTIVE archive source = never mutated in this lane
```

Machine cross-check: `eye-scale-mid-vs-old-proof.json`.
