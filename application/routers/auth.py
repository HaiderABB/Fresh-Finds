from fastapi import Depends, APIRouter, HTTPException
from database.session import get_db
from schemas.user import user_registration, user_registration_response, user_login, user_login_response, user_logout, user_logout_response, user_retrieve_response, user_retrieve
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.model import User
from crud.users.crud_register_user import register_user as crud_register_user, user_exists
from utils.password_hash import hash_password_bcrypt
from crud.users.crud_user_login import validate_user_status, crud_login_user, verify_user_password
from utils.jwt_token import create_jwt_token, unsign_jwt_token
from crud.users.crud_retrieve_data import crud_retrieve_user
from crud.users.crud_logout_user import crud_logout_user

auth_router = APIRouter(prefix="/FreshFinds/auth")


@auth_router.post("/register", status_code=201, response_model=user_registration_response)
def register_user(payload: user_registration, db: Session = Depends(get_db)):
    # Create the user data object
    user_data = User(
        username=payload.username,
        email=payload.email.lower(),
        password_hash=hash_password_bcrypt(payload.password)
    )

    # Check if the user already exists
    exists = user_exists(user_data.email, db)

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


@auth_router.post("/login", status_code=200, response_model=user_login_response)
def login_user(payload: user_login, db: Session = Depends(get_db)):
    user_data = User(email=payload.email.lower(),
                     password_hash=payload.password)
    exists = user_exists(user_data.email, db)

    if exists:
        isValid = validate_user_status(user_data.email, db)
        if isValid:
            validPass = verify_user_password(
                user_data.email, user_data.password_hash, db)
            if validPass:
                id = crud_login_user(user_data, db)
                jwt_token = create_jwt_token(id)
                return {"jwt_token": jwt_token, "login": True, "password": True, "email": True, "status": True, "message": "Login Successful"}
            else:
                raise HTTPException(status_code=401, detail={
                                    "jwt_token": False, "login": False, "password": False, "email": True, "status": True, "message": "Invalid Password"})
        else:
            raise HTTPException(status_code=403, detail={
                                "jwt_token": False, "login": False, "password": False, "email": True, "status": False, "message": "User Status False"})
    else:
        raise HTTPException(status_code=404, detail={
                            "jwt_token": False, "login": False, "password": False, "email": False, "status": False, "message": "User does not exist"})


@auth_router.get("/me", status_code=200, response_model=user_retrieve_response)
def get_user_me(payload: user_retrieve, db: Session = Depends(get_db)):
    if payload.jwt_token:
        user_id = unsign_jwt_token(payload.jwt_token)
        validToken = bool(user_id)
        if validToken:
            user = crud_retrieve_user(user_id, db)
            return {"token": True, "username": user.username, "email": user.email, "created_at": user.created_at, "updated_at": user.updated_at}
        else:
            raise HTTPException(status_code=404, detail={
                "token": False, "message": "Invalid Token"})
    else:
        raise HTTPException(status_code=401, detail={
            "token": False, "message": "Please provide a jwt_token"})


@auth_router.post("/logout", status_code=200, response_model=user_logout_response)
def user_logout(payload: user_logout, db: Session = Depends(get_db)):
    user_id = unsign_jwt_token(payload.jwt_token)
    validToken = bool(user_id)
    if validToken:
        logout = crud_logout_user(user_id, db)
        return {"logout": logout, "token": True, "message": "Logout Successful"}
    else:
        raise HTTPException(status_code=404, detail={
            "logout": False, "token": False, "message": "Invalid Token"})
