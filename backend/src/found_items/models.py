from sqlalchemy import Integer, Column, VARCHAR, Date, TEXT, ForeignKey, ARRAY


from ..database import Base


class FoundItem(Base):
    __tablename__ = "found_items"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    found_date = Column(Date, nullable=False)
    description = Column(TEXT, nullable=False)
    place_where_left = Column(VARCHAR, nullable=False)
    tags = Column(ARRAY(VARCHAR))
    place_where_found = Column(VARCHAR)
    image = Column(VARCHAR)
    preferred_contact = Column(VARCHAR)

