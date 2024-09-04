from fastapi import Depends, APIRouter, HTTPException
from database.session import get_db
from sqlalchemy.orm import Session
from typing import Optional
from crud.products.crud_get_products import get_products_params as crud_get_products, get_product_id as crud_product_by_id
from schemas.products import product_by_id


product_router = APIRouter(prefix="/FreshFinds")


@product_router.get("/products", status_code=200)
def get_products_params(name: Optional[str] = None, price: Optional[float] = None, category: Optional[str] = None, db: Session = Depends(get_db)):
    Products = crud_get_products(name, price, category, db)
    return {"products": Products, "message": "Products Found"}


@product_router.get("/product", status_code=200)
def get_product_by_id(payload: product_by_id, db: Session = Depends(get_db)):
    products = crud_product_by_id(payload.product_id, db)
    if products is None:
        raise HTTPException(status_code=404, detail={
                            "products": None, "message": "No products found"})
    else:
        return {"products": products, "message": "Found products"}
