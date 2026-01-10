"""Foydalanuvchi autentifikatsiyasi xizmati.

Funktsiyalar nomlari va izohlar ozbekcha.
"""
import hashlib
from parking.models import User
from datetime import datetime, timezone


class AuthService:
    """Foydalanuvchi ro'yxatdan o'tkazish va login qilish uchun xizmat.

    Endi `royxatdan_otish` email parametrini qabul qiladi va ogohlantirishlar (notifications)
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

    def email_valid(self, email: str) -> bool:
        """Sodda email tekshiruvi: @ va domen qismi nuqta mavjudligini tekshiradi."""
        try:
            return "@" in email and "." in email.split("@")[-1]
        except Exception:
            return False

    def royxatdan_otish(self, username: str, parol: str, email: str, role: str = "user") -> bool:
        """Foydalanuvchini ro'yxatdan o'tkazadi; agar email noto'g'ri bo'lsa False qaytaradi.

        `role` parametri yordamida admin yaratish mumkin (akademik loyihada ehtiyot bo'ling).
        """
        # sodda email tekshiruvi
        if not self.email_valid(email):
            # ogohlantirish yozamiz
            self.saqlovchi.append("notifications", {"username": username, "message": "Email noto'g'ri", "time": self._now()})
            return False

        foydalanuvchilar = self.saqlovchi.get("users")
        if any(u["username"] == username for u in foydalanuvchilar):
            return False
        user = User(username=username, password_hash=self._hash(parol), email=email, role=role)
        self.saqlovchi.append("users", {"username": user.username, "password_hash": user.password_hash, "email": user.email, "role": user.role})
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
