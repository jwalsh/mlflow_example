from mlflow import log_metric, log_param, log_artifact

if __name__ == "__main__":
    print('Log a parameter (key-value pair)')
    log_param("param1", 5)
    log_metric("foo", 1)
    log_metric("foo", 2)
    log_metric("foo", 3)

    # Log an artifact (output file)
    with open("output.txt", "w") as f:
        f.write("MLflow")
    log_artifact("output.txt")
