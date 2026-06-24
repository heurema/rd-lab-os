# 02 Source Map

## Project config sources

| Source ID | Source | Mode | Trust | Watch | Status |
|---|---|---|---|---|---|
| normalized-v2-ledger | `idea_ledger_v2_normalized.csv` | internal_doc | A | false | checked |
| claude-plan | `claude_implementation_plan.md` | unknown | B | false | checked |
| agy-plan | `agy_implementation_plan.md` | unknown | B | false | checked |
| existing-evidence-validator | `scripts/validate_ledger.py` | code_repo | A | true | checked |

## Primary sources

| Priority | Source | Mode | Why it matters | Status |
|---|---|---|---|---|
| 1 | `idea_ledger_v2_normalized.csv` | internal_doc | Sole provider input. | checked |
| 2 | Claude implementation plan | unknown | Independent plan from one provider. | checked |
| 3 | Agy implementation plan | unknown | Independent plan from second provider. | checked |
| 4 | `scripts/validate_ledger.py` | code_repo | Confirms existing file is for evidence ledger. | checked |

## Secondary sources

None.

## External source pass

Internal-only by design. This run validates implementation sequencing from a
local artifact and repo file inventory.

## Sources to avoid or treat carefully

| Source | Reason |
|---|---|
| Provider proposed filename `validate_ledger.py` | Conflicts with existing evidence-ledger validator. |
| Prior chat | Excluded by handoff test design. |
