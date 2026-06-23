#!/usr/bin/env python3
"""Validate an evidence ledger CSV."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

REQUIRED = [
    "id", "claim", "source_title", "source_url", "source_mode", "source_type",
    "date", "author_org", "evidence_quote_or_paraphrase", "confidence",
    "conflicts", "notes", "used_in_final"
]
OPTIONAL = ["topic_id", "source_id", "change_id"]
ALLOWED_MODES = {"academic", "official_docs", "code_repo", "benchmark", "product_docs", "market_news", "social_signal", "expert_blog", "internal_doc", "unknown"}
ALLOWED_CONFIDENCE = {"high", "medium", "low", "unknown", ""}


def has_any_value(row: dict[str, str | None]) -> bool:
    return any((value or "").strip() for value in row.values())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger")
    parser.add_argument("--strict", action="store_true", help="Require complete evidence rows")
    args = parser.parse_args()
    path = Path(args.ledger)
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        missing = [c for c in REQUIRED if c not in (reader.fieldnames or [])]
        if missing:
            raise SystemExit("Missing columns: " + ", ".join(missing))
        errors = []
        rows = 0
        for i, row in enumerate(reader, start=2):
            if not has_any_value(row):
                continue
            rows += 1
            source_mode = (row.get("source_mode") or "").strip()
            confidence = (row.get("confidence") or "").strip()
            claim = (row.get("claim") or "").strip()
            evidence = (row.get("evidence_quote_or_paraphrase") or "").strip()
            source_title = (row.get("source_title") or "").strip()
            source_url = (row.get("source_url") or "").strip()

            if source_mode and source_mode not in ALLOWED_MODES:
                errors.append(f"row {i}: invalid source_mode {row.get('source_mode')!r}")
            if confidence not in ALLOWED_CONFIDENCE:
                errors.append(f"row {i}: invalid confidence {row.get('confidence')!r}")
            if claim and not evidence:
                errors.append(f"row {i}: claim without evidence")
            if args.strict:
                if not row.get("id"):
                    errors.append(f"row {i}: missing id")
                if not claim:
                    errors.append(f"row {i}: missing claim")
                if not (source_title or source_url):
                    errors.append(f"row {i}: missing source_title or source_url")
                if not source_mode:
                    errors.append(f"row {i}: missing source_mode")
                if not evidence:
                    errors.append(f"row {i}: missing evidence_quote_or_paraphrase")
                if not confidence:
                    errors.append(f"row {i}: missing confidence")
        if args.strict and rows == 0:
            errors.append("ledger has no evidence rows")
    if errors:
        print("Ledger validation failed:")
        for e in errors:
            print(f"  - {e}")
        raise SystemExit(1)
    print(f"Ledger OK: {path}")


if __name__ == "__main__":
    main()
