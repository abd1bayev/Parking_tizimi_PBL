import json
from typing import Dict, Any
from pathlib import Path


class JSONStorage:
    """JSON orqali ma'lumotlarni saqlovchi (ozbekcha izohlar bilan)."""
    def __init__(self, path: str | Path = "data.json"):
        self.path = Path(path)
        if not self.path.exists():
            self._init_file()

    def _init_file(self):
        base = {"users": [], "cars": [], "slots": [], "payments": [], "notifications": [], "reservations": []}
        self._write(base)

    def _read(self) -> Dict[str, Any]:
        with self.path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data: Dict[str, Any]):
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get(self, key: str):
        """Kalit bo'yicha qiymatni o'qish."""
        data = self._read()
        return data.get(key, [])

    def set(self, key: str, value):
        """Kalitga qiymat yozish (to'liq yangilash)."""
        data = self._read()
        data[key] = value
        self._write(data)

    def append(self, key: str, item):
        """Ro'yxatga yangi element qo'shish."""
        data = self._read()
        data.setdefault(key, []).append(item)
        self._write(data)
