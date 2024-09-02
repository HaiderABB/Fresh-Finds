from sqlalchemy import Integer, Float, ForeignKey
from models.order import Order
from database.session import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship


class OrderItem(Base):
    __tablename__ = 'order_items'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'orders.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'products.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[Float] = mapped_column(Float)
    order: Mapped["Order"] = relationship("Order", back_populates="items")


class Config:
    from_attributes = True
