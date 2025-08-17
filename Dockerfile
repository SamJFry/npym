FROM python:3.13.7-bookworm

COPY pyproject.toml /
COPY src/ /src/
COPY README.md /

RUN pip install . --no-cache-dir

CMD ["uvicorn", "npym.main:app", "--host", "0.0.0.0", "--port", "8000"]

