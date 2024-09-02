from models.cart_item import CartItem
from models.order import Order
from database.session import Base
from sqlalchemy import TIMESTAMP, Integer, DateTime, String, Boolean, text
from sqlalchemy.orm import mapped_column, Mapped, relationship


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(100),  nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=True, unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'), nullable=False)

    orders: Mapped[list["Order"]] = relationship(
        "Order", back_populates="user")
    cart_items: Mapped[list["CartItem"]] = relationship(
        "CartItem", back_populates="user")


class Config:
    from_attributes = True
