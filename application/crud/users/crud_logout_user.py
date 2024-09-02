from sqlalchemy.orm import Session
from models.model import Authenticated_User


def crud_logout_user(user_id, db: Session) -> bool:
    user_delete = db.query(Authenticated_User).filter(
        Authenticated_User.id == user_id).first()
    if user_delete:
        db.query(Authenticated_User).filter(
            Authenticated_User.id == user_id).delete()
        db.commit()
        return True
    else:
        return False
