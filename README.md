# DriftSense

DriftSense is a lightweight **model-observability toolkit**.

* **SDK** – single import to push prediction scores & PSI drift metrics.  
* **Reporter service** – FastAPI app exposing `/metrics` and `/healthz`.  
* **Helm chart** – one-line deploy to any Kubernetes cluster.

```python
from driftsense.sdk import monitor
monitor(pred=0.76, feature_drift={"age":0.08})
```
