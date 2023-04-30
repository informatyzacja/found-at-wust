from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from ..database import Base

# This import is necessary because tables must be initialized after this model
from ..found_items.models import FoundItem
from ..lost_items.models import LostItem


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    lost_item = relationship("LostItem", backref="users")
    found_item = relationship("FoundItem", backref="users")
