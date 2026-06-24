# 04 Change Log

## Source snapshot

Snapshot:

```text
.heurema/rdlab/watch/snapshots/20260624T051742518067Z.json
```

Diff:

```text
.heurema/rdlab/watch/diffs/20260624T051742518067Z.json
```

## Changes detected

First snapshot for this project-local lab:

- added: 8 watched sources;
- changed: 0;
- removed: 0;
- unchanged: 0;
- failed: 0;
- skipped: 1 unwatched source.

## Run setup changes

- Created `.heurema/rdlab/` for `rd-lab-os`.
- Configured real `sources.toml` and `topics.toml`.
- Reused `providers.toml` from the subscription-only router template.
- Created project-local run:
  `.heurema/rdlab/runs/2026-06-24-rd-lab-os-idea-discovery-and-discussion/`.

## Follow-up watch notes

- `github_repo` source is registered but not snapshotted by the current minimal
  snapshot adapter.
- External URL snapshot confirms reachability and hash, not semantic content
  interpretation.
