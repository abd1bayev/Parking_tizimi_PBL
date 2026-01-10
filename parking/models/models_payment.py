from dataclasses import dataclass, asdict


@dataclass
class Payment:
    reg_number: str
    owner: str
    entry_time: str
    exit_time: str
    amount: float
    currency: str = "UZS"

    def to_dict(self):
        return asdict(self)
