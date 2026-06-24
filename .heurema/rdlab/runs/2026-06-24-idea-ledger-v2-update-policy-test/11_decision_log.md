# 11 Decision Log

## Entry

Date: 2026-06-24

Project: R&D Lab OS

Decision: Accept `idea_ledger_v2.csv` as the current run-local handoff shape,
but do not promote it to global templates yet.

Reason: Explicit update policy prevented the unsupported status upgrade
observed in the previous handoff test.

What this prevents:

- provider-driven status inflation;
- premature template churn;
- ambiguous status transitions.

Next review: after X1f implementation-planning handoff test.

Evidence: V2-1 through V2-6.
