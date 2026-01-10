from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    username: str
    password_hash: str
    email: Optional[str] = None
    role: str = "user"
