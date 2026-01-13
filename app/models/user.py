


class User:
    user_id: int
    name: str
    email: str
    password_hash: str

    def __str__(self):
        return f"User(id={self.user_id}, name={self.name}, email={self.email})"
