from fastapi import HTTPException

from typing import List

from fastapi import FastAPI, APIRouter

from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserRead, UserCreate
from app.services.user import UserService

router = APIRouter(prefix="/users")

repo = UserRepository()


service = UserService(repo=repo)


@router.get("", response_model=List[UserRead])
def get_users():
    return service.get_all_users()


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("", response_model=UserRead)
def create_user(user: UserCreate):
    return service.create_user(user)


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserCreate):
    updated = service.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@router.delete("/{user_id}")
def delete_user(user_id: int):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}
