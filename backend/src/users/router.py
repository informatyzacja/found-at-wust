from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..dependencies import get_db
from .schemas import User as SchemaUser
from .models import User as ModelUser
router = APIRouter(prefix="/users", tags=["users"])


# actual only for testing
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: SchemaUser, db: Session = Depends(get_db)):
    db_user = ModelUser(id=user.id)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
