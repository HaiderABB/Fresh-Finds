from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class user_registration(BaseModel):
    username: str
    email: EmailStr
    password: str


class user_registration_response(BaseModel):
    registration: bool
    message: str

    class Config:
        from_attributes = True


class user_login(BaseModel):
    email: EmailStr
    password: str


class user_login_response(BaseModel):
    jwt_token: str
    login: bool
    password: bool
    email: bool
    status: bool
    message: str

    class Config:
        from_attributes = True


class user_retrieve(BaseModel):
    jwt_token: str

    class Config:
        from_attributes: True


class user_retrieve_response(BaseModel):
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
    token: bool

    class Config:
        from_attributes = True


class user_logout(BaseModel):
    jwt_token: str


class user_logout_response(BaseModel):
    logout: bool
    message: str

    class Config:
        from_attributes = True
