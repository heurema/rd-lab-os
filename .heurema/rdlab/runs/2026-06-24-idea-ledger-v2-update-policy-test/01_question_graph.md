# 01 Question Graph

## Root question

Does explicit update policy in `idea_ledger_v2.csv` prevent unsupported provider
status upgrades?

## Sub-questions

| ID | Question | Why it matters | Evidence rows |
|---|---|---|---|
| Q1 | Can both providers parse and return v2 ledger CSV? | Basic schema viability. | V2-1,V2-2,V2-3 |
| Q2 | Do providers preserve status without new evidence? | Tests whether policy fixes previous failure. | V2-2,V2-3,V2-4 |
| Q3 | Is row-level update policy enough to guide behavior? | Determines next schema direction. | V2-4,V2-5 |
| Q4 | Is the ledger ready for template promotion? | Avoids premature template churn. | V2-5,V2-6 |

## Perspectives

| Perspective | Concern |
|---|---|
| Handoff agent | Must know what can change. |
| Critic | Must avoid unsupported promotion. |
| Maintainer | Must keep schema usable and not too wide. |

## Evidence gaps

- No real downstream implementation test exists yet.
- This run used two providers only.
- Row-level policy may be verbose for long-term templates.
