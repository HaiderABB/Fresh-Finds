from sqlalchemy import or_
from sqlalchemy.orm import Session
from models.model import Product, Category


def get_products_params(name, price, user_category, db: Session):
    query = db.query(Product)
    if name:
        names = name.split()
        products = query.all()
        filter_conditions = [Product.product_name.ilike(
            f"%{word}%") for word in names]
        products = query.filter(or_(*filter_conditions)).all()
        return products
    elif price:
        query = query.filter(Product.price <= price)
        products = query.all()
        return products
    elif user_category:
        query = db.query(Product).join(Category)
        query = query.filter(Category.category_name.ilike(f"%{user_category}"))
        products = query.all()
        return products
    else:
        products = query.all()
        return products


def get_product_id(product_id, db: Session):
    products = db.query(Product).filter(Product.id == product_id).first()
    return products
