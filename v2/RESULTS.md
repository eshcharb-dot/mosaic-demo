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

## Scorer update — 2026-11-08
Added `brand_precision_vs_labels` to `src/score.mjs`. Run 1: **83% (157/190)** predicted brands match a labelled brand. Caveat: labels are a single labeller's list and may omit visible brands, so the 33 "misses" are an upper bound on hallucination — needs manual review of those 33 before calling them errors.

## Non-match review — 2026-11-08 (run 1, scorer v2)
Scorer now strips diacritics (Höfflin/Hofflin): recall 92% (154/168), precision-vs-labels 84% (159/190). `src/nonmatches.mjs` lists the 31 remaining non-matches (14 images).
Manually viewed 3 of the 14 images (img038, 039, 046): the "extra" brands are real and visible (Totenflak chips; "Quaker Cereal" on a sale sign; Patak's-style curry jars) — **label omissions, not hallucinations**. Not yet viewed: img003/004/015/016/017/021/025/026/036/037/047 (img017 candy wall and img021 are likely omissions too: dense wall, labeller listed only brands it was sure of). So true precision is higher than 84%, but unverified until the rest are reviewed. Takeaway: the labels are a lower bound; improving them (labelling every legible brand) matters more than tuning the model.

## Non-match review part 2 — 2026-11-08
Viewed img003 (Kemach syrup, top-right), img004 (Dr Pepper 12-pack, bottom), img015 ("ja!" jars, bottom-right), img016 (Culinary Elements toothpick dispenser). All four "extra" brands are real and legible, so label omissions again. Running tally: 7/14 images reviewed, 0 hallucinated brands found. Not yet viewed: img017/021/025/026/036/037/047. Labels need a full-brand pass before precision is meaningful.

## Non-match review part 3 — 2026-11-08
Viewed img017 (all 11 extras real: Sweet Tarts, Charleston Chew, Juicy Fruits, Bit-O-Honey, Sugar Babies, Spree, Bottle Caps, Runts, Symphony, Lindt, Quest), img021 (Cocoba, Cha Dô, Bergland Kräuter, Mas Lunette all legible; Mas Lunette small on a wine label), img025 (Edmond Fallot jars, Vita oil, First Price ketchup all visible). 10/14 images reviewed, 0 hallucinated brands found. Not yet viewed: img026/036/037/047 (≈7 brands). Conclusion so far: model precision is effectively ~100% on reviewed images; the 84% figure reflects label omissions. Next: prompt v1 for counting.

## Non-match review part 4 (final) — 2026-11-08
Viewed img026 (Mezzetta olives, Robert Rothschild marinades, Pearls olive cups all legible), img036 (Evonia on shelf, Leader banner), img037 ("Fitness" cereal box). img047 had no non-matches. **14/14 images reviewed: 0 hallucinated brands among the 31 non-matches; all are label omissions** (img037 "Fitness" is a small partially-visible box, the most borderline). Conclusion: precision vs. labels (84%) understates model precision; labels need a full-brand pass. Next: prompt v1 for counting (shelves/facings, the real weakness at ~50%).

## Run 2 — prompt v1 (explicit counting procedure) — 2026-11-08
`node src/analyze-cli.mjs --prompt v1 --out eval/runs/cli-sonnet-v1`, same model (Sonnet via `claude -p`), same 30 images, 0 parse failures. Both runs scored with the current scorer (`src/score.mjs`; v0 facings now reads 56%, not 48%, because of later scorer fixes).

| Metric | v0 | v1 |
|---|---|---|
| Brand recall | 92% | 92% |
| Brand precision vs labels | 84% | 86% |
| Gap recall | 100% (9/9) | 89% (8/9) |
| Gap false alarm | 19% (4/21) | 5% (1/21) |
| Price tags within ±2 | 73% | 63% |
| Shelf count exact | 55% (16/29) | 48% (14/29) |
| Facings exact | 56% (15/27) | 67% (18/27) |

Reading: the counting procedure helps facings (+11 pts, 3 images) and cuts gap false alarms, at the cost of one missed gap, worse shelf count and worse price-tag counts. n=30 and a single run each (model output is non-deterministic), so the differences are within noise except possibly gap false alarms. No clear win: do not adopt v1 wholesale. Next: shelf counting is the weakest metric in both prompts, so try a two-pass approach (separate shelf-count question) and a stronger model tier, ideally repeating each run to measure variance.

## Run 3 — variance check: prompt v0 repeated — 2026-11-08
Same prompt (v0), model and 30 images as Run 1; only the sampling differs (`eval/runs/cli-sonnet-v0b`).

| Metric | v0 run A | v0 run B | v1 |
|---|---|---|---|
| Brand recall | 92% | 93% | 92% |
| Gap false alarm | 19% (4/21) | 29% (6/21) | 5% (1/21) |
| Price tags within ±2 | 73% | 67% | 63% |
| Shelf count exact | 55% | 48% | 48% |
| Facings exact | 56% | 52% | 67% |

Reading: identical-prompt runs swing 7 pts on shelf count and tags, 10 pts on gap false alarms, 4 on facings. So v1's shelf-count and tag "regressions" are inside run-to-run noise (v1 shelf count equals v0-B). v1's facings (+11-15 pts) and gap false-alarm gains are the only differences above the observed spread, still only a single run of n=27-30. Verdict: v1 is plausibly better for facings/gaps and not worse elsewhere; adopt v1 as default pending one more v1 repeat. Exact shelf count stays ~50% either way, so the next lever is a separate shelf-count pass or a stronger model tier.

## Run 4 — v1 repeated (`eval/runs/cli-sonnet-v1b`) — 2026-11-08
Same prompt v1, model, images; 0 parse failures.

| Metric | v0 A | v0 B | v1 A | v1 B |
|---|---|---|---|---|
| Brand recall | 92% | 93% | 92% | 91% |
| Gap recall | 100% | 100% | 89% | 100% |
| Gap false alarm | 19% | 29% | 5% | 5% |
| Price tags ±2 | 73% | 67% | 63% | 70% |
| Shelf count exact | 55% | 48% | 48% | 55% |
| Facings exact | 56% | 52% | 67% | 52% |

Reading: the v1 facings gain (67%) did NOT replicate (52% on repeat), so it was noise; facings sit ~52-67% for both prompts. The only effect that held across both v1 runs is the gap false-alarm drop (5%, 5% vs 19%, 29%; 1/21 vs 4-6/21), with gap recall 89-100%. Shelf count and tags are ~50-70% and indistinguishable between prompts. Verdict: adopt v1 as default for the gap-check only; counting prompts don't move shelf/facing accuracy. Next lever: separate shelf-count pass or stronger model tier.

## Run 5 — model tier: Opus with prompt v1 (`eval/runs/cli-opus-v1`) — 2026-11-08
`node src/analyze-cli.mjs --prompt v1 --model opus`, same 30 images, 0 parse failures, ~24 s/image (5 parallel shards).

| Metric | Sonnet v1 A | Sonnet v1 B | Opus v1 |
|---|---|---|---|
| Brand recall | 92% | 91% | 93% |
| Brand precision vs labels | 86% | n/a | 79% |
| Gap recall | 89% | 100% | 89% |
| Gap false alarm | 5% | 5% | 29% (6/21) |
| Price tags ±2 | 63% | 70% | 53% |
| Shelf count exact | 48% | 55% | 59% |
| Facings exact | 67% | 52% | 56% |

Reading: the larger tier is not better on this set. Everything sits inside the Sonnet run-to-run spread except gap false alarm (29% vs 5%) and price tags (53% vs 63-70%), both worse. Model size is not the lever for counting; Sonnet v1 stays default. Single run each, n=30. (Scorer's mean_cost shows NaN because the CLI meta field is `cost_usd_equiv`; not fixed yet.) Next: separate shelf-count pass, or crop/tile high-res images before counting.

## Run 6 — dedicated shelf-count pass (`eval/runs/cli-sonnet-shelf`) + third v0 repeat (`cli-sonnet-v0c`) — 2026-11-08
`--prompt shelf`: Sonnet, a prompt that only counts shelf levels (lists each level first, then counts). Same 30 images. Also a third repeat of plain v0 (run C) for variance; scorer cost field fixed (v0c mean cost ~$0.16/image subscription-equivalent).

| Metric | v0 A | v0 B | v0 C | v1 A | v1 B | Opus v1 | shelf-only |
|---|---|---|---|---|---|---|---|
| Shelf count exact | 55% | 48% | 66% (19/29) | 48% | 55% | 59% | 52% (15/29) |

Reading: three identical-prompt v0 runs span 48-66% on shelf count, so the dedicated pass (52%) is indistinguishable from baseline; a separate count pass does not fix it. Shelf-level counting is stuck near 50-60% regardless of prompt or tier, so a single-run difference of under ~18 pts means nothing on n=29. Other v0C numbers: gap FA 19%, tags 70%, facings 48%, brand recall 90%. Next lever left: image tiling/cropping, or accept ~55% and reframe the product around brand presence + gap check (which are reliable) rather than exact counts.

## Run 7 — video walk-through (src/video.mjs), 2026-11-08
Synthetic test only: a pan across eval img001 (1920x1440 wine shelf) cut into a 8 s clip (ffmpeg crop sweep), 1 fps, 8 frames, none deduped (the pan changes every frame), prompt v1 wording, Sonnet via `claude -p`.
- Labelled brands recovered: 3/3 (Auchan, Cave du Roi Dagobert, Hunawihr); gap false alarms: 0 (label has no gaps).
- Merged list had 6 entries: 3 real + 3 noise ("Alsace", "Vin d'Alsace", a verbose duplicate) — appellation words and name variants; merging needs fuzzy/containment dedupe.
- Cost-equiv $1.17 for 8 frames (subscription, not billed) — ~$0.15/frame, so video is expensive per walk-through.
- NOT a real handheld clip: no motion blur, no perspective change, no exposure shifts. Proves the pipeline runs, not that video works. A real clip is still needed. n=1.

## Run 8a — real handheld aisle clip: NOT RUN (no suitable CC clip), 2026-11-10
Searched Wikimedia Commons (video, namespace File:) for supermarket/aisle/grocery/shelves. Only candidate: "Super snel door een supermarkt" (1960s Dutch newsreel, CC BY-SA 3.0, 384x288, shoppers filling carts). Too low-res and not a shelf walk-through (labels unreadable), so running it would prove nothing; skipped. `eval/video/aisle8a.mp4` left by an earlier cycle is a truncated download (ffprobe: moov atom not found, no source recorded) and unusable. Video capability stays "pipeline works on synthetic pan only" (Run 7). A real test needs an owner phone clip: 20-30 s along one aisle (add to docs/SHOOTING_GUIDE.md).

## Run 9 — image tiling (`src/analyze-tiles.mjs`, `eval/runs/cli-sonnet-tiles`) — 2026-11-13
Each of the 30 images cut into 3 left-right tiles (15% overlap), v1-style presence+gap prompt per tile (Sonnet, `claude -p`), brands merged with the fuzzy word-subset merge, gaps = any tile. 90 calls, 1 tile failure (img024, other 2 tiles used). Shelf count/facings not produced (can't count across tiles), so only presence + gap scored.

| Metric | v0 A-C range | v1 A / B | Tiled |
|---|---|---|---|
| Brand recall | 90-93% | 92% / 91% | 95% (159/168) |
| Brand precision vs labels | 84% | 86% / 88% | 69% (159/229) |
| Gap recall | 100% | 89% / 100% | 78% (7/9) |
| Gap false alarm | 19-29% | 5% / 5% | 10% (2/21) |
| Cost-equiv / image | ~$0.16 | ~$0.16 | ~$0.44 (3 calls) |

Reading: NOISE / NOT KEPT. Recall +3-5 pts is inside the run-to-run spread; precision drops 17 pts (overlap double-reports and tile-edge fragments inflate the brand list: 229 vs ~182 names); gap recall falls to 78% (7/9; n=9 so one image is 11 pts); gap false alarm 10% is between v0 and v1. Triples cost and latency for no reliable gain. Presence + gap stay on single-image v1. Tiling dropped from the queue.
