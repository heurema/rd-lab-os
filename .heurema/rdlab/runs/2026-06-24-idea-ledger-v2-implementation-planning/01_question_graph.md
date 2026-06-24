# 01 Question Graph

## Root question

What is the smallest implementation step justified by
`idea_ledger_v2_normalized.csv` alone?

## Sub-questions

| ID | Question | Why it matters | Evidence rows |
|---|---|---|---|
| Q1 | Do providers choose validator/docs before template promotion? | Tests whether ledger encodes the right sequencing. | P2,P3 |
| Q2 | What exact file should be created? | Avoids clobbering evidence-ledger validator. | P4,P5 |
| Q3 | What should the validator check first? | Keeps implementation minimal. | P2,P3,P6 |
| Q4 | What remains deferred? | Prevents scope creep. | P2,P3,P7 |

## Perspectives

| Perspective | Concern |
|---|---|
| Coding agent | Needs exact next file and test scope. |
| Maintainer | Must avoid mixing evidence ledger and idea ledger semantics. |
| Critic | Must keep templates and automation deferred. |

## Evidence gaps

- No actual validator implementation has been written in this run.
- Provider plans did not inspect code except through the provided ledger.
- Naming was corrected by local repo inspection.
