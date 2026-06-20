#!/usr/bin/env python3
"""Placeholder utility for future memory exports.

V0 intentionally keeps memory simple: markdown, csv, yaml.
"""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
print("Memory folders:")
for p in sorted((root / "memory").glob("*")):
    print(" -", p.relative_to(root))
