# VacuumKart — vacuum cleaner spare-parts storefront

A modern, responsive React + TypeScript + Vite storefront for an India-focused vacuum cleaner spare-parts shop, with an optional FastAPI starter API.

## Current UI preview

The storefront includes:
- Responsive desktop and mobile layouts with product search, category filters and sorting.
- Product cards, quick-view details, favourites, a shopping bag and quantity controls.
- A model fit-finder to narrow the sample catalogue.
- Category discovery cards, support/contact section and a newsletter UI preview.
- A **Product Studio** screen with sample catalogue stats and local add/edit/delete controls.
- A responsive design system with reusable colours, typography, cards, spacing and reduced-motion support.

The sample products, prices, ratings, stock, photos and compatibility notes are illustrative only. They are not verified listings or supplier inventory.

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

## Product Studio demo

Use the floating **Product studio** control or the footer link to open the product management UI. Add, edit and remove actions currently update React state in the browser only. Changes are lost on refresh; this is not a secure admin panel and does not write to the API or a database.

## Optional API

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs: `http://localhost:8000/docs`; health check: `/health`. The current API uses temporary in-memory state. The storefront currently uses its sample frontend catalogue and does not submit orders to the API.

## Deploy on Render

The included `render.yaml` defines two services:

1. **vacuumkart** — static React frontend, built with `npm install && npm run build`, published from `dist`.
2. **vacuumkart-api** — optional FastAPI starter service rooted at `backend`.

Deploy from Render using **New + → Blueprint**, connect this repository, and review the service settings and CORS origin after Render creates the frontend URL.

## Planned next steps

1. Connect the storefront to a Neon PostgreSQL database and serve product listings from the API.
2. Add persistent product, stock and order models with schema migrations.
3. Add secure admin authentication and server-side product CRUD.
4. Connect cart/checkout to the backend with validated order totals and stock checks.
5. Integrate a payment gateway (for example Razorpay) using server-side verification and environment variables.
6. Add shipping, order-status updates, transactional notifications, privacy/legal pages and tests.

## Important limitations

- Product Studio is a UI prototype, not production admin authentication.
- Product, cart and newsletter interactions are demo-only; data is not persisted.
- No real payment is collected. Do not use this starter to accept real customer payments or store personal data until database persistence, authentication, payment verification, security controls and end-to-end testing are implemented.
- Never commit secrets or credentials. Configure database URLs and API keys through Render environment variables.
