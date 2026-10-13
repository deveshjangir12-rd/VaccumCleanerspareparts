from __future__ import annotations
from typing import Literal
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import os

app = FastAPI(title="VacuumKart Demo API", version="1.0.0", description="Starter API for a vacuum cleaner spare-parts storefront.")
origins = [x.strip() for x in os.getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",") if x.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=False, allow_methods=["GET", "POST", "OPTIONS"], allow_headers=["*"])

class Product(BaseModel):
    id: str
    name: str = Field(min_length=2, max_length=160)
    brand: str = Field(min_length=1, max_length=100)
    category: str = Field(min_length=1, max_length=80)
    price: int = Field(gt=0, le=10000000)
    description: str = Field(default="", max_length=2000)
    compatibility: list[str] = Field(default_factory=list, max_length=30)
    stock: int = Field(default=0, ge=0, le=1000000)

class OrderLine(BaseModel):
    product_id: str
    quantity: int = Field(ge=1, le=99)

class DemoOrderRequest(BaseModel):
    customer_name: str = Field(min_length=2, max_length=120)
    email: str
    items: list[OrderLine] = Field(min_length=1, max_length=50)

# Deliberately in-memory demo state: data resets when the service restarts.
_catalog: dict[str, Product] = {}
_orders: list[dict] = []

@app.get("/")
def root():
    return {"service": "VacuumKart Demo API", "docs": "/docs", "health": "/health", "notice": "Prototype only; orders and catalogue are not persisted."}

@app.get("/health")
def health():
    return {"status": "ok", "service": "vacuumkart-api"}

@app.get("/api/products", response_model=list[Product])
def list_products(q: str | None = Query(default=None, max_length=120), category: str | None = Query(default=None, max_length=80)):
    products = list(_catalog.values())
    if q:
        term = q.casefold()
        products = [p for p in products if term in " ".join([p.name, p.brand, p.category, *p.compatibility]).casefold()]
    if category and category.casefold() != "all parts":
        products = [p for p in products if p.category.casefold() == category.casefold()]
    return products

@app.get("/api/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    if product_id not in _catalog:
        raise HTTPException(status_code=404, detail="Product not found")
    return _catalog[product_id]

@app.post("/api/demo-orders", status_code=201)
def create_demo_order(order: DemoOrderRequest):
    lines = []
    total = 0
    for line in order.items:
        product = _catalog.get(line.product_id)
        if product is None:
            raise HTTPException(status_code=400, detail=f"Unknown product: {line.product_id}")
        if line.quantity > product.stock:
            raise HTTPException(status_code=409, detail=f"Insufficient demo stock for {product.name}")
        total += product.price * line.quantity
        lines.append({"product_id": product.id, "name": product.name, "quantity": line.quantity, "unit_price": product.price})
    order_id = f"VK-DEMO-{len(_orders) + 1:05d}"
    result = {"order_id": order_id, "status": "demo_only", "customer_name": order.customer_name, "email": order.email, "items": lines, "subtotal": total, "message": "Demo order only. No payment was collected; this order is held in temporary memory."}
    _orders.append(result)
    return result

@app.get("/api/demo-orders")
def list_demo_orders():
    return {"orders": _orders, "notice": "Demo data only. Do not use this endpoint for real customer records."}

@app.post("/api/admin/products", status_code=201, response_model=Product)
def demo_add_product(product: Product):
    # Not secure: deliberately disabled until real admin authentication is implemented.
    raise HTTPException(status_code=501, detail="Admin product writes are disabled in this starter. Add authenticated admin access and persistent storage first.")
