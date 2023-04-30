from typing import Optional

from pydantic import BaseModel
from datetime import date


class Item(BaseModel):
    user_id: int
    found_date: date
    tags: list[str]
    description: str
    image: Optional[str]
    preferred_contact: Optional[str]

    class Config:
        orm_mode = True
