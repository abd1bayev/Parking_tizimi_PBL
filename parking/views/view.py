from ..core.utils import format_parking_table


def view_table(parking) -> str:
    slots = parking.saqlovchi.get("slots")
    cars = parking.saqlovchi.get("cars")
    reservations = parking.saqlovchi.get("reservations")
    return format_parking_table(slots, cars, reservations)
