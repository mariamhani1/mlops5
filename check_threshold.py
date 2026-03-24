import sys
import os

THRESHOLD = 0.85

print("Files in directory:")
for f in os.listdir("."):
    print(f"  {f}")

with open("accuracy.txt", "r") as f:
    accuracy = float(f.read().strip())

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

print(f"Run ID:    {run_id}")
print(f"Accuracy:  {accuracy}")
print(f"Threshold: {THRESHOLD}")

if accuracy < THRESHOLD:
    print(f"FAILED: {accuracy} < {THRESHOLD}")
    sys.exit(1)
else:
    print(f"PASSED: {accuracy} >= {THRESHOLD}")