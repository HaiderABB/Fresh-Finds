from sqlalchemy import TIMESTAMP, Column, Integer, DateTime, String, Boolean, text, true
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func
from application.database.session import Base


class users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=true, autoincrement=True,
                nullable=False, unique=True)
    username = Column(String(100),  nullable=False)
    email = Column(String(255), nullable=True, unique=True)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'), nullable=False)
