# 07 Ideas

## Candidate ideas

| ID | Idea | Evidence rows | Confidence | Next step |
|---|---|---|---|---|
| I1 | Keep `idea_ledger_v2.csv` as current run-local handoff shape. | V2-2,V2-3,V2-4,V2-5 | high | Use v2 in one practical implementation-planning run. |
| I2 | Add a tiny `validate_idea_ledger.py` before template promotion. | V2-2,V2-5,V2-6 | medium-high | Validate columns, allowed statuses, and no disallowed status values. |
| I3 | Document status vocabulary before promotion. | V2-5,V2-6 | medium | Draft allowed statuses and transition rules. |

## Rejected ideas

| Idea | Reason |
|---|---|
| Promote v2 to templates immediately | It passed provider handoff but has not been used by a downstream implementation-planning run. |
| Remove update policy to keep CSV narrow | Would reintroduce the status inflation failure. |

## Open idea questions

- Should update policy be row-level forever, or generated from a smaller status
  policy table?
- Should `validate_idea_ledger.py` live in core scripts or project lab only?
