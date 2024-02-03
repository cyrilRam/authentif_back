from typing import Optional

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.Schemas import CRUD as crud


class User(BaseModel):
    id: Optional[int]
    nom_user: str
    password_user: str

    class Config:
        orm_mode = True

    @staticmethod
    def create_user(db: Session, user_name, hashed_passeword):
        crud.create_user(db, user_name, hashed_passeword)

    @staticmethod
    def get_user(db: Session, user_name):
        return crud.get_user(db, user_name, User)

    @staticmethod
    def get_user_info(db: Session, id):
        return crud.get_user_info(db,id,User)
