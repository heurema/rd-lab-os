# 07 Ideas

## Candidate ideas

| ID | Idea | Evidence rows | Confidence | Next step |
|---|---|---|---|---|
| I1 | Keep testing `idea_ledger.csv` as a run-local artifact. | L1,L2,L4,L5 | medium-high | Use it again in one more idea run. |
| I2 | Add `debate_ideas.py` only after two manual debates show repeated friction. | L5 | medium | Run manual provider-router debate one more time. |
| I3 | Merge scorecard dimensions into ledger columns before adding a separate scorecard template. | L5,L7 | medium | Try score columns inside the ledger next. |

## Rejected ideas

| Idea | Reason |
|---|---|
| Discussion import script now | Agy marked it STOP; brittle parsing risk is high. Evidence: L5. |
| Global template promotion now | One run is insufficient; provider normalization still needed. Evidence: L4,L6. |

## Open idea questions

- Should `critic_verdict` be required or optional?
- Should score fields be numeric or categorical?
- Should stopped ideas remain in the ledger forever or move to rejected ideas
  only?
