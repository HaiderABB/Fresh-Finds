from fastapi import Depends, APIRouter, HTTPException
from database.session import get_db
from sqlalchemy.orm import Session
from typing import Optional
from crud.products.crud_get_products import get_products_params


product_router = APIRouter(prefix="/FreshFinds")


@product_router.get("/products", status_code=200)
def get_products_query(name: Optional[str] = None, price: Optional[float] = None, category: Optional[str] = None, db: Session = Depends(get_db)):
    Products = get_products_params(name, price, category, db)
    return {"products": Products, "message": "Products Found"}
