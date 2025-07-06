from fastapi import FastAPI, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="DriftSense Reporter")

@app.get("/metrics", include_in_schema=False)
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/healthz", include_in_schema=False)
def health():
    return {"status":"ok"}