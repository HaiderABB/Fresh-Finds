import os
import uvicorn
from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware
from database.session import Base, init_db
from routers.auth import auth_router
from routers.products import product_router

root_router = APIRouter(prefix="/FreshFinds")

app = FastAPI(title="Fresh Finds")
init_db()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DB_URL'])
app.include_router(root_router)
app.include_router(auth_router)
app.include_router(product_router)


@app.get("/FreshFinds")
def read_root():
    return {"message": "Welcome to Fresh Finds"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
