from sqlalchemy import Integer, Float, Boolean, TIMESTAMP, ForeignKey, text, DateTime
from models.order_item import OrderItem
from models.user import User
from database.session import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'users.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    total_price: Mapped[Float] = mapped_column(Float)
    status: Mapped[Boolean] = mapped_column(
        Boolean, default=False, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="orders")
    items: Mapped[list["OrderItem"]] = relationship(
        "OrderItem", back_populates="order")


class Config:
    from_attributes = True
