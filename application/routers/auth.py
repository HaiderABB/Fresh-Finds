from fastapi import Depends, APIRouter, HTTPException
from database.session import get_db
from schemas.user import user_registration, user_registration_response
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.users import users
from sqlalchemy import text


auth_router = APIRouter(prefix="/FreshFinds/auth")


def user_registeration(user_data, db: Session):

    sql_command = text("""
        SELECT register_user(:username, :email, :password);
    """)

    db.execute(sql_command, {
        'username': user_data.username,
        'email': user_data.email,
        'password': user_data.password_hash
    })

    # Commit the transaction to ensure the changes are saved
    db.commit()


@auth_router.post("/register", status_code=200)
def register_user(payload: user_registration, db: Session = Depends(get_db)):

    user_data = users(username=payload.username,
                      email=payload.email, password_hash=payload.password)
    query_result = user_registeration(user_data, db)
    return {"Message": "User Registered Successfully"}
