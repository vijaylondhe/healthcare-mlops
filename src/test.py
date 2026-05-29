import mlflow
from mlflow.tracking import MlflowClient

print("1")

mlflow.set_tracking_uri("http://127.0.0.1:5001")

print("2")

client = MlflowClient()

print("3")

exp = client.get_experiment_by_name("healthcare-risk-classification")

print("4")
print(exp)