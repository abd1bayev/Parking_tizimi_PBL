# Arxitektura va sxema — Parking Tizimi

Qisqacha: Loyihaning asosiy qismi `parking` paketi. Maqsad — sodda, testlanadigan biznes mantiqni JSON fayl bilan saqlash orqali ishlatish.

Komponentlar
- `parking.core`:
  - `parking.py` — `Parking` klassi; yuqori darajadagi API: `enter`, `exit`, `view`, `view_table`, `reserve`, `cancel_reservation`.
  - `operations.py` — kirish/chiqish/rezervatsiya mantiqi (yon effektli, storage bilan ishlaydi).
  - `utils.py` — vaqt, plate validatsiya va jadval formatlash yordamchilari.
- `parking.models`:
  - `User`, `Car`, `Payment` — dataclasslar; JSONga serialize qilish uchun `to_dict` metodlari (Payment).
- `parking.views`:
  - Jadval formatlash va ko‘rsatish funksionalari.
- `parking.storage.JSONStorage`:
  - JSON faylga o‘qish/yozish/append imkoniyatlari.
- `user.service.AuthService`:
  - Ro'yxatdan o'tish, login va email validatsiyasi. Hozir SHA-256 ishlatilgan; tavsiya: `passlib`.
- `cli.py` — konsol interfeys; role asosida menyular (admin vs user).

Saqlash sxemasi (`data.json`)
- users: list of {username, password_hash, email, role}
- cars: list of {reg_number, owner, entry_time, slot}
- slots: list|null per slot (reg_number or null)
- payments: list of payment dicts
- notifications: list of {username, message, time}
- reservations: list of {owner, slot, time}

Ma'lumot oqimi (enter → exit)
1. `Parking.enter(reg, owner)` valide qiladi, bo'sh slot topadi yoki agar `owner` uchun rezerv mavjud bo'lsa uni ishlatadi.
2. `cars` ro'yxatiga yozadi, `slots[slot]=reg` qilib belgilaydi, `notifications` ga ogohlantirish qo'shadi.
3. `Parking.exit(reg)` kirish vaqtini o'qib to'lovni hisoblaydi, `payments` ga yozadi, `slots[slot]=None` qiladi, `cars` dan olib tashlaydi va `notifications` ga yozadi.

Integratsiya nuqtalari
- Fayl-saqlash: `parking.storage.JSONStorage` bevosita fayl bilan ishlaydi.
- CLI: `cli.py` foydalanuvchi harakatlarini `Parking` va `AuthService` orqali chaqiradi.

Testlash
- `tests/` da pytest testlari mavjud. `run_tests.py` oddiy runner.
