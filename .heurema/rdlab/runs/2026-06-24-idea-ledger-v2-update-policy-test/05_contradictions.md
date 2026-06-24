# 05 Contradictions

## C1: Policy fixes safety but increases CSV width

- Evidence: V2-2,V2-3,V2-4,V2-6.
- Tension: Row-level `update_policy` successfully guided providers, but makes
  the ledger heavier.
- Resolution: Keep v2 run-local until one practical idea run proves the width is
  acceptable.

## C2: Template promotion is tempting but still early

- Evidence: V2-3,V2-4,V2-5,V2-6.
- Tension: The safety failure is fixed in this run, but no implementation or
  downstream user workflow has consumed v2 yet.
- Resolution: Do not promote to templates yet; run one practical use case or add
  a small validator first.

## C3: Status vocabulary needs documentation

- Evidence: V2-2,V2-5.
- Tension: `candidate_validated_once` is precise but awkward.
- Resolution: Define allowed statuses before adding this to global templates.
