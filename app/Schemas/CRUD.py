from typing import Type

from app.DB.models import User


def create_user(db, username, password):
    try:
        new_user = User(nom_user=username, password_user=password)
        db.add(new_user)
        db.commit()
    except Exception as e:
        raise ValueError(e)
    finally:
        db.close()


def get_user(db, username, schema_type: Type):
    user = db.query(User).filter_by(nom_user=username).first()
    if user:
        user_sch = schema_type(**{k: getattr(user, k) for k in schema_type.__annotations__})
        return user_sch

    return None

def get_user_info(db,id, schema_type: Type):
    user = db.query(User).filter_by(id=id).first()
    if user:
        user_sch = schema_type(**{k: getattr(user, k) for k in schema_type.__annotations__})
        return user_sch

    return None
