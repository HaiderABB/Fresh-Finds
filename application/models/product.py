from sqlalchemy import TIMESTAMP, Float, ForeignKey, Integer, String, text, DateTime
from models.category import Category
from database.session import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    product_name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[Float] = mapped_column(Float, nullable=False)
    inventory_count: Mapped[int] = mapped_column(Integer, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'categories.id', ondelete='SET NULL', onupdate='CASCADE'))
    created_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'), nullable=False)
    category: Mapped["Category"] = relationship(
        "Category", back_populates="products")


class Config:
    from_attributes = True
