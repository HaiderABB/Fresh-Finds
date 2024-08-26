import os
from fastapi import FastAPI, APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware
from dotenv import load_dotenv

load_dotenv(".env")

root_router = APIRouter()

app = FastAPI(title="Fresh Finds")
