# app/models.py
from pydantic import BaseModel, Field


class Item(BaseModel):
    id: int = Field(..., description="Item ID")
    name: str = Field(..., description="Item name")
    price: float = Field(..., ge=0, description="Item price")
