# 01 Question Graph

## Root question

How should `rd-lab-os` support agent-run idea discovery and discussion while
staying evidence-ledger-first, portable, stdlib-first, and lightweight?

## Sub-questions

| ID | Question | Why it matters | Evidence rows |
|---|---|---|---|
| Q1 | What is already present for idea workflows? | Avoid rebuilding surfaces that already exist. | E1,E6,E7 |
| Q2 | What is missing between source snapshots and actionable ideas? | This is likely the next workflow gap. | E8,E9,E11 |
| Q3 | How should provider debate be represented without heavy orchestration? | The user observed that one agent deciding alone is insufficient. | E5,E8,E10,E12 |
| Q4 | How should ideas be triaged and promoted? | Ideas should not remain chat-only or become memory too early. | E3,E7,E12 |
| Q5 | Which next experiment is smallest and most reversible? | The project should avoid backend/UI/vector DB creep. | E1,E4,E12 |

## Perspectives

| Perspective | Primary concern |
|---|---|
| Operator | Agents should do source/provider passes and leave durable artifacts. |
| Maintainer | Keep scripts small, stdlib-only, and easy to inspect. |
| Critic | Prevent provider theater, overbuilt orchestration, and unsupported ideas. |
| Product owner | Turn repeated research friction into practical workflows. |

## Controversies

- Whether a dedicated `idea_ledger.csv` is useful or duplicates `07_ideas.md`.
- Whether provider debate should be scripted now or remain manual command
  routing via `provider_router.py`.
- Whether idea promotion should write top-level `.heurema/rdlab/ideas/`
  artifacts during v0 or only after repeated validated runs.

## Evidence gaps

- No real multi-week history of project-local idea runs yet.
- No user-tested friction data from multiple projects yet.
- Provider outputs are useful critique but not a substitute for observed
  repeated workflow failures.
