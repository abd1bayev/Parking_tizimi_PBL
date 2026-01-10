# Parking Tizimi

Oddiy konsolga yo'naltirilgan Parking tizimi (Python). Loyihaning maqsadi — mashinalarni ro‘yxatga olish, parkga kiritish/chiqarish, bronlash va to‘lovlarni JSON fayl orqali saqlash.

Tez start

- Virtual environmentni faollashtiring (agar kerak bo'lsa):
```
source venv/bin/activate
```
- Paketlar o'rnatish:
```
pip install -r requirements.txt
```
- CLI ishga tushurish:
```
python main.py
```

Asosiy xususiyatlar
- Foydalanuvchi ro'yxatdan o'tkazish va login (rol: `user` yoki `admin`).
- Avtomobil kirishi va chiqishi — slotlarni boshqarish.
- Bronlash va bronni bekor qilish.
- To'lovlarni hisoblash (soatiga konfiguratsiyalangan stavka, `UZS`).
- JSON fayl bilan saqlash (`data.json`).

Loyihaning struktura (eng muhim fayllar)
- `parking/` — paket: saqlash, asosiy biznes mantiq va kichik yordamchi modullar.
  - `parking/core/` — `Parking` klassi, `operations`, `utils`.
  - `parking/models/` — `User`, `Car`, `Payment` dataclasslari.
  - `parking/views/` — jadval chiqarish yordamchilari.
- `user/service.py` — autentifikatsiya va ro'yxatdan o'tish.
- `cli.py` — konsol interfeysi.
- `data.json` — ilova saqlovchi fayli.
- `tests/` — pytest testlari.

Admin yaratish
- Eng tez usul (python yordamida):
```
python - <<'PY'
from parking.storage import JSONStorage
from user.service import AuthService
s = JSONStorage('data.json')
auth = AuthService(s)
auth.royxatdan_otish('admin','SizningParolingiz','admin@example.uz', role='admin')
print(s.get('users'))
PY
```

Keyingi qadamlar / Takliflar
- Parol xavfsizligini oshirish (`passlib` yoki `bcrypt`).
- Unit testlarni kengaytirish va CI qo'shish.
- JSON o'rniga kichik RDBMS yoki NoSQL (masalan Cosmos DB) uchun adapter.

README: shunchaki boshlash uchun. Batafsil arxitektura va TZ fayllari repositoryda mavjud: `ARCHITECTURE.md`, `TZ.md`.
# Parking_tizimi_PBL

Simple parking system implemented in Python (console-based).

Quick start:

1. Run the app:

```bash
python3 main.py
```

2. Run the simple tests:

```bash
python3 run_tests.py
```
# Parking_tizimi_PBL