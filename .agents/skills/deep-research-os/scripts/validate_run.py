#!/usr/bin/env python3
"""Convenience wrapper for the repo-level validate_run.py script."""
from pathlib import Path
import runpy

root = Path(__file__).resolve().parents[4]
runpy.run_path(str(root / 'scripts' / 'validate_run.py'), run_name='__main__')
