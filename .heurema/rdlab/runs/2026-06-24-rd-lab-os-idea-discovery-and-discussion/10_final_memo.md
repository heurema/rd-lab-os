# 10 Final Memo

## Decision

Start the idea discovery/discussion lab inside `rd-lab-os` as a project-local
`.heurema/rdlab/` workflow, using source snapshots, evidence ledger rows, and
subscription provider critique before promoting any idea.

## Recommendation

Run the first implementation experiment around a run-local `idea_ledger.csv`.
Do not add a backend, UI, vector DB, or multi-agent framework. Do not add
`debate_ideas.py` until manual provider-router debate has been repeated and the
manual commands become real friction.

## Why

The repository already contains the necessary project-local lab structure,
idea/experiment artifacts, source snapshots, and provider routing. The first
useful step is to make ideas more inspectable and comparable inside the
artifact workflow. Evidence: E1-E12.

## Next task for an agent

Create a second project-local run or branch experiment that adds a run-local
`idea_ledger.csv` prototype and tests whether Claude/Vibe/Agy can:

1. extract ideas from `07_ideas.md`;
2. critique each idea independently;
3. update status without inventing evidence;
4. validate the run afterward.

## Explicitly deferred

- Cross-project idea sync.
- Vector/embedding deduplication.
- UI/dashboard.
- Automated semantic diffing.
- Provider debate framework beyond the existing subscription router.
