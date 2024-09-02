from database.session import Base
from sqlalchemy import TIMESTAMP, Integer, DateTime
from sqlalchemy.orm import mapped_column, Mapped


class authenticated_user(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False,
                                    nullable=False, unique=True)

    class Config:
        from_attributes = True
