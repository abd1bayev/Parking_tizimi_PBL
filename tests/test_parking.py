from datetime import datetime, timedelta, timezone

from parking.core.parking import Parking


def test_enter_and_exit_fee(test_storage):
    parking = Parking(test_storage, total_slots=2, rate_per_hour=10.0)
    # enter a car
    ok = parking.enter("CAR123", "testuser")
    assert ok is True
    cars = test_storage.get("cars")
    assert any(c["reg_number"] == "CAR123" for c in cars)

    # simulate earlier entry time (2 hours ago) for deterministic fee
    two_hours_ago = (datetime.now(timezone.utc) - timedelta(hours=2)).isoformat()
    cars = test_storage.get("cars")
    for c in cars:
        if c["reg_number"] == "CAR123":
            c["entry_time"] = two_hours_ago
    test_storage.set("cars", cars)

    payment = parking.exit("CAR123")
    assert payment is not None
    # with rate 10.0 and ~2 hours expect around 20.0
    assert payment["amount"] >= 19.9 and payment["amount"] <= 20.1

def test_parking_full(test_storage):
    parking = Parking(test_storage, total_slots=1)
    assert parking.enter("A1", "u") is True
    assert parking.enter("B2", "u") is False

def test_plate_validation_rejects_invalid(test_storage):
    parking = Parking(test_storage, total_slots=2)
    # lowercase and wrong format should be rejected
    assert parking.enter("eqw2342a", "u") is False
    # correct uzbek-like plate accepted
    assert parking.enter("10C234BD", "u") is True
