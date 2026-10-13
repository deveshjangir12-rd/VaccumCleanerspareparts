# VacuumKart demo API

This FastAPI service is a starter API for development previews. It deliberately uses in-memory storage and has no database persistence.

## Local run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

- `GET /` — service info
- `GET /health` — health check
- `GET /api/products` — demo catalogue (empty until a persistent catalogue is implemented)
- `POST /api/demo-orders` — creates a temporary demo order only when product IDs exist in the in-memory catalogue
- `GET /docs` — interactive API documentation

The admin product-write endpoint is disabled with HTTP 501 until proper authentication and persistent storage are implemented. Do not use this API for real customer or payment data.

## Render

Use root directory `backend`, build command `pip install -r requirements.txt`, and start command `uvicorn app.main:app --host 0.0.0.0 --port $PORT`. Set `CORS_ORIGINS` to the exact frontend origin after deployment.
