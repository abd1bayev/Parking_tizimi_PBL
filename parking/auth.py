import hashlib
from .models import User


class AuthService:
    def __init__(self, storage):
        self.storage = storage

    def _hash(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username: str, password: str) -> bool:
        users = self.storage.get("users")
        if any(u["username"] == username for u in users):
            return False
        user = User(username=username, password_hash=self._hash(password))
        self.storage.append("users", {"username": user.username, "password_hash": user.password_hash})
        return True

    def login(self, username: str, password: str) -> bool:
        users = self.storage.get("users")
        h = self._hash(password)
        return any(u["username"] == username and u["password_hash"] == h for u in users)
