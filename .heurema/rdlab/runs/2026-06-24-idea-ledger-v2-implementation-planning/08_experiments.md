# 08 Experiments

## Candidate experiments

| ID | Hypothesis | Method | Evidence rows | Success criteria | Risk |
|---|---|---|---|---|---|
| X1g | A tiny idea-ledger validator is enough guardrail for repeated handoff edits. | Implement `scripts/validate_idea_ledger.py` and run it against valid/invalid fixtures. | P5,P6 | Valid v2 ledger passes; invalid status, duplicate ID, missing policy fail. | Validator may grow beyond MVP. |

## Experiment backlog

1. Implement X1g.
2. Add status semantics docs.
3. Only then consider template promotion.

## Experiments not worth running

- Template promotion before validator.
- Debate automation before manual friction evidence.
- Score fields before validation.
