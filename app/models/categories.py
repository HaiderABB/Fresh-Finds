from sqlalchemy import Column, Integer, DateTime, String, Boolean
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func
from App.database.session import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    category_name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
