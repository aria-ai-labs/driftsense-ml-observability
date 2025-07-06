FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml .
RUN pip install --no-cache-dir poetry && poetry install --no-dev
COPY driftsense driftsense
COPY services/reporter services/reporter
CMD ["uvicorn", "services.reporter.app:app", "--host", "0.0.0.0", "--port", "8000"]