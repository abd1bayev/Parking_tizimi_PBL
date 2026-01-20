"""Foydalanuvchi autentifikatsiyasi xizmati.

Funktsiyalar nomlari va izohlar ozbekcha.
"""
import hashlib
from parking.models import User
from datetime import datetime, timezone


class AuthService:
    """Foydalanuvchi ro'yxatdan o'tkazish va login qilish uchun xizmat.

    `royxatdan_otish` telefon raqamini qabul qiladi va ogohlantirishlar (notifications)
    `notifications` ro'yxatiga yoziladi.
    """

    def __init__(self, saqlovchi):
        # saqlovchi: JSONStorage obyekti
        self.saqlovchi = saqlovchi

    def _hash(self, parol: str) -> str:
        """Parolni xeshlash (SHA-256)."""
        return hashlib.sha256(parol.encode()).hexdigest()

    def _now(self) -> str:
        return datetime.now(timezone.utc).isoformat()

    def phone_valid(self, phone: str) -> bool:
        """Telefon raqamini tekshirish: +998 bilan boshlanadi, 12 ta raqam."""
        try:
            phone = phone.replace(" ", "").replace("-", "")
            return phone.startswith("+998") and len(phone) == 13 and phone[1:].isdigit()
        except Exception:
            return False

    def royxatdan_otish(self, username: str, parol: str, phone: str, role: str = "user") -> bool:
        """Foydalanuvchini ro'yxatdan o'tkazadi; agar telefon noto'g'ri bo'lsa False qaytaradi.

        `role` parametri yordamida admin yaratish mumkin (akademik loyihada ehtiyot bo'ling).
        """
        # telefon raqamini tekshirish
        if not self.phone_valid(phone):
            # ogohlantirish yozamiz
            self.saqlovchi.append("notifications", {"username": username, "message": "Telefon noto'g'ri", "time": self._now()})
            return False

        foydalanuvchilar = self.saqlovchi.get("users")
        if any(u["username"] == username for u in foydalanuvchilar):
            return False
        user = User(username=username, password_hash=self._hash(parol), phone=phone, role=role)
        self.saqlovchi.append("users", {"username": user.username, "password_hash": user.password_hash, "phone": user.phone, "role": user.role})
        # ro'yxatdan o'tganligi haqida ogohlantirish
        self.saqlovchi.append("notifications", {"username": username, "message": "Ro'yxatdan o'tdingiz", "time": self._now()})
        return True

    def login(self, username: str, parol: str) -> bool:
        """Login tekshiruvini bajaradi; to'g'ri bo'lsa True va ogohlantirish yozadi."""
        foydalanuvchilar = self.saqlovchi.get("users")
        h = self._hash(parol)
        ok = any(u["username"] == username and u["password_hash"] == h for u in foydalanuvchilar)
        self.saqlovchi.append("notifications", {"username": username, "message": "Login urinish: " + ("muvaffaqiyatli" if ok else "muvaffaqiyatsiz"), "time": self._now()})
        return ok
