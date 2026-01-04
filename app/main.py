# app/main.py
from fastapi import FastAPI
from app.models import Item

app = FastAPI(title="Codespaces Sample API (uv)")


@app.get("/health")
def read_health():
    return {"status": "ok"}


@app.post("/items", response_model=Item)
def create_item(item: Item):
    return item
