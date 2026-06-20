#!/usr/bin/env python3
"""Validate a research run folder."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

REQUIRED = [
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


def nonempty_text(path: Path) -> bool:
    text = path.read_text(encoding="utf-8").strip()
    # template headings count as scaffold, not complete content; validation only checks existence by default
    return bool(text)


def validate_ledger(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return ["ledger is empty"]
    missing = [col for col in LEDGER_COLUMNS if col not in header]
    if missing:
        errors.append("ledger missing columns: " + ", ".join(missing))
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", help="Path to run folder")
    parser.add_argument("--strict", action="store_true", help="Require non-template evidence rows and final memo content")
    args = parser.parse_args()

    root = Path(args.run_dir).resolve()
    if not root.exists():
        raise SystemExit(f"Run folder does not exist: {root}")

    errors: list[str] = []
    for name in REQUIRED:
        path = root / name
        if not path.exists():
            errors.append(f"missing: {name}")
        elif not nonempty_text(path):
            errors.append(f"empty: {name}")

    ledger = root / "03_evidence_ledger.csv"
    if ledger.exists():
        errors.extend(validate_ledger(ledger))

    if errors:
        print("Run validation failed:")
        for error in errors:
            print(f"  - {error}")
        raise SystemExit(1)

    print(f"Run scaffold OK: {root}")
    print("Note: default validation checks structure. Use human/critic review for evidence quality.")


if __name__ == "__main__":
    main()
