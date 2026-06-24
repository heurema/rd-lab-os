# 06 Synthesis

## Summary

The `idea_ledger.csv` experiment is useful enough to continue, but not yet
strong enough to promote into global templates.

## What changed

The baseline had six candidate ideas. After this run:

- I1 is the strongest immediate mechanism.
- I2 is useful but should wait for repeated manual debate.
- I3 should be absorbed into ledger columns before adding a separate artifact.
- I4 and I5 are deferred.
- I6 is stopped for now.

## Artifact verdict

Use a run-local ledger with compact columns:

```text
idea_id,title,premise,evidence_rows,status,next_test,main_risk,critic_verdict
```

Add score fields only if a second run proves they change decisions:

```text
score_feasibility,score_impact,scope_risk
```

## Why not promote yet

One run is not enough to change `templates/run_project_lab/`. The ledger helped
normalize ideas, but the current run still needed human/operator normalization
of provider evidence IDs and statuses.

## Confidence

Medium. The artifact was helpful, and Agy critique changed decisions. The main
weakness is that Vibe did not provide a usable critique for this task.
