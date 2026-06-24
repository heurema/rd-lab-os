# 02 Source Map

## Project config sources

| Source ID | Source | Mode | Trust | Watch | Status |
|---|---|---|---|---|---|
| previous-normalized-ledger | `handoff_normalized_idea_ledger.csv` | internal_doc | A | false | checked |
| v2-input-ledger | `idea_ledger_v2_input.csv` | internal_doc | A | false | checked |
| agy-v2-output | `agy_v2_handoff_output.csv` | unknown | B | false | checked |
| claude-v2-output | `claude_v2_handoff_output.csv` | unknown | B | false | checked |

## Primary sources

| Priority | Source | Mode | Why it matters | Status |
|---|---|---|---|---|
| 1 | `idea_ledger_v2_input.csv` | internal_doc | Contains update policy under test. | checked |
| 2 | Agy v2 output | unknown | Shows whether Agy still over-promotes. | checked |
| 3 | Claude v2 output | unknown | Shows independent behavior on same input. | checked |

## Secondary sources

| Priority | Source | Mode | Why it matters | Status |
|---|---|---|---|---|
| 1 | Previous handoff final memo | internal_doc | Defines why v2 is needed. | checked |

## External source pass

Internal-only by design. The run validates local artifact policy behavior.

## Sources to avoid or treat carefully

| Source | Reason |
|---|---|
| Provider output | Behavior evidence, not product truth. |
| Previous chat | Excluded by handoff test design. |
