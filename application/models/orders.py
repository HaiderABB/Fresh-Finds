from sqlalchemy import Column, Integer, Float, Boolean, TIMESTAMP, ForeignKey, text
from database.session import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey(
        'users.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    total_price = Column(Float)
    status = Column(Boolean, default=False, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'), nullable=False)


class Config:
    orm_mode = True
