# VacuumKart — vacuum cleaner spare-parts storefront

A responsive React + TypeScript + Vite demo storefront for an India-focused vacuum cleaner spare-parts shop, with a small optional FastAPI demo service.

## Local development

Requirements: Node.js 20+ and npm.

```bash
npm install
npm run dev
```

Production build:

```bash
npm run build
npm run preview
```

## Optional API

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs are available at `http://localhost:8000/docs`; health check at `/health`. The API's demo catalogue starts empty and its demo order data is stored in memory, so it resets when the process restarts. The storefront currently uses illustrative frontend catalogue data and does **not** submit orders to this API.

## Deploy on Render

The included `render.yaml` defines two services:

1. **vacuumkart** — static React frontend, built with `npm install && npm run build`, published from `dist`.
2. **vacuumkart-api** — optional FastAPI demo service rooted at `backend`.

You can deploy from Render by choosing **New + → Blueprint**, connecting this GitHub repository, and applying the blueprint. Check the generated service settings and CORS origin after Render creates the public frontend URL.

## Prototype limitations — read before taking live orders

- Product names, images, prices, ratings, stock, and compatibility are illustrative sample data. They are not verified parts listings or supplier inventory.
- Cart and checkout are frontend-only demonstration behaviour; no payment is taken and the frontend does not persist orders.
- The optional API uses temporary in-memory data, not PostgreSQL or another persistent database.
- There is no production customer login, authenticated admin panel, payment gateway, shipping integration, tax invoice flow, email/SMS notifications, refund workflow, or verified parts fitment database.
- Do not use this starter to accept real customer payments or store personal data until these systems and security controls are implemented and tested.

Never commit secrets or credentials. Use Render environment variables for future API keys and database URLs.
