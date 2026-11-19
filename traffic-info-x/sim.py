#!/usr/bin/env python3
"""Traffic skill simulation runner.
Usage: python3 sim.py [--seed N] [--rounds 10]
"""
import argparse
import json
import random
from collections import Counter
from pathlib import Path

TRIGGERS = ["경로교통정보", "교통정보요약", "주변교통정보", "근처교통정보"]

def should_trigger(text: str) -> bool:
    t = text.replace(" ", "")
    return any(k in t for k in TRIGGERS)

def load_dataset():
    p = Path(__file__).parent / "evals" / "dataset.jsonl"
    if not p.exists():
        return []
    rows = []
    for line in p.read_text().splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows

def sim_output_risks(rng: random.Random) -> list:
    risks = []
    if rng.random() < 0.8:
        risks.append("날씨누락")
    if rng.random() < 0.5:
        risks.append("색상무시")
    if rng.random() < 0.4:
        risks.append("문장길어짐")
    return risks

def run_trigger_eval(dataset):
    tp = tn = fp = fn = 0
    for row in dataset:
        got = should_trigger(row["input"])
        expect = row["intent"] != "none"
        if got and expect:
            tp += 1
        elif not got and not expect:
            tn += 1
        elif got and not expect:
            fp += 1
        else:
            fn += 1
    total = tp + tn + fp + fn
    acc = (tp + tn) / total * 100 if total else 0
    return {"tp": tp, "tn": tn, "fp": fp, "fn": fn, "accuracy": acc}

def run_output_sim(rounds: int, rng: random.Random):
    all_risks = []
    results = []
    for i in range(1, rounds + 1):
        risks = sim_output_risks(rng)
        results.append({"round": i, "risks": risks, "pass": not risks})
        all_risks.extend(risks)
    return results, Counter(all_risks)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--rounds", type=int, default=10)
    args = ap.parse_args()
    rng = random.Random(args.seed)

    print("=== Trigger Eval ===")
    ds = load_dataset()
    if ds:
        te = run_trigger_eval(ds)
        print(f"  TP={te['tp']} TN={te['tn']} FP={te['fp']} FN={te['fn']}")
        print(f"  Accuracy: {te['accuracy']:.0f}%")
    else:
        print("  (no dataset)")

    print(f"\n=== Output Sim ({args.rounds} rounds, seed={args.seed}) ===")
    results, counts = run_output_sim(args.rounds, rng)
    for r in results:
        status = "PASS" if r["pass"] else "RISK: " + ", ".join(r["risks"])
        print(f"  [{r['round']}] {status}")
    print("\n=== Risk Counts ===")
    for k, v in counts.most_common():
        print(f"  {k}: {v}/{args.rounds}")

if __name__ == "__main__":
    main()
