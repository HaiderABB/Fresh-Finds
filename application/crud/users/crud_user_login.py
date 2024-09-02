from sqlalchemy import func, text
from sqlalchemy.orm import Session
from utils.password_hash import verify_password_bcrypt
from models.model import User, Authenticated_User


def crud_login_user(user_data, db: Session) -> int:
    user_id = db.query(User.id).filter(User.email == user_data.email).first()
    login_user = Authenticated_User(user_id)
    db.add(login_user)
    db.commit()
    db.refresh(login_user)
    return user_id


def validate_user_status(user_email, db: Session) -> bool:
    return db.query(User.is_active).filter(User.email == user_email).first()


def verify_user_password(user_password, user_email, db: Session) -> bool:
    user = db.query(User.password_hash).filter(
        User.email == user_email).first()
    validPass = verify_password_bcrypt(user, user_password)
    return validPass
