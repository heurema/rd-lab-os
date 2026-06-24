# 08 Experiments

## Candidate experiments

| ID | Hypothesis | Method | Evidence rows | Success criteria | Risk |
|---|---|---|---|---|---|
| X1a | A ledger with `critic_verdict` is enough for v0 idea triage. | Use `idea_ledger.csv` in one more run and ask two providers to update only `critic_verdict`, `status`, and `next_test`. | L4,L5,L7 | At least one status changes without editing prose sections. | CSV becomes cramped. |
| X1b | Score fields belong in the ledger, not a separate artifact. | Add `score_feasibility`, `score_impact`, and `scope_risk` in a copy of `idea_ledger.csv`. | L5,L7 | Scores change ordering or rejection of at least one idea. | False precision. |
| X2 | Manual debate remains sufficient for now. | Repeat one manual Claude/Agy or Claude/Vibe debate using provider_router.py. | L3,L5,L6 | Debate takes fewer than three commands and produces usable critique. | Provider reliability varies by prompt. |

## Experiment backlog

1. Run X1a next.
2. Run X1b only if X1a still leaves ambiguous priority.
3. Defer `debate_ideas.py` until manual debate is repeated.

## Experiments not worth running

- Discussion transcript parser.
- Pipeline report before three idea runs exist.
- Separate scorecard template before score fields are tested inside the ledger.
