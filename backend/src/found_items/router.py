from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..dependencies import get_db
from .schemas import FoundItemCreate, FoundItemRead
from .models import FoundItem

router = APIRouter(prefix="/found-items", tags=["found-items"])


@router.get("/", response_model=list[FoundItemRead])
def get_events(db: Session = Depends(get_db)):
    events = db.query(FoundItem).all()
    if not events:
        return []
    return events


@router.post("/", response_model=FoundItemRead, status_code=status.HTTP_201_CREATED)
def create_found_item(found_item: FoundItemCreate, db: Session = Depends(get_db)):
    db_found_item = FoundItem(user_id=found_item.user_id, found_date=found_item.found_date, tags=found_item.tags,
                              place_where_found=found_item.place_where_found, image=found_item.image,
                              place_where_left=found_item.place_where_left, description=found_item.description,
                              preferred_contact=found_item.preferred_contact)
    db.add(db_found_item)
    db.commit()
    db.refresh(db_found_item)
    return db_found_item
