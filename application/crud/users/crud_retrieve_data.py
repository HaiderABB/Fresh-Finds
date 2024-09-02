from sqlalchemy.orm import Session
from models.model import User


def crud_retrieve_user(user_id, db: Session) -> User:
    return db.query(User).filter(User.id == user_id).first()
