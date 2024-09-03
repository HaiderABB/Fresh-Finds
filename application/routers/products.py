from fastapi import Depends, APIRouter, HTTPException
from database.session import get_db
from sqlalchemy.orm import Session
from typing import Optional


product_router = APIRouter(prefix="/FreshFinds")


@product_router.get("/products", status_code=200)
def get_products_query(name: Optional[str], price):
    return {"name": name}
