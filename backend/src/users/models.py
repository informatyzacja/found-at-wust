from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    lost_item = relationship("lost_items", back_populates="user")
    found_item = relationship("found_items", back_populates="user")

