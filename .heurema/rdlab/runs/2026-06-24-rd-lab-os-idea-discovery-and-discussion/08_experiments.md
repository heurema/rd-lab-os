# 08 Experiments

## Candidate experiments

| ID | Hypothesis | Method | Evidence rows | Success criteria | Risk |
|---|---|---|---|---|---|
| X1 | A minimal idea ledger improves continuity more than extending prose-only `07_ideas.md`. | Add a run-local `idea_ledger.csv` in the next idea run and ask two providers to critique the same rows. | E3,E4,E7,E12 | Agent can extract, critique, and update ideas without reading chat history. | Artifact duplication if `07_ideas.md` is enough. |
| X2 | Manual provider debate through `provider_router.py` is enough for v0. | Run one more idea debate using Claude/Vibe/Agy and record results in `09_critic_review.md`. | E5,E8,E10,E12 | Debate is traceable and takes fewer than three commands. | Manual routing may be inconsistent across agents. |
| X3 | A tiny scorecard catches weak ideas before implementation. | Create a run-local `idea_scorecard.csv` with feasibility, evidence, risk, and next-test columns. | E3,E7,E12 | At least one idea is downgraded or rejected with a documented reason. | Scores may create false precision. |
| X4 | Snapshot diffs can seed change-brief ideas without semantic diff automation. | Use the latest diff JSON to create a run scaffold and manually fill the first change log. | E9,E11 | New run opens with changed/added/failed sources already listed. | Could duplicate `snapshot_sources.py` output. |

## Experiment backlog

- X1 should run first.
- X2 can run in parallel with X1 because it uses existing `provider_router.py`.
- X3 should wait until at least 3 candidate ideas are in a ledger.
- X4 should wait for a second snapshot so there is a real changed/unchanged
  comparison.

## Experiments not worth running

- Vector/embedding deduplication in v0.
- UI dashboard for ideas before artifacts prove useful.
- Multi-agent framework integration before a plain provider-router loop is
  proven insufficient.
