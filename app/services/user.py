from typing import List, Optional

from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, user_create: UserCreate) -> User:
        user = User()
        user.name = user_create.name
        user.email = user_create.email
        user.password_hash = user_create.password
        return self.repo.create(user)

    def get_all_users(self) -> List[User]:
        return self.repo.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self.repo.get_by_id(user_id)

    def update_user(self, user_id: int, user: User) -> Optional[User]:
        return self.repo.update(user_id, user)

    def delete_user(self, user_id: int)-> bool:
        return self.repo.delete(user_id)