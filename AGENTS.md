# Agent Instructions for R&D Lab OS

## Mission

Build and operate a reproducible, portable deep-research workflow using existing AI agents, not custom model training.

## Default behavior

When asked to do research in this repo:

1. Create or update a run folder under `runs/YYYY-MM-DD-topic/`.
2. Fill artifacts in order.
3. Do not write `07_final_memo.md` before evidence exists.
4. Add claims to `03_evidence_ledger.csv` before synthesizing.
5. Run `scripts/validate_run.py` before declaring the run complete.

When asked to attach the lab to another project:

1. Use `.heurema/rdlab/` as the canonical project-local lab path.
2. Do not create `.rdlab/`.
3. Run `scripts/init_project.py <project-root>` if the project lab does not exist.
4. Read `.heurema/rdlab/rdlab.toml`, `sources.toml`, `topics.toml`, and `providers.toml` when present.
5. Create or update runs under `.heurema/rdlab/runs/YYYY-MM-DD-topic/`.
6. Use `scripts/new_run.py "<topic>" --project-root <project-root>` for project-local runs.
7. Use `scripts/provider_router.py` for subscription-only provider selection when a second provider/critic pass is needed.
8. Run `scripts/validate_project.py <project-root>` and `scripts/validate_run.py <run-folder>` before declaring the project-local workflow valid.

When a project-local run is idea-heavy:

1. Keep `07_ideas.md` as the normal run artifact.
2. Optionally copy `templates/idea_ledger/idea_ledger_v2.csv` into the run folder and replace the example row.
3. Use the idea ledger to track idea status, allowed status changes, and status update reasons.
4. Run `scripts/validate_idea_ledger.py <idea-ledger.csv> --strict`.
5. Do not make the idea ledger mandatory for non-idea research runs.

## Non-goals

- No model training.
- No custom multi-agent backend in v0.
- No UI before the artifact workflow works.
- No unlabelled blending of social, market, academic, official, and internal sources.
- No top-level `.rdlab/` directory.

## Quality bar

A research run is valid only if:

- The scope is explicit.
- The question graph exists.
- External sources were checked before synthesis, unless the run explicitly marks itself as internal-only and explains why.
- Claims have ledger support.
- Contradictions and uncertainty are preserved.
- The critic pass is separate from synthesis.
- Independent provider/agent critique was attempted when available; use `scripts/provider_router.py doctor --probe` to verify availability when practical.
- If only one agent/provider was used, or if a provider was blocked by auth, location, or token refresh, record that limitation explicitly.
- Idea status changes obey the row's idea-ledger update policy when an idea ledger is used.
- Recommendations trace back to evidence.

The evidence ledger remains the source of truth in both repo-local and project-local mode. Final memos are derivative artifacts.
