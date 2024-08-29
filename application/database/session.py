import os
import orjson
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

load_dotenv()


Base = declarative_base()


def orjson_serializer(obj):
    return orjson.dumps(
        obj, option=orjson.OPT_SERIALIZE_NUMPY | orjson.OPT_NAIVE_UTC
    ).decode()


engine = create_engine(
    os.environ['DB_URL'],
    json_serializer=orjson_serializer,
    json_deserializer=orjson.loads,
    connect_args={}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    # Create an engine connected to the PostgreSQL database
    engine = create_engine(os.environ['DB_URL'])


print("Database Connection Successful")
# Create all tables defined in the Base metadata
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()
