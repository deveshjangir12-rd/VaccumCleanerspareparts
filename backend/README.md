# VacuumKart demo API

## Local run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open `/docs` for the interactive API documentation. This API uses in-memory demo storage and is intended for development previews, not durable production orders. Replace the storage layer with PostgreSQL and add authenticated admin routes before live commerce.

## Render

Create a **Web Service** with root directory `backend`, build command `pip install -r requirements.txt`, and start command `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
