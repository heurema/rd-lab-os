# 08 Experiments

## Candidate experiments

| ID | Hypothesis | Method | Evidence rows | Success criteria | Risk |
|---|---|---|---|---|---|
| X1c | Adding update policy prevents unsupported status upgrades. | Create `idea_ledger_v2.csv` with `update_policy` and allowed status notes, then repeat Agy/Claude handoff. | H4,H5,H6 | Providers either preserve status or cite update policy when changing it. | More columns can make CSV harder to scan. |
| X1d | A run-level policy may be cleaner than a per-row policy column. | Add `idea_ledger_policy.md` next to CSV and repeat provider handoff. | H4,H6 | Providers follow policy without bloating CSV. | Agents may miss the policy file if only CSV is handed off. |

## Experiment backlog

1. Run X1c first because the user asked for agent handoff via the ledger itself.
2. Compare with X1d only if the CSV becomes too wide.

## Experiments not worth running

- Template promotion before update policy test.
- Debate script before manual debate friction is proven.
