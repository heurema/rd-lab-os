# 07 Ideas

## Candidate ideas

| ID | Idea | Evidence rows | Confidence | Next step |
|---|---|---|---|---|
| I1 | Keep `idea_ledger.csv` as the primary idea handoff artifact. | H2,H3,H5,H6 | medium-high | Add update policy and run one more schema test. |
| I2 | Add `update_policy` or status rules to the ledger schema. | H4,H5,H6 | high | Prototype `idea_ledger_v2.csv` with update rules. |
| I3 | Treat provider refusal to update as a valid critic result. | H5 | high | Record refusals explicitly in critic review. |

## Rejected ideas

| Idea | Reason |
|---|---|
| Promote `validated` status from Agy output | No new evidence justified full validation. Evidence: H4,H6. |
| Require full memo context for handoff | The test goal is to keep handoff artifact compact. Evidence: H1. |

## Open idea questions

- Should update policy be one column per row or a run-level artifact?
- Should `candidate_validated_once` be an allowed status?
- Should `critic_verdict` and `status` be merged or kept separate?
