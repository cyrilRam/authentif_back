from sqlalchemy import Column, Integer, String

from app.DB.config import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nom_user = Column(String, index=True, unique=True)
    password_user = Column(String, index=True, unique=True)
