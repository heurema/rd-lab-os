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
ALLOWED_MODES = {"academic", "official_docs", "code_repo", "benchmark", "product_docs", "market_news", "social_signal", "expert_blog", "internal_doc", "unknown"}
ALLOWED_CONFIDENCE = {"high", "medium", "low", "unknown", ""}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger")
    args = parser.parse_args()
    path = Path(args.ledger)
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        missing = [c for c in REQUIRED if c not in (reader.fieldnames or [])]
        if missing:
            raise SystemExit("Missing columns: " + ", ".join(missing))
        errors = []
        for i, row in enumerate(reader, start=2):
            if row.get("source_mode") not in ALLOWED_MODES:
                errors.append(f"row {i}: invalid source_mode {row.get('source_mode')!r}")
            if row.get("confidence") not in ALLOWED_CONFIDENCE:
                errors.append(f"row {i}: invalid confidence {row.get('confidence')!r}")
            if row.get("claim") and not row.get("evidence_quote_or_paraphrase"):
                errors.append(f"row {i}: claim without evidence")
    if errors:
        print("Ledger validation failed:")
        for e in errors:
            print(f"  - {e}")
        raise SystemExit(1)
    print(f"Ledger OK: {path}")


if __name__ == "__main__":
    main()
