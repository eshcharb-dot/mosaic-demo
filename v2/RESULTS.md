# Eval results (Mosaic v2)
Labels: `eval/labels.json` — 30 usable Wikimedia Commons shelf photos, **single labeller, draft**. Small n; treat as indicative, not a benchmark.

## Run 1 — 2026-11-08, Claude Sonnet (alias `sonnet` via `claude -p`, Read tool for the image), prompt v0
Script: `src/analyze-cli.mjs` (raw outputs in `eval/runs/cli-sonnet/`). Scored with `src/score.mjs`.

| Metric | Result |
|---|---|
| Parse failures | 0/30 |
| Brand recall (labelled brands found) | 90% (152/168) |
| Gap recall (empty-space detected) | 100% (9/9) |
| Gap false alarm | 19% (4/21 shelves without gaps flagged) |
| Price-tag count within ±2 | 73% (22/30) |
| Shelf count exact | 55% (16/29) |
| Facings exact | 48% (13/27) |
| Mean latency | 15.8 s/image |
| Cost | Ran on owner's subscription (no API spend). CLI-reported "equivalent" cost is inflated by agent context overhead (~$0.17/img), so not a valid per-image API cost; measure with a direct API call later. |

Takeaways: brand reading and gap detection are strong; exact counting (shelves, facings) is weak (~50%) — consistent with "counting is still hard". Brand recall does not measure precision (hallucinated brands not scored yet).
Next: add brand precision to scorer; prompt v1 (ask for per-shelf crops/step-by-step count); compare model tiers.
