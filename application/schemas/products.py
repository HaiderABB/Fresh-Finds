from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class product_by_id(BaseModel):
    product_id: int
