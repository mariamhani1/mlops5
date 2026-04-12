import os
import mlflow
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

flip_y = float(os.environ.get("FLIP_Y", "0.01"))

mlflow.set_tracking_uri("./mlruns")
mlflow.set_experiment("ml_pipeline_experiment")

X, y = make_classification(
    n_samples=1000, n_features=20, flip_y=flip_y, random_state=42
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

with mlflow.start_run() as run:
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, clf.predict(X_test))
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("flip_y", flip_y)
    mlflow.log_metric("accuracy", accuracy)
    run_id = run.info.run_id

print(f"Run ID: {run_id}")
print(f"Accuracy: {accuracy}")

with open("model_info.txt", "w") as f:
    f.write(run_id)

with open("accuracy.txt", "w") as f:
    f.write(str(accuracy))
