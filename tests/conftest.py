import os
import sys
import pathlib
import pytest

# Add project root to sys.path so tests can import local packages
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from parking.storage import JSONStorage


@pytest.fixture(autouse=True)
def test_storage(tmp_path):
    # Use a temporary test file for isolation
    p = tmp_path / "test_data.json"
    storage = JSONStorage(str(p))
    # ensure clean state
    storage.set("users", [])
    storage.set("cars", [])
    storage.set("slots", [None] * 2)
    storage.set("payments", [])
    storage.set("notifications", [])
    return storage
