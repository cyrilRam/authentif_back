from typing import Optional

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.DB.models import User as modelUser


class User(BaseModel):
    id: Optional[int]
    nom_user: str
    password_user: str

    class Config:
        orm_mode = True

    @staticmethod
    def create_user(db: Session, user_name, hashed_passeword):
        try:
            new_user = modelUser(nom_user=user_name, password_user=hashed_passeword)
            db.add(new_user)
            db.commit()
        except Exception as e:
            raise ValueError(e)
        finally:
            db.close()

    @staticmethod
    def get_user(db: Session, user_name):
        user = db.query(modelUser).filter_by(nom_user=user_name).first()
        if user:
            user_sch = User(**{k: getattr(user, k) for k in User.__annotations__})
            return user_sch

        return None

    @staticmethod
    def get_user_info(db: Session, id):
        user = db.query(modelUser).filter_by(id=id).first()
        if user:
            user_sch = User(**{k: getattr(user, k) for k in User.__annotations__})
            return user_sch

        return None
