import sys

THRESHOLD = 0.85

with open("model_info.txt", "r") as f:
    lines = f.read().strip().split("\n")
    run_id = lines[0]
    accuracy = float(lines[1])

print(f"Run ID:    {run_id}")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Threshold: {THRESHOLD}")

if accuracy < THRESHOLD:
    print(f"FAILED: {accuracy:.4f} < {THRESHOLD}")
    sys.exit(1)
else:
    print(f"PASSED: {accuracy:.4f} >= {THRESHOLD}")