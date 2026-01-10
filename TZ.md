# Texnik topshiriq (TZ) — Parking tizimi

Maqsad: Konsol ilovasi sifatida ishlaydigan, sodda va testlanadigan parking boshqaruv tizimini yaratish. Saqlash — JSON fayl (`data.json`).

1. Funksional talablar
- Foydalanuvchilar: ro'yxatdan o'tish, login. Har bir foydalanuvchi `role`ga ega: `user` yoki `admin`.
- Mashina kirishi (`enter`) — avtomobil raqami va egasi bilan kirish; agar bo'sh slot bo'lmasa rad etadi.
- Mashina chiqishi (`exit`) — kirish vaqtiga asoslanib to'lov hisoblanadi va `payments` saqlanadi.
- Park holatini ko'rsatish (`view_table`) — slotlar jadvali, rezervatsiyalar va egalar ko'rsatiladi.
- Rezervatsiya: foydalanuvchi slot bron qilishi va bekor qilishi mumkin.
- Ogohlantirishlar (`notifications`) — tizim voqealari bu yerga yoziladi.

2. Texnik talablar
- Python 3.10+.
- Kichikroq modullar: har bir modulning mas'uliyati aniq bo'lishi kerak.
- Testlar: `pytest` uchun unit testlar bo'lishi kerak.

3. Ma'lumot modeli
- `User` {username, password_hash, email, role}
- `Car` {reg_number, owner, entry_time, slot}
- `Payment` {reg_number, owner, entry_time, exit_time, amount, currency}

4. API / CLI qoidalari
- `cli.py` orqali:
  - Ro'yxatdan o'tish: foydalanuvchi `role`ni ko'rsatishi mumkin (admin yaratish imkoniyati mavjud).
  - Login → role ga qarab menyu: `admin` kengroq funktsiyalar (foydalanuvchilar ko'rish, mashina kiritish boshqalar uchun).

5. Qabul qilish mezonlari
- Unit testlar barcha asosiy oqimlarni qoplaydi: kirish/chiqish, plate validatsiya, rezervatsiya.
- `Parking.enter` va `Parking.exit` ishlaydi va `data.json` ni mos ravishda yangilaydi.
- CLI interaktiv bo'lib, noto'g'ri kiritilgan email/plate bolligida tegishli ogohlantirish beradi.

6. Kelajakda yaxshilashlar
- Parollarni `passlib` yordamida yaxshilash.
- Saqlash qatlamini plagin qilish — JSON dan boshqa DB'ga tez o‘tish.
- Web/REST interfeys qo‘shish va autentifikatsiyani yaxshilash (JWT, OAuth).
