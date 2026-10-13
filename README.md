# VacuumKart — vacuum cleaner spare-parts storefront

A modern, animated React + TypeScript + Vite demo storefront for an India-focused vacuum-cleaner spare-parts shop. Includes illustrative multi-brand products and prices so you can explore the shopping journey immediately.

## Run the storefront

Requirements: Node.js 20+ and npm.

```bash
npm install
npm run dev
```

Build for deployment:

```bash
npm run build
npm run preview
```

## Run the demo API (optional)

In a second terminal:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs: `http://localhost:8000/docs`. The API starts with an empty SQLite database by design. Catalogue entries in the frontend are illustrative demo data, not verified real-world parts.

## Important prototype boundaries

This is a functional UI/demo journey, not a production commerce system. The frontend checkout creates browser-local demo orders and does not charge payments. Authentication, real payment processing, shipping, notifications, GST invoices, returns/refunds, admin authentication, supplier imports, and a verified model/part catalogue still need implementation before live sales. The `/admin` screen and `POST /api/admin/products` endpoint are demonstration-only and must not be exposed publicly without authentication.

Keep real secrets in environment variables, never in frontend code or Git.
