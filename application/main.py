import os
from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware
from database.session import Base, init_db

# load_dotenv()

# print(os.environ.get("PORT"))

root_router = APIRouter(prefix="/FreshFinds")

app = FastAPI(title="Fresh Finds")
init_db()
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DB_URL'])

print(os.environ['PORT'])


@app.get("/FreshFinds")
def read_root():
    return {"message": "Welcome to Fresh Finds"}
