from sqlalchemy import Integer, TIMESTAMP, ForeignKey, text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.user import User

Base = declarative_base()


class CartItem(Base):
    __tablename__ = 'cart_items'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'users.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'products.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="cart_items")


class Config:
    from_attributes = True
