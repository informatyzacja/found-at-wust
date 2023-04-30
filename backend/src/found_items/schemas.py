from typing import Optional

from ..schemas import Item


class FoundItemCreate(Item):
    place_where_left: str
    place_where_found: Optional[str]


class FoundItemRead(FoundItemCreate):
    id: int
