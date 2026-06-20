# Agent Instructions for R&D Lab OS

## Mission

Build and operate a reproducible deep-research workflow using existing AI agents, not custom model training.

## Default behavior

When asked to do research in this repo:

1. Create or update a run folder under `runs/YYYY-MM-DD-topic/`.
2. Fill artifacts in order.
3. Do not write `07_final_memo.md` before evidence exists.
4. Add claims to `03_evidence_ledger.csv` before synthesizing.
5. Run `scripts/validate_run.py` before declaring the run complete.

## Non-goals

- No model training.
- No custom multi-agent backend in v0.
- No UI before the artifact workflow works.
- No unlabelled blending of social, market, academic, official, and internal sources.

## Quality bar

A research run is valid only if:

- The scope is explicit.
- The question graph exists.
- Claims have ledger support.
- Contradictions and uncertainty are preserved.
- The critic pass is separate from synthesis.
- Recommendations trace back to evidence.
