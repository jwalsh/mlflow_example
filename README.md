# MLflow

This is a review of MLflow specifically looking at the integration with SageMaker.

## Setup

``` shell
python3.6 -mvenv .venv
source .venv/bin/activate
pip install --upgrade pip
```

``` shell
pip install -r requirements.txt
```

## Running

``` shell
python -m mlflow_example
```


## Workflow

``` shell
mlflow ui && open http://localhost:5000/
```
