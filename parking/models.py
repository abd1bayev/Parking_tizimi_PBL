from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class User:
    """Foydalanuvchi modeli (username, parol xeshi va email)."""
    username: str
    password_hash: str
    email: Optional[str] = None
    role: str = "user"


@dataclass
class Car:
    """Mashina modeli: reg_number (raqam), owner (egasi), kirish va slot."""
    reg_number: str
    owner: str
    entry_time: Optional[str] = None
    slot: Optional[int] = None


@dataclass
class Payment:
    """To'lov yozuvi: kirish, chiqish va summasi."""
    reg_number: str
    owner: str
    entry_time: str
    exit_time: str
    amount: float
    currency: str = "UZS"

    def to_dict(self):
        return asdict(self)
