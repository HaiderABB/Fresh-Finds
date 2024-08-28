from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database.session import Base


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    order_id = Column(Integer, ForeignKey(
        'orders.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey(
        'products.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float)


class Config:
    orm_mode = True
