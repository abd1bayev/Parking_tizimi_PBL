from dataclasses import dataclass
from typing import Optional


@dataclass
class Car:
    reg_number: str
    owner: str
    entry_time: Optional[str] = None
    slot: Optional[int] = None
