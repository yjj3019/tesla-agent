#!/usr/bin/env python3
"""Automated eval pipeline for traffic-info-x skill."""
import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent
EVALS_PATH = SKILL_DIR / "evals" / "evals.json"
TRIGGERS_PATH = SKILL_DIR / "evals" / "triggers.json"
VALIDATOR = "/usr/share/grok/bundled-skills/bundled__postmortem/scripts/validate-skill.py"

def run_validator():
    print("=== Skill Structure Validation ===")
    result = subprocess.run(
        [sys.executable, VALIDATOR, str(SKILL_DIR)],
        capture_output=True, text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        return False
    return True

def load_json(path):
    if not path.exists():
        print(f"Missing: {path}")
        return None
    with open(path) as f:
        return json.load(f)

def summarize_evals():
    print("\n=== Eval Cases Summary ===")
    evals = load_json(EVALS_PATH)
    if not evals:
        return
    cases = evals.get("test_cases", [])
    print(f"Total test cases: {len(cases)}")
    for i, case in enumerate(cases, 1):
        name = case.get("name", f"case_{i}")
        assertions = len(case.get("assertions", []))
        print(f"  {i}. {name} ({assertions} assertions)")

def summarize_triggers():
    print("\n=== Trigger Cases Summary ===")
    triggers = load_json(TRIGGERS_PATH)
    if not triggers:
        return
    cases = triggers.get("test_cases", [])
    true_count = sum(1 for c in cases if c.get("should_trigger"))
    false_count = len(cases) - true_count
    print(f"Total triggers: {len(cases)} (should_trigger: {true_count}, negative: {false_count})")

def main():
    print("Running Automated Eval Pipeline for traffic-info-x\n")
    ok = run_validator()
    summarize_evals()
    summarize_triggers()
    print("\n=== Pipeline Complete ===")
    if ok:
        print("✅ Structure validation PASS")
        print("ℹ️  Assertion execution requires runtime skill invocation (manual or CI integration)")
    else:
        print("❌ Structure validation FAIL")
        sys.exit(1)

if __name__ == "__main__":
    main()
