# 06 Synthesis

## Summary

The first idea-discovery lab should not add a new system. The strongest path is
to make ideas first-class artifacts inside the existing project-local run
workflow, then add one small helper only after the artifact shape proves useful.

## What the evidence supports

1. The repository already has the right boundaries: portable project lab,
   evidence ledger, provider router, source snapshots, ideas, experiments, and
   memory update artifacts. Evidence: E1-E8.
2. The first snapshot and provider probe completed successfully, so this run has
   a valid source and provider baseline. Evidence: E9-E10.
3. Independent provider outputs converge on three near-term mechanisms:
   idea ledger, provider debate, and idea triage/scorecards. Evidence: E11-E12.

## Recommended ordering

1. Keep this first run as the baseline idea discussion record.
2. Add a minimal idea ledger experiment before adding a new orchestration script.
3. Use `provider_router.py` manually for the next 1-2 idea debates.
4. If manual routing repeats, add a tiny `scripts/debate_ideas.py`.
5. Defer cross-project sync and semantic clustering.

## Why this order

An idea ledger creates a stable unit of discussion without requiring backend,
UI, vector DB, or a new agent framework. Provider debate can then critique those
idea rows. Scorecards can come after there are enough ideas to compare.

## Current confidence

Medium-high. The repo evidence strongly supports artifact-first ideation, and
two external provider passes independently support ledger/debate/triage. The
main uncertainty is whether operators will prefer a new `idea_ledger.csv` or a
richer `07_ideas.md` table.
