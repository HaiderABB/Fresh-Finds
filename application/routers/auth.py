from fastapi import Depends, APIRouter, HTTPException
from database.session import get_db
from schemas.user import user_registration, user_registration_response
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.users import users
from crud.users.register_user import register_user as crud_register_user, validate_user
from utils.password_hash import hash_password

auth_router = APIRouter(prefix="/FreshFinds/auth")


@auth_router.post("/register", status_code=200, response_model=user_registration_response)
def register_user(payload: user_registration, db: Session = Depends(get_db)):
    # Create the user data object
    user_data = users(
        username=payload.username,
        email=payload.email.lower(),
        password_hash=hash_password(payload.password)
    )

    # Check if the user already exists
    exists = validate_user(user_data.email, db)

    if not exists:
        # Register the user if not exists
        crud_register_user(user_data, db)
        return {"registration": True, "message": "User Registration Successful"}
    else:
        # Handle user already exists case
        raise HTTPException(
            status_code=400, detail={
                "registration": False, "message": "User Exists Already"}
        )
