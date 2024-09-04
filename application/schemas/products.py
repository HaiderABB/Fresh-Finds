from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class product_by_id(BaseModel):
    product_id: int

    class Config:
        from_attributes: True
