from sqlalchemy import Integer, Column, VARCHAR, Date, TEXT, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

from ..database import Base


class LostItems(Base):
    __tablename__ = "lost_items"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    lost_date = Column(Date, nullable=False)
    tags = Column(ARRAY(VARCHAR))
    place_where_lost = Column(VARCHAR)
    image = Column(VARCHAR)
    description = Column(TEXT)
    preferred_contact = Column(VARCHAR)

    user = relationship("users", back_populates="lost_item")
