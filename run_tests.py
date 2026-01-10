from parking.storage import JSONStorage
from user.service import AuthService
from parking.parking import Parking


def run():
    # use a test file so we don't clobber real data
    storage = JSONStorage("test_data.json")
    auth = AuthService(storage)
    parking = Parking(storage, total_slots=2, rate_per_hour=1.0)

    # clean start
    storage.set("users", [])
    storage.set("cars", [])
    storage.set("slots", [None] * 2)
    storage.set("payments", [])

    # royxatdan otish va login tekshiruvi
    assert auth.royxatdan_otish("alice", "secret", "alice@example.com") is True
    assert auth.royxatdan_otish("alice", "x", "bademail") is False
    assert auth.login("alice", "secret") is True
    assert auth.login("alice", "bad") is False

    ok = parking.enter("ABC123", "alice")
    assert ok is True
    # entering when full
    ok2 = parking.enter("XYZ999", "alice")
    assert ok2 is True
    ok3 = parking.enter("FULL1", "alice")
    assert ok3 is False

    # exit first car
    payment = parking.exit("ABC123")
    assert payment is not None
    assert "amount" in payment

    print("All tests passed.")


if __name__ == "__main__":
    run()
