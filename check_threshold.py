import mlflow
import os
import sys

THRESHOLD = 0.85

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

tracking_uri = os.environ.get("MLFLOW_TRACKING_URI", "./mlruns")
mlflow.set_tracking_uri(tracking_uri)

client = mlflow.tracking.MlflowClient()
run = client.get_run(run_id)
accuracy = run.data.metrics["accuracy"]

print(f"Run ID: {run_id}")
print(f"Accuracy: {accuracy:.4f}")
print(f"Threshold: {THRESHOLD}")

if accuracy < THRESHOLD:
    print(f"FAILED: {accuracy:.4f} < {THRESHOLD}")
    sys.exit(1)
else:
    print(f"PASSED: {accuracy:.4f} >= {THRESHOLD}")