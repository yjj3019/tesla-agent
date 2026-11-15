#!/usr/bin/env python3
"""Simple validation runner for traffic-info-x skill."""
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent
VALIDATOR = "/usr/share/grok/bundled-skills/bundled__postmortem/scripts/validate-skill.py"

def main():
    print("Running traffic-info-x skill validation...")
    result = subprocess.run(
        [sys.executable, VALIDATOR, str(SKILL_DIR)],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode

if __name__ == "__main__":
    sys.exit(main())
