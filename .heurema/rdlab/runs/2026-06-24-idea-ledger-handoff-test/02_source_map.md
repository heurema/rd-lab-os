# 02 Source Map

## Project config sources

| Source ID | Source | Mode | Trust | Watch | Status |
|---|---|---|---|---|---|
| input-idea-ledger | previous run `idea_ledger.csv` | internal_doc | A | false | checked |
| agy-handoff-output | provider output | unknown | B | false | checked |
| claude-handoff-output | provider output | unknown | B | false | checked |

## Primary sources

| Priority | Source | Mode | Why it matters | Status |
|---|---|---|---|---|
| 1 | `.heurema/rdlab/runs/2026-06-24-idea-ledger-prototype/idea_ledger.csv` | internal_doc | Sole handoff input. | checked |
| 2 | Agy provider output | unknown | Shows one provider's update behavior. | checked |
| 3 | Claude provider output | unknown | Shows independent evidence-discipline behavior. | checked |

## Secondary sources

None.

## External source pass

This run is explicitly internal-only because it validates local artifact
handoff behavior. No external source can answer whether the current ledger
schema carries enough local context.

## Sources to avoid or treat carefully

| Source | Reason |
|---|---|
| Chat history | Excluded by test design. |
| Prior prose memos | Excluded by test design; only the CSV should carry handoff context. |
| Provider output | Useful for behavior observation, not authoritative truth. |
