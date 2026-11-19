#!/usr/bin/env python3
"""Test framework for traffic-info-x skill.
Usage: python3 test_framework.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DATASET = ROOT / "evals" / "dataset.jsonl"
SKILL = ROOT / "SKILL.md"

def load_jsonl(path):
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]

def check_skill_exists():
    ok = SKILL.exists()
    print(f"[{'OK' if ok else 'FAIL'}] SKILL.md exists")
    return ok

def check_description():
    text = SKILL.read_text() if SKILL.exists() else ""
    has = "description:" in text and "Trigger" in text
    print(f"[{'OK' if has else 'FAIL'}] description present")
    return has

def check_triggers(dataset):
    fails = 0
    for row in dataset:
        text = row["input"].replace(" ", "")
        keys = ["경로교통정보", "교통정보요약", "주변교통정보", "근처교통정보"]
        got = any(k in text for k in keys)
        expect = row["intent"] != "none"
        if got != expect:
            fails += 1
            print(f"  [MISMATCH] {row['input']} expect={expect} got={got}")
    ok = fails == 0
    print(f"[{'OK' if ok else 'FAIL'}] trigger consistency ({fails} mismatches)")
    return ok

def check_output_rules():
    text = SKILL.read_text() if SKILL.exists() else ""
    has_weather = "날씨" in text
    has_forbid = "전 구간 원활" in text or "전구간원활" in text
    has_voice = "입니다" in text
    ok = has_weather and has_forbid and has_voice
    print(f"[{'OK' if ok else 'FAIL'}] output rules (weather={has_weather}, forbid={has_forbid}, voice={has_voice})")
    return ok

def main():
    print("=== traffic-info-x Test Framework ===\n")
    results = []
    results.append(check_skill_exists())
    results.append(check_description())
    ds = load_jsonl(DATASET)
    print(f"[INFO] dataset rows: {len(ds)}")
    results.append(check_triggers(ds))
    results.append(check_output_rules())
    passed = sum(results)
    total = len(results)
    print(f"\n=== Result: {passed}/{total} passed ===")
    sys.exit(0 if passed == total else 1)

if __name__ == "__main__":
    main()
