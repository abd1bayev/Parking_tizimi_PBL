from datetime import datetime
from .models import Car, Payment


class Parking:
    def __init__(self, storage, total_slots: int = 10, rate_per_hour: float = 2.0):
        self.storage = storage
        self.total_slots = total_slots
        self.rate = rate_per_hour
        # ensure slots list length equals total_slots
        slots = self.storage.get("slots")
        if not slots or len(slots) != total_slots:
            self.storage.set("slots", [None] * total_slots)

    def _now_iso(self):
        return datetime.utcnow().isoformat()

    def view(self):
        slots = self.storage.get("slots")
        cars = self.storage.get("cars")
        return {"slots": slots, "cars": cars}

    def enter(self, reg_number: str, owner: str) -> bool:
        slots = self.storage.get("slots")
        try:
            free_index = slots.index(None)
        except ValueError:
            return False
        entry_time = self._now_iso()
        car = {"reg_number": reg_number, "owner": owner, "entry_time": entry_time, "slot": free_index}
        cars = self.storage.get("cars")
        cars.append(car)
        slots[free_index] = reg_number
        self.storage.set("cars", cars)
        self.storage.set("slots", slots)
        return True

    def _calculate_amount(self, entry_iso: str, exit_iso: str) -> float:
        entry = datetime.fromisoformat(entry_iso)
        exit = datetime.fromisoformat(exit_iso)
        seconds = (exit - entry).total_seconds()
        hours = max(0.0, seconds / 3600.0)
        return round(hours * self.rate, 2)

    def exit(self, reg_number: str) -> dict | None:
        cars = self.storage.get("cars")
        slots = self.storage.get("slots")
        car = next((c for c in cars if c["reg_number"] == reg_number), None)
        if not car:
            return None
        exit_time = self._now_iso()
        amount = self._calculate_amount(car["entry_time"], exit_time)
        payment = Payment(reg_number=car["reg_number"], owner=car["owner"], entry_time=car["entry_time"], exit_time=exit_time, amount=amount)
        payments = self.storage.get("payments")
        payments.append(payment.to_dict())
        # free slot and remove car
        slot_index = car.get("slot")
        if slot_index is not None:
            slots[slot_index] = None
        cars = [c for c in cars if c["reg_number"] != reg_number]
        self.storage.set("cars", cars)
        self.storage.set("slots", slots)
        self.storage.set("payments", payments)
        return payment.to_dict()
