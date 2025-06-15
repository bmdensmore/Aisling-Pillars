import json
import sys
import os
import csv

def load_schema(path):
    with open(path, "r") as f:
        return json.load(f)

def compare_values(v1, v2):
    old = {v["label"]: v["weight"] for v in v1["values"]}
    new = {v["label"]: v["weight"] for v in v2["values"]}

    all_labels = set(old) | set(new)
    diffs = []

    for label in sorted(all_labels):
        old_w = old.get(label)
        new_w = new.get(label)

        if old_w is None:
            diffs.append((label, "ADDED", None, new_w))
        elif new_w is None:
            diffs.append((label, "REMOVED", old_w, None))
        else:
            delta = new_w - old_w
            if abs(delta) > 0.01:
                diffs.append((label, "SHIFTED", old_w, new_w))

    return diffs

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_values.py values_day1.json values_day2.json")
        sys.exit(1)

    v1_path, v2_path = sys.argv[1], sys.argv[2]
    v1 = load_schema(v1_path)
    v2 = load_schema(v2_path)

    print(f"🔍 Comparing: {v1['version']} → {v2['version']}")
    print("-" * 50)

    changes = compare_values(v1, v2)

    if not changes:
        print("✅ No significant value drift detected.")
    else:
        for label, change, old, new in changes:
            print(f"{change:<8} {label:<30} {old if old is not None else '—'} → {new if new is not None else '—'}")

        # Save to CSV
        output_path = os.path.join("docs", "value_drift_report.csv")
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Label", "Change", "Old Weight", "New Weight"])
            for row in changes:
                writer.writerow(row)

        print(f"\n📄 Drift report saved to: {output_path}")
