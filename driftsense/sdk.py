"""
DriftSense lightweight SDK.

Usage:
    from driftsense.sdk import monitor
    monitor(pred=0.63, feature_drift={"age":0.04,"dx_code":0.11})
"""
from prometheus_client import Histogram, Gauge, CollectorRegistry, push_to_gateway
from typing import Dict

_REGISTRY = CollectorRegistry()
_pred_hist = Histogram(
    "model_prediction_score",
    "Distribution of model prediction scores",
    buckets=[i/20 for i in range(21)],
    registry=_REGISTRY,
)
_drift_gauge = Gauge(
    "model_feature_drift_psi",
    "Population stability index for features",
    ["feature"],
    registry=_REGISTRY,
)

def monitor(pred: float, feature_drift: Dict[str, float], push_gateway: str = None):
    """Record prediction and feature drift metrics.

    Args:
        pred: model score between 0 and 1
        feature_drift: mapping feature -> PSI
        push_gateway: optional Prometheus Pushgateway URL
    """
    _pred_hist.observe(pred)
    for feat, psi in feature_drift.items():
        _drift_gauge.labels(feat).set(psi)
    if push_gateway:
        push_to_gateway(push_gateway, job="driftsense_sdk", registry=_REGISTRY)
