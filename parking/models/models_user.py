from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    username: str
    password_hash: str
    phone: Optional[str] = None
    role: str = "user"
