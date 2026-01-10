from datetime import datetime, timezone
import re
from config.settings import DEFAULT_SLOTS, DEFAULT_RATE_PER_HOUR, DEFAULT_CURRENCY
from .utils import now_iso
from .operations import enter as op_enter, exit as op_exit, reserve as op_reserve, cancel_reservation as op_cancel
from ..views.view import view_table as op_view_table


class Parking:
    def __init__(self, storage, total_slots: int = DEFAULT_SLOTS, rate_per_hour: float = DEFAULT_RATE_PER_HOUR):
        """Parking boshqaruvi obyekti.

        Izohlar: parametrlar va o'zgaruvchilar ozbekcha kontekstda ishlatilmoqda.
        """
        self.saqlovchi = storage
        self.total_slots = total_slots
        self.rate = rate_per_hour
        self.currency = DEFAULT_CURRENCY
        # ensure slots list length equals total_slots
        slots = self.saqlovchi.get("slots")
        if not slots or len(slots) != total_slots:
            self.saqlovchi.set("slots", [None] * total_slots)

    def _now_iso(self):
        return now_iso()

    def plate_valid(self, reg: str) -> bool:
        """Sodda O'zbekiston uslubidagi avtomobil raqami tekshiruvi.

        Qabul qilinadigan asosiy format: `DDLDDDLL` masalan `10C234BD`.
        - D: raqam
        - L: katta harf (A-Z)

        Bu yerga kerak bo'lsa qo'shimcha formatlar qo'shilishi mumkin.
        """
        if not isinstance(reg, str):
            return False
        reg = reg.strip()
        # Reject lowercase entries
        if any(c.islower() for c in reg):
            return False
        # primary uzbek pattern: 2 digits, 1 letter, 3 digits, 2 letters
        pattern = r"^[0-9]{2}[A-Z][0-9]{3}[A-Z]{2}$"
        if re.fullmatch(pattern, reg):
            return True
        # fallback: require at least one digit and at least one uppercase letter, length 2-9
        if 2 <= len(reg) <= 9 and re.search(r"[0-9]", reg) and re.search(r"[A-Z]", reg):
            return True
        return False

    def view(self):
        slots = self.saqlovchi.get("slots")
        cars = self.saqlovchi.get("cars")
        return {"slots": slots, "cars": cars}

    def view_table(self) -> str:
        """Return parking status as a formatted table string by delegating to view module."""
        return op_view_table(self)

    def enter(self, reg_number: str, owner: str) -> bool:
        # plate validation
        if not self.plate_valid(reg_number):
            try:
                self.saqlovchi.append("notifications", {"username": owner, "message": f"Noto'g'ri avtomobil raqami kiritildi: {reg_number}", "time": self._now_iso()})
            except Exception:
                pass
            return False
        return op_enter(self, reg_number, owner)

    def _calculate_amount(self, entry_iso: str, exit_iso: str) -> float:
        entry = datetime.fromisoformat(entry_iso)
        exit = datetime.fromisoformat(exit_iso)
        seconds = (exit - entry).total_seconds()
        hours = max(0.0, seconds / 3600.0)
        return round(hours * self.rate, 2)

    def reserve(self, owner: str, slot: int | None = None) -> dict | None:
        """Create a reservation for `owner`. If `slot` is None, find first free slot.

        Returns reservation dict or None if not possible.
        """
        return op_reserve(self, owner, slot)

    def cancel_reservation(self, owner: str, slot: int | None = None) -> bool:
        return op_cancel(self, owner, slot)

    def exit(self, reg_number: str) -> dict | None:
        return op_exit(self, reg_number)
