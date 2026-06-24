# 01 Question Graph

## Root question

Can `idea_ledger.csv` carry enough context for an agent to continue idea work
without reading chat history?

## Sub-questions

| ID | Question | Why it matters | Evidence rows |
|---|---|---|---|
| Q1 | Can providers parse the ledger and preserve idea IDs? | Basic handoff viability. | H1,H2,H3 |
| Q2 | Do providers update statuses only when justified? | Prevents roadmap inflation. | H3,H4,H5 |
| Q3 | Does the ledger need an explicit update policy column? | The current schema may be ambiguous. | H4,H5,H6 |
| Q4 | Is refusal to update a valid outcome? | Evidence discipline may require no-op changes. | H5,H6 |

## Perspectives

| Perspective | Concern |
|---|---|
| Handoff agent | Needs enough context to act. |
| Critic agent | Must not promote ideas without new evidence. |
| Maintainer | Needs stable CSV schema before template promotion. |

## Evidence gaps

- Only two providers were used for the handoff test.
- The test used a short prompt, not a complete scripted protocol.
- No separate human attempted to continue from the ledger.
