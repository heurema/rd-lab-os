# 11 Decision Log

## Entry

Date: 2026-06-24

Project: R&D Lab OS

Decision: Implement `scripts/validate_idea_ledger.py` as the next code step.

Reason: Provider-only handoff from `idea_ledger_v2_normalized.csv` converged on
validator-before-template-promotion, and repo inspection showed the existing
`validate_ledger.py` is evidence-ledger-specific.

What this prevents:

- status inflation in idea ledgers;
- mixing evidence-ledger and idea-ledger semantics;
- premature template promotion.

Next review: after validator implementation and smoke checks.

Evidence: P1-P7.
