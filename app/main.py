import os
from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv

load_dotenv(".env")

root_router = APIRouter(prefix="/FreshFinds")

app = FastAPI(title="Fresh Finds")


@app.get("/FreshFinds")
def read_root():
    return {"message": "Welcome to Fresh Finds"}
