# 📋 TEXNIK TOPSHIRIQ (TZ) — PARKING BOSHQARUV TIZIMI

**Versiya:** 2.0 (3-Tier Role System)  
**Sana:** 2026-01-20  
**Status:** ✅ Production Ready  
**Til:** Python 3.12 + Uzbek

---

## 1️⃣ LOYIHA MAQSADI VA QAMROVI

### 1.1 Maqsad
Parking slotlarini boshqarish uchun konsolga yo'naltirilgan tizim yaratish. Tizim 3-tier role sistemasi (Admin, Operator, User) bilan foydalanuvchilarni nazorat qiladi va mashinalar kirishi/chiqishi, slotni bronlash, to'lovlarni hisoblash kabi operatsiyalarni boshqaradi.

### 1.2 Qamrov
- **Foydalanuvchilar:** 3 ta rol bilan autentifikatsiya (Admin, Operator, User)
- **Parking:** 10 ta slotni boshqarish
- **To'lovlar:** Soatiga stavka asosida hisoblash (UZS, default 5000.0/soat)
- **Saqlash:** JSON fayl (`data.json`)
- **Testlash:** Pytest bilan 4 ta avtomatlashtirilgan test

### 1.3 Muvaffaqiyat Mezonlari
- ✅ Hamma 4 ta test o'tadi (100%)
- ✅ 3-tier role sistema ishlaydi
- ✅ Hamma CLI operatsiyalari ishlaydi
- ✅ Telefon validatsiyasi (+998 format)
- ✅ Jadval chiqish formatting

---

## 2️⃣ FUNKSIONAL TALABLAR

### 2.1 Autentifikatsiya va Foydalanuvchilar

#### 2.1.1 Ro'yxatdan O'tish (CLI)
**Operator va User** ro'yxatdan o'tishlari mumkin:
```
1. Foydalanuvchi nomini kiriting
2. Parolni kiriting
3. Rol tanlang: 1=Operator, 2=User
4. Telefon raqamini kiriting (+998 ** *** ** **)
```

**Tekshiruv:**
- Username unikallik
- Parol kam 3 ta belgi
- Telefon: +998 formati, 13 ta belgi, raqamlar
- Ro'yxatdan o'tish muvaffaqiyatli → user `data.json`ga qo'shiladi

#### 2.1.2 Admin Yaratish (Script orqali)
**Faqat ichki script orqali:**
```bash
python create_admin.py

Admin username: admin_main
Admin password: secure_pass_123
Admin telefon: +998 90 123 45 67
```

⚠️ **Admin CLI orqali yaratilmaydi!**

#### 2.1.3 Login
```
1. Foydalanuvchi nomini kiriting
2. Parolni kiriting
→ Rol tekshiriladi, mos menyu ko'rsatiladi
```

**Tekshiruv:**
- SHA-256 parol xeshi
- Username va parol to'g'ri yo'q → xatolik
- Login muvaffaqiyatli → role-specific menyu

### 2.2 Parking Operatsiyalari

#### 2.2.1 Mashina Kiritish (`enter`)
```
Avtomobil raqami: 10C234BD (format: \d{2}[A-Z]\d{3}[A-Z]{2})
Egasi: operator_karim
→ Slot tanlandi (bo'sh birinchi), vaqt qayd qilindi
```

**Tekshiruv:**
- Raqam formati to'g'ri
- Bo'sh slot mavjud
- Owner foydalanuvchi mavjud
- Bir mashinaning bir egasi bo'lsa, allaqachon yo'q deb qaytarish

**Data:**
```json
{
  "reg_number": "10C234BD",
  "owner": "operator_karim",
  "entry_time": "2026-01-20T15:30:12",
  "slot": 0,
  "status": "occupied"
}
```

#### 2.2.2 Mashina Chiqarish (`exit`)
```
Avtomobil raqami: 10C234BD
→ Entry vaqti dan exit vaqtiga qarab to'lov hisoblandi
→ Payment saqlandı
```

**Hisoblash:**
```
To'lov = (exit_time - entry_time) / 3600 * RATE_UZS_PER_HOUR
Masalan: 2 soat * 2000 = 4000 UZS
```

**Data:**
```json
{
  "reg_number": "10C234BD",
  "owner": "operator_karim",
  "entry_time": "2026-01-20T15:30:12",
  "exit_time": "2026-01-20T17:30:12",
  "amount": 4000,
  "currency": "UZS"
}
```

#### 2.2.3 Park Holatini Ko'rish
```
Slot | Holat      | Raqam    | Ega            | Kirish vaqti
-----|------------|----------|----------------|------------------
0    | Band       | 10C234BD | operator_karim | 2026-01-20T15:30:12
1    | Bo'sh      |          |                |
2    | Bronlangan |          | user_ali       |
...
```

**Jadval kolonkalari:**
- Slot: 0-9
- Holat: Bo'sh / Band / Bronlangan
- Raqam: Avtomobil raqami (agar band bo'lsa)
- Ega: Foydalanuvchi nomi
- Kirish vaqti: ISO8601 format

#### 2.2.4 Slotni Bronlash
```
Slot raqami: 5 (bo'sh = avtomatik)
→ Slot "Bronlangan" holati
→ Notification: "Slot 5 broni tasdiqlandi"
```

**Data:**
```json
{
  "slot": 5,
  "owner": "user_ali",
  "status": "reserved",
  "reserved_at": "2026-01-20T15:00:00"
}
```

#### 2.2.5 Bronni Bekor Qilish
```
Slot raqami: 5
→ Slot "Bo'sh" holati
→ Notification: "Slot 5 broni bekor qilindi"
```

### 2.3 Ogohlantirishlar (Notifications)

**Saqlanish:**
```json
{
  "username": "user_ali",
  "message": "Slot 5 broni tasdiqlandi",
  "time": "2026-01-20T15:00:00"
}
```

**Ko'rish:**
- Admin: Hamma ogohlantirishlari ko'radi
- Operator: Hamma ogohlantirishlari ko'radi
- User: Faqat o'z ogohlantirishlari

---

## 3️⃣ ROL TIZIMI

### 3.1 Admin (Asosiy Raqib)

**Yaratish:** Script orqali (`python create_admin.py`)

**Menyu Operatsiyalari:**
1. Mashina kiritish (boshqa uchun)
2. Mashina chiqarish (istalgan)
3. Park holatini ko'rish
4. Barcha foydalanuvchilari ro'yxati (jadval)
5. Ogohlantirishlar (hamma)
6. Logout

**Ruxsatlar:**
- ✅ Istalgan mashinani kiritish/chiqarish
- ✅ Istalgan foydalanuvchini ko'rish
- ✅ Hamma ogohlantirishlari ko'rish

### 3.2 Operator (Parkovka Operatori)

**Yaratish:** CLI orqali Rol=1

**Menyu Operatsiyalari:**
1. Mashina kiritish
2. Mashina chiqarish
3. Park holatini ko'rish
4. Barcha foydalanuvchilari ro'yxati
5. Ogohlantirishlar (hamma)
6. Logout

**Ruxsatlar:**
- ✅ Istalgan mashinani kiritish/chiqarish
- ✅ Foydalanuvchilar ro'yxati ko'rish
- ✅ Hamma ogohlantirishlari ko'rish

### 3.3 User (Oddiy Foydalanuvchi)

**Yaratish:** CLI orqali Rol=2

**Menyu Operatsiyalari:**
1. O'z mashinasini kiritish
2. O'z mashinasini chiqarish
3. Park holatini ko'rish
4. Slot bron qilish
5. Bronni bekor qilish
6. Mening ogohlantirishlarim
7. Logout

**Ruxsatlar:**
- ✅ Faqat o'z mashinasini kiritish/chiqarish
- ✅ Slotni bron qilish/bekor qilish
- ✅ Faqat o'z ogohlantirishlari ko'rish

**Cheklantirish:**
- ❌ Boshqa mashinani kiritish/chiqarish
- ❌ Foydalanuvchilar ro'yxati ko'rish
- ❌ Boshqa ogohlantirishlari ko'rish

---

## 4️⃣ MA'LUMOT MODELI

### 4.1 Foydalanuvchi (User)
```python
@dataclass
class User:
    username: str          # Unikallik tekshiriladi
    password_hash: str     # SHA-256
    phone: str            # +998 ** *** ** **
    role: str             # admin | operator | user
```

### 4.2 Avtomobil (Car)
```python
@dataclass
class Car:
    reg_number: str       # 10C234BD (regex: \d{2}[A-Z]\d{3}[A-Z]{2})
    owner: str           # Foydalanuvchi nomi
    entry_time: str      # ISO8601
    slot: int            # 0-9
    status: str          # occupied
```

### 4.3 To'lov (Payment)
```python
@dataclass
class Payment:
    reg_number: str      # Avtomobil raqami
    owner: str          # Foydalanuvchi nomi
    entry_time: str     # ISO8601
    exit_time: str      # ISO8601
    amount: float       # Hisoblangan to'lov
    currency: str       # "UZS"
```

### 4.4 Slot Status
```
Bo'sh (empty)        → Kirish mumkin
Band (occupied)      → Avtomobil mavjud
Bronlangan (reserved) → Foydalanuvchi bronlagan
```

---

## 5️⃣ TEXNIK TALABLAR

### 5.1 Texnologiyalar
- **Dasturlash tili:** Python 3.12
- **Saqlash:** JSON (`data.json`)
- **Testlash:** pytest
- **Arxitektura:** Modular (packages)

### 5.2 Paketlar
```
parking/
  ├── core/           → Yadro (parking, operations, utils)
  ├── models/         → Ma'lumot klasslari
  └── views/          → Formatting
user/
  └── service.py      → AuthService
config/
  └── settings.py     → Global sozlamalar
```

### 5.3 Sozlamalar (`config/settings.py`)
```python
PARKING_SLOTS = 10
RATE_UZS_PER_HOUR = 2000.0
```

---

## 6️⃣ QABUL QILISH MEZONLARI (Acceptance Criteria)

### 6.1 Avtentifikatsiya
- ✅ Operator va User CLI orqali ro'yxatdan o'tishlari mumkin
- ✅ Admin faqat `create_admin.py` orqali yaratiladi
- ✅ Telefon +998 formatida tekshiriladi
- ✅ Parol SHA-256 bilan hashlandi
- ✅ Login muvaffaqiyatli bo'lsa role-specific menyu ko'rsatiladi

### 6.2 Parking Operatsiyalari
- ✅ `enter()` bo'sh slot topadi yoki xatolik beradi
- ✅ `exit()` to'lov hisoblab `payments` ga qo'shadi
- ✅ `view_table()` jadval formatida ko'rsatadi
- ✅ `reserve()` slotni "Bronlangan" qiladi
- ✅ `cancel_reservation()` slotni "Bo'sh" qiladi

### 6.3 Validatsiya
- ✅ Raqam formati: `\d{2}[A-Z]\d{3}[A-Z]{2}` (10C234BD)
- ✅ Telefon formati: `+998 XX YYY ZZ AA` (+998 93 123 45 67)
- ✅ Username: unikallik
- ✅ Parol: kam 1 ta belgi

### 6.4 Data Integrity
- ✅ `data.json` barcha o'zgarishlari qayd qiladi
- ✅ Mashinalar barcha ma'lumotlari saqlanadi

### 6.5 Testing
- ✅ `pytest tests/ -v` → 4/4 PASSED
- ✅ `test_register_and_login` — 3 ta rol uchun
- ✅ `test_enter_and_exit_fee` — to'lov hisoblash
- ✅ `test_parking_full` — 10 ta slotga to'ladigan
- ✅ `test_plate_validation_rejects_invalid` — noto'g'ri raqam

### 6.6 CLI
- ✅ Menyu jadval formatida
- ✅ Notifications jadval formatida
- ✅ Users ro'yxati jadval formatida
- ✅ Park holati jadval formatida
- ✅ Hamma xatoliklar uchun xabar

---

## 7️⃣ XAVFSIZLIK VA HIMOYA

### 7.1 Paroli
- ✅ SHA-256 hashing
- ⏳ Production: passlib/bcrypt ga o'tish

### 7.2 Role-Based Access Control
- ✅ Har bir rol o'z operatsiyalari
- ✅ User boshqa mashinasini o'zgartirib bo'lmaydi
- ✅ Admin script orqali himoyalangan

### 7.3 Data Validatsiya
- ✅ Telefon: +998 format
- ✅ Raqam: Regex pattern
- ✅ Username: Unikallik

---

## 8️⃣ KELAJAKDA YAXSHILASHLAR

### Priority: HIGH
- Passlib/bcrypt ga o'tish
- PostgreSQL database
- Transaction support

### Priority: MEDIUM
- REST API (Flask/FastAPI)
- Web UI (React/Vue)
- Mobile app (React Native)

### Priority: LOW
- Email notifications
- SMS alerts
- ML-based predictions

---

## 9️⃣ YAKUNIY QIYMAT (MVP Features)

✅ **Tayyorlangan:**
- 3-tier role system bilan autentifikatsiya
- Parking slot management (10 slotlar)
- Avtomobil kirishi/chiqishi, bronlash
- To'lovlarni hisoblash (soatiga stavka)
- Role-specific CLI menyulari
- JSON data persistence
- Phone validation (+998 format)
- Automated testing (4/4)
- Comprehensive documentation
- Jadval formatida chiqish

⏳ **Kelajakda:**
- PostgreSQL database
- REST API
- Web/Mobile UI
- Email notifications
- Advanced security

---

**Status:** ✅ **PRODUCTION READY**  
**Version:** 2.0  
**Last Updated:** 2026-01-20
