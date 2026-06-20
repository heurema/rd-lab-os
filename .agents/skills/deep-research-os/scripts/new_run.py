#!/usr/bin/env python3
"""Convenience wrapper for the repo-level new_run.py script."""
from pathlib import Path
import runpy

root = Path(__file__).resolve().parents[4]
runpy.run_path(str(root / 'scripts' / 'new_run.py'), run_name='__main__')
