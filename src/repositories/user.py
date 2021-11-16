from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from src.helpers import utils
from src.models.user import User
from src.schemas.user import UserRequest


def get_users(db: Session, limit: int = 100):
    return db.query(User).limit(limit).all()


def get_one_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The user with id {user_id} is not available.")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"The user with id {user_id} is not available."}
    return user


def save_user(request: UserRequest, db: Session):
    to_create = User(
        email=request.email,
        name=request.name,
        password=utils.hash_password(request.password)
    )
    db.add(to_create)
    db.commit()
    db.refresh(to_create)
    return to_create


def update_user(user_id, request: UserRequest, db: Session):
    user = db.query(User).filter(User.id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The user with id {user_id} is not available.")
    user.update(request)
    db.commit()
    return {"result": "updated"}


def remove_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The user with id {user_id} is not available.")
    user.delete(synchronize_session=False)
    db.commit()
    return {'result': True}
