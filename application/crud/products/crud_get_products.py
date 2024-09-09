from sqlalchemy import or_
from sqlalchemy.orm import Session
from models.model import Product, Category


def get_products_params(name, price, user_category, db: Session):
    query = db.query(Product)
    if name:
        names = name.split()
        filter_conditions = [Product.product_name.ilike(
            f"%{word}%") for word in names]
        query = query.filter(or_(*filter_conditions))
    if price is not None:
        query = query.filter(Product.price <= price)
    if user_category:
        query = query.join(Category).filter(
            Category.category_name.ilike(f"%{user_category}"))
        print(query)

    products = query.all()
    return products


def get_product_id(product_id, db: Session):
    products = db.query(Product).filter(Product.id == product_id).first()
    return products
