from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.config.database import get_db
from ..helpers.oauth2 import get_current_user
from ..models.user import User
from ..repositories import user as u
from ..schemas.user import UserRequest, UserView

user = APIRouter(
    prefix='/users',
    tags=['Users'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@user.get('', status_code=status.HTTP_200_OK, response_model=List[UserView])
def get_all(db: Session = Depends(get_db), limit: int = 100,
            current_user: User = Depends(get_current_user)):
    return u.get_users(db, limit)


@user.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=UserView)
def get_one(user_id: int, db: Session = Depends(get_db),
            current_user: User = Depends(get_current_user)):
    return u.get_one_user(user_id, db)


@user.post('', status_code=status.HTTP_201_CREATED, response_model=UserView)
def save(request: UserRequest, db: Session = Depends(get_db),
         current_user: User = Depends(get_current_user)):
    return u.save_user(request, db)


@user.put('', status_code=status.HTTP_202_ACCEPTED)
def update(user_id: int, request: UserRequest, db: Session = Depends(get_db),
           current_user: User = Depends(get_current_user)):
    return u.update_user(user_id, request, db)


@user.delete('/{user_id}', status_code=status.HTTP_201_CREATED)
def remove(user_id: int, db: Session = Depends(get_db),
           current_user: User = Depends(get_current_user)):
    return u.remove_user(user_id, db)
