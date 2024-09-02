from fastapi import Depends, APIRouter, HTTPException
from database.session import get_db
from schemas.user import user_registration, user_registration_response, user_auth, user_auth_response, user_logout, user_logout_response, user_retrieve_response
from sqlalchemy.orm import Session
from sqlalchemy import func
from application.models.user import users
from crud.users.crud_register_user import register_user as crud_register_user, validate_user
from utils.password_hash import hash_password_bcrypt
from crud.users.crud_authenticate_user import validate_user_status, crud_authenticate_user, verify_user_password

auth_router = APIRouter(prefix="/FreshFinds/auth")


@auth_router.post("/register", status_code=201, response_model=user_registration_response)
def register_user(payload: user_registration, db: Session = Depends(get_db)):
    # Create the user data object
    user_data = users(
        username=payload.username,
        email=payload.email.lower(),
        password_hash=hash_password_bcrypt(payload.password)
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


@auth_router.post("/login", status_code=200, response_model=user_auth_response)
def authenticate_user(payload: user_auth, db: Session = Depends(get_db)):
    user_data = users(email=payload.email.lower(),
                      password_hash=payload.password)
    exists = validate_user(user_data.email, db)

    if exists:
        isValid = validate_user_status(user_data.email, db)
        if isValid:
            validPass = verify_user_password(
                user_data.email, user_data.password_hash)
            if validPass:
                id = crud_authenticate_user(user_data, db)

    else:
        raise HTTPException(status_code=401, detail={
                            "login": False, "message": "User does not exist"})
