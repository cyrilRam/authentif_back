from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.DB.config import get_db
from app.Schemas.User import User
from app.utils.security import Security

router = APIRouter()
security = Security()
db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/create-user")
async def create_user(db: db_dependency, username: str, password: str):
    hashed_password = security.get_password_hash(password)
    User.create_user(db, username, hashed_password)
    return {"message": "User created successfully"}


@router.post("/token")
async def login_for_access_token(db: db_dependency, username: str, password: str):
    user = User.get_user(db, username)
    if user and security.verify_password(password, user.password_user):
        user.password_user = ""
        token_data = user.dict()
        access_token = security.create_access_token(token_data)
        return {"access_token": access_token, "token_type": "bearer", "user_object": user.dict()}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.get("/get_user_from_token")
async def get_user_from_token(token: str):
    try:
        current_user = security.decode_token(token)
        return {"message": "This is a protected route", "user": current_user}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"{e}",
        )

# @router.get("/getUserInfo")
# async def protected_route(db: db_dependency, id: int):
#     user = User.get_user_info(db, id)
#     user.password_user = ""
#     return JSONResponse(content=user.dict())
