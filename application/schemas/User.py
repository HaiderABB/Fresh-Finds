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
        orm_mode = True


class user_auth(BaseModel):
    email: EmailStr
    password: str


class user_auth_response(BaseModel):
    jwt_token: str
    auth: bool
    message: str

    class Config:
        orm_mode = True


class user_retrieve_response(BaseModel):
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class user_logout(BaseModel):
    jwt_token: str


class user_logout_response(BaseModel):
    logout: bool
    message: str

    class Config:
        orm_mode = True
