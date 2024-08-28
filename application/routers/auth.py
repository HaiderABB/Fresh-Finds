from fastapi import Depends, APIRouter, HTTPException
from database.session import get_db
from schemas.user import user_registration, user_registration_response
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.users import users


auth_router = APIRouter(prefix="/FreshFinds/auth")


def user_registeration(user_data, db: Session):

    result = db.query(
        func.register_user(
            user_data.username, user_data.email, user_data.password).label('user')
    )

    return result


@auth_router.post("/register", status_code=200)
async def register_user(payload: user_registration, db: Session = Depends(get_db)):

    user_data = users(username=payload.username,
                      email=payload.email, password=payload.password)
    query_result = await user_registeration(user_data, db)
    return {"Message": "User Registered Successfully"}
