from pydantic import BaseModel


class User(BaseModel):
    id: int

    class Config:
        orm_mode = True
