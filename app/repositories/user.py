from typing import List

from app.db.memory import users, counter
from app.models.user import User


class UserRepository:

    def create(self, user: User) -> User:
        global counter
        user.user_id = counter
        counter += 1
        users.append(user)
        return user




    def get_all(self) -> List[User]:
        return users

    def get_by_id(self, user_id: int) -> User | None:
        return next((user for user in users if user.user_id == user_id), None)

    def update(self, user_id: int, new_user: User) -> User | None:
        index_for_update = next((i for i, user in enumerate(users) if user.user_id == user_id), None)
        if index_for_update is not None:
            new_user.user_id = user_id
            users[index_for_update] = new_user
            return users[index_for_update]
        return None

    def delete(self, user_id: int):
        index_for_delete = next((i for i, user in enumerate(users) if user.user_id == user_id), None)
        if index_for_delete is not None:
            del users[index_for_delete]
            return True
        return False
