from prometheus_client import Histogram

REQUEST_LATENCY = Histogram(
    "prediction_latency_seconds",
    "Prediction latency histogram",
    buckets=(0.05,0.1,0.25,0.5,1,2)
)