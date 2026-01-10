from typing import Optional
from .core.operations import *

__all__ = [
    'enter', 'exit', 'reserve', 'cancel_reservation'
]


def _calculate_amount(rate: float, entry_iso: str, exit_iso: str) -> float:
    from datetime import datetime

    entry = datetime.fromisoformat(entry_iso)
    exit = datetime.fromisoformat(exit_iso)
    seconds = (exit - entry).total_seconds()
    hours = max(0.0, seconds / 3600.0)
    return round(hours * rate, 2)


def enter(parking, reg_number: str, owner: str) -> bool:
    slots = parking.saqlovchi.get("slots")
    reservations = parking.saqlovchi.get("reservations")
    owner_res = next((r for r in reservations if r.get("owner") == owner), None)
    if owner_res:
        slot_candidate = owner_res.get("slot")
        if slots[slot_candidate] is None:
            free_index = slot_candidate
            reservations = [r for r in reservations if not (r.get("owner") == owner and r.get("slot") == slot_candidate)]
            parking.saqlovchi.set("reservations", reservations)
        else:
            try:
                free_index = slots.index(None)
            except ValueError:
                return False
    else:
        try:
            free_index = slots.index(None)
        except ValueError:
            return False
    entry_time = parking._now_iso()
    mashina = {"reg_number": reg_number, "owner": owner, "entry_time": entry_time, "slot": free_index}
    cars = parking.saqlovchi.get("cars")
    cars.append(mashina)
    slots[free_index] = reg_number
    parking.saqlovchi.set("cars", cars)
    parking.saqlovchi.set("slots", slots)
    try:
        parking.saqlovchi.append("notifications", {"username": owner, "message": f"Sizning mashinangiz {reg_number} parkka kiritildi (slot {free_index})", "time": entry_time})
    except Exception:
        pass
    return True


def exit(parking, reg_number: str) -> Optional[dict]:
    cars = parking.saqlovchi.get("cars")
    slots = parking.saqlovchi.get("slots")
    car = next((c for c in cars if c["reg_number"] == reg_number), None)
    if not car:
        return None
    exit_time = parking._now_iso()
    amount = _calculate_amount(parking.rate, car["entry_time"], exit_time)
    payment = Payment(reg_number=car["reg_number"], owner=car["owner"], entry_time=car["entry_time"], exit_time=exit_time, amount=amount, currency=parking.currency)
    payments = parking.saqlovchi.get("payments")
    payments.append(payment.to_dict())
    slot_index = car.get("slot")
    if slot_index is not None:
        slots[slot_index] = None
    cars = [c for c in cars if c["reg_number"] != reg_number]
    parking.saqlovchi.set("cars", cars)
    parking.saqlovchi.set("slots", slots)
    parking.saqlovchi.set("payments", payments)
    try:
        parking.saqlovchi.append("notifications", {"username": car.get("owner"), "message": f"Sizning mashinangiz {reg_number} parkdan chiqdi. To'lov: {amount}", "time": exit_time})
    except Exception:
        pass
    return payment.to_dict()


def reserve(parking, owner: str, slot: Optional[int] = None) -> Optional[dict]:
    slots = parking.saqlovchi.get("slots")
    reservations = parking.saqlovchi.get("reservations")
    if slot is not None:
        if slot < 0 or slot >= len(slots):
            return None
        if slots[slot] is not None:
            return None
        if any(r.get("slot") == slot for r in reservations):
            return None
        res = {"owner": owner, "slot": slot, "time": parking._now_iso()}
        reservations.append(res)
        parking.saqlovchi.set("reservations", reservations)
        return res
    for i, s in enumerate(slots):
        if s is None and not any(r.get("slot") == i for r in reservations):
            res = {"owner": owner, "slot": i, "time": parking._now_iso()}
            reservations.append(res)
            parking.saqlovchi.set("reservations", reservations)
            return res
    return None


def cancel_reservation(parking, owner: str, slot: Optional[int] = None) -> bool:
    reservations = parking.saqlovchi.get("reservations")
    before = len(reservations)
    if slot is None:
        reservations = [r for r in reservations if r.get("owner") != owner]
    else:
        reservations = [r for r in reservations if not (r.get("owner") == owner and r.get("slot") == slot)]
    parking.saqlovchi.set("reservations", reservations)
    return len(reservations) < before
