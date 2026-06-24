#!/usr/bin/env python3
"""Validate an idea ledger CSV."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


REQUIRED = ["idea_id", "status", "allowed_statuses", "update_policy", "status_update_reason"]


def has_any_value(row: dict[str, str | None]) -> bool:
    return any((value or "").strip() for value in row.values())


def split_allowed_statuses(value: str) -> list[str]:
    return [part.strip() for part in value.split("|") if part.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger")
    parser.add_argument("--strict", action="store_true", help="Require status update reasons and at least one row")
    args = parser.parse_args()

    path = Path(args.ledger)
    errors: list[str] = []
    rows = 0
    seen_ids: set[str] = set()

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = [column for column in REQUIRED if column not in (reader.fieldnames or [])]
        if missing:
            errors.append("missing columns: " + ", ".join(missing))
        else:
            for line_number, row in enumerate(reader, start=2):
                if not has_any_value(row):
                    continue
                rows += 1

                idea_id = (row.get("idea_id") or "").strip()
                status = (row.get("status") or "").strip()
                allowed_statuses = split_allowed_statuses((row.get("allowed_statuses") or "").strip())
                update_policy = (row.get("update_policy") or "").strip()
                status_update_reason = (row.get("status_update_reason") or "").strip()

                if not idea_id:
                    errors.append(f"row {line_number}: missing idea_id")
                elif idea_id in seen_ids:
                    errors.append(f"row {line_number}: duplicate idea_id {idea_id!r}")
                else:
                    seen_ids.add(idea_id)

                if not status:
                    errors.append(f"row {line_number}: missing status")
                if not allowed_statuses:
                    errors.append(f"row {line_number}: missing allowed_statuses")
                elif status and status not in allowed_statuses:
                    errors.append(
                        f"row {line_number}: status {status!r} is not in allowed_statuses "
                        f"{'|'.join(allowed_statuses)!r}"
                    )
                if not update_policy:
                    errors.append(f"row {line_number}: missing update_policy")
                if args.strict and not status_update_reason:
                    errors.append(f"row {line_number}: missing status_update_reason")

    if args.strict and rows == 0:
        errors.append("idea ledger has no rows")

    if errors:
        print("Idea ledger validation failed:")
        for error in errors:
            print(f"  - {error}")
        raise SystemExit(1)

    print(f"Idea ledger OK: {path}")


if __name__ == "__main__":
    main()
