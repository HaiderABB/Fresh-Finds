from sqlalchemy import Integer, String, list
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.product import Product
from database.session import Base


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    category_name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    products: Mapped[list["Product"]] = relationship(
        "Product", back_populates="category")


class Config:
    from_attributes = True
