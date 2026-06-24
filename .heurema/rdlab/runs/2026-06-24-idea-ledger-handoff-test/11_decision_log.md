# 11 Decision Log

## Entry

Date: 2026-06-24

Project: R&D Lab OS

Decision: Continue `idea_ledger.csv` as a handoff artifact, but require an
update-policy test before template promotion.

Reason: Providers could continue from the ledger alone, but one provider
over-promoted an idea status without sufficient evidence.

What this prevents:

- unsupported status inflation;
- premature template changes;
- assuming provider action equals evidence quality.

Next review: after X1c `idea_ledger_v2.csv` test.

Evidence: H1-H6.
