# 05 Contradictions

## C1: Idea discovery needs structure, but too much structure becomes product bloat

- Evidence: E1, E3, E4, E7, E12.
- Tension: A dedicated idea ledger or scorecard could improve continuity, but
  adding too many new artifacts duplicates the existing project-lab template.
- Current resolution: test one lightweight artifact before expanding templates.

## C2: Provider debate is valuable, but scripted debate can become heavy orchestration

- Evidence: E5, E8, E10, E12.
- Tension: The user wants different providers to debate ideas, but the project
  explicitly avoids heavy multi-agent infrastructure.
- Current resolution: use `provider_router.py run/route/doctor` first; only add
  a tiny deterministic `debate_ideas.py` if repeated manual routing becomes
  friction.

## C3: Source watching can seed ideas, but raw diffs are not semantic insight

- Evidence: E9, E11, E12.
- Tension: Snapshot diffs can show that something changed, but not why it
  matters.
- Current resolution: keep change-brief generation as a candidate experiment,
  not a claimed finished feature.

## C4: Cross-project idea bridge is useful, but privacy and conflict boundaries are not solved

- Evidence: E6, E11.
- Tension: Cross-project labs could share idea patterns, but projects may contain
  sensitive or incompatible context.
- Current resolution: defer lab-to-lab sync until at least two project labs have
  validated idea artifacts and explicit sharing rules.

## C5: Semantic deduplication is attractive, but vector DB violates constraints

- Evidence: E1, E12.
- Tension: Deduping ideas across many runs would be useful, but embeddings/vector
  DBs conflict with stdlib-first/no-vector constraints.
- Current resolution: stop vector DB clustering for v0; use plain text/CSV and
  provider critique only.
