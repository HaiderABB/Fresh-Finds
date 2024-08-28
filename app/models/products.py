from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String, text
from App.database.session import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    product_name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    inventory_count = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey(
        'categories.id', ondelete='SET NULL', onupdate='CASCADE'))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'), nullable=False)
