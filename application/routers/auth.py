from fastapi import APIRouter

auth_router = APIRouter(prefix="/FreshFinds/auth")


@auth_router.post("/register")
def func():
    return {"message": "Hello, World!"}
