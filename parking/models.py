from dataclasses import dataclass, asdict
from typing import Optional
from datetime import datetime


@dataclass
class User:
    username: str
    password_hash: str


@dataclass
class Car:
    reg_number: str
    owner: str
    entry_time: Optional[str] = None
    slot: Optional[int] = None


@dataclass
class Payment:
    reg_number: str
    owner: str
    entry_time: str
    exit_time: str
    amount: float

    def to_dict(self):
        return asdict(self)
