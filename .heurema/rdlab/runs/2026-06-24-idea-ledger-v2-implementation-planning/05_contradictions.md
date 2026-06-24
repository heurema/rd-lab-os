# 05 Contradictions

## C1: Provider suggested validator name conflicts with existing file

- Evidence: P2,P3,P4,P5.
- Tension: Providers suggested `validate_ledger.py`, but the repo already uses
  that name for evidence ledger validation.
- Resolution: Use `scripts/validate_idea_ledger.py`.

## C2: Validator vs documentation first

- Evidence: P1,P2,P3,P6.
- Tension: Documentation would explain semantics, but a validator gives direct
  mechanical protection against status inflation.
- Resolution: Implement validator first; document status semantics after the
  validator contract stabilizes.

## C3: Template promotion is now closer but still premature

- Evidence: P1,P7.
- Tension: v2 passed provider handoff and implementation planning, but no
  validator exists yet.
- Resolution: Defer template promotion until validator and status docs exist.
