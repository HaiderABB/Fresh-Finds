from sqlalchemy import func, text
from sqlalchemy.orm import Session
from models.model import User


def register_user(user_data, db: Session):
    db.add(user_data)
    db.commit()
    db.refresh(user_data)


def user_exists(user_email, db: Session) -> bool:
    return db.query(User).filter(User.email == user_email).first() is not None
