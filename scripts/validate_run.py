#!/usr/bin/env python3
"""Validate a research run folder."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

LEGACY_REQUIRED = [
    "00_spec.md",
    "01_question_graph.md",
    "02_source_map.md",
    "03_evidence_ledger.csv",
    "04_contradictions.md",
    "05_synthesis.md",
    "06_critic_review.md",
    "07_final_memo.md",
    "08_decision_log.md",
]
PROJECT_LAB_REQUIRED = [
    "00_spec.md",
    "01_question_graph.md",
    "02_source_map.md",
    "03_evidence_ledger.csv",
    "04_change_log.md",
    "05_contradictions.md",
    "06_synthesis.md",
    "07_ideas.md",
    "08_experiments.md",
    "09_critic_review.md",
    "10_final_memo.md",
    "11_decision_log.md",
    "12_memory_update.md",
]

LEDGER_COLUMNS = [
    "id",
    "claim",
    "source_title",
    "source_url",
    "source_mode",
    "source_type",
    "date",
    "author_org",
    "evidence_quote_or_paraphrase",
    "confidence",
    "conflicts",
    "notes",
    "used_in_final",
]
PROFILES = {
    "legacy": LEGACY_REQUIRED,
    "project_lab": PROJECT_LAB_REQUIRED,
}


def nonempty_text(path: Path) -> bool:
    text = path.read_text(encoding="utf-8").strip()
    # template headings count as scaffold, not complete content; validation only checks existence by default
    return bool(text)


def has_content_beyond_template(path: Path) -> bool:
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("|"):
            continue
        if stripped in {"```text", "```"}:
            continue
        if stripped.endswith(":"):
            continue
        return True
    return False


def validate_ledger(path: Path, strict: bool) -> list[str]:
    errors: list[str] = []
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return ["ledger is empty"]
        rows = [row for row in reader if any(cell.strip() for cell in row)]
    missing = [col for col in LEDGER_COLUMNS if col not in header]
    if missing:
        errors.append("ledger missing columns: " + ", ".join(missing))
    if strict:
        if not rows:
            errors.append("ledger has no evidence rows")
    return errors


def detect_profile(root: Path) -> str:
    if (root / "12_memory_update.md").exists() or (root / "10_final_memo.md").exists():
        return "project_lab"
    if (root / "08_decision_log.md").exists() and (root / "07_final_memo.md").exists():
        return "legacy"
    if ".heurema/rdlab/runs" in root.as_posix():
        return "project_lab"
    return "legacy"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", help="Path to run folder")
    parser.add_argument("--profile", choices=sorted(PROFILES), help="Run profile. Auto-detected by default.")
    parser.add_argument("--strict", action="store_true", help="Require non-template evidence rows and final memo content")
    args = parser.parse_args()

    root = Path(args.run_dir).resolve()
    if not root.exists():
        raise SystemExit(f"Run folder does not exist: {root}")

    profile = args.profile or detect_profile(root)
    required = PROFILES[profile]
    errors: list[str] = []
    for name in required:
        path = root / name
        if not path.exists():
            errors.append(f"missing: {name}")
        elif not nonempty_text(path):
            errors.append(f"empty: {name}")
        elif args.strict and path.suffix == ".md" and not has_content_beyond_template(path):
            errors.append(f"template-only: {name}")

    ledger = root / "03_evidence_ledger.csv"
    if ledger.exists():
        errors.extend(validate_ledger(ledger, args.strict))

    if errors:
        print("Run validation failed:")
        for error in errors:
            print(f"  - {error}")
        raise SystemExit(1)

    print(f"Run scaffold OK ({profile}): {root}")
    print("Note: default validation checks structure. Use human/critic review for evidence quality.")


if __name__ == "__main__":
    main()
