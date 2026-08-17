#!/usr/bin/env python3
"""Validate all YAML files in the repository."""
import yaml
import sys
import glob

def main():
    failed = 0
    for f in sorted(glob.glob('**/*.yaml', recursive=True) + glob.glob('**/*.yml', recursive=True)):
        try:
            with open(f) as fh:
                yaml.safe_load(fh)
            print(f"  OK: {f}")
        except Exception as e:
            print(f"  FAIL: {f} — {e}")
            failed = 1
    sys.exit(failed)

if __name__ == "__main__":
    main()