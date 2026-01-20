# 📋 QUICK REFERENCE CARD - 3-Tier Parking System

## 🎯 Tezkor Sarlavha

```
┌─────────────────────────────────────────────────────┐
│    PARKING TIZIMI - 3-TIER ROLE SYSTEM v2.0        │
│                                                     │
│    Admin | Operator | User                         │
│    Jadval UI | Phone +998 | Uzbek Doc              │
└─────────────────────────────────────────────────────┘
```

---

## 🚀 Boshlash (3 ta variant)

### 1. Admin yaratish (Script orqali)
```bash
python create_admin.py

Admin foydalanuvchi nomi: admin_main
Admin parol: secure_password_123
Admin telefon: +998 90 123 45 67
```

### 2. Interactive CLI (Operator va User)
```bash
python main.py
```

### 3. Demo (Auto)
```bash
python demo_three_tier_system.py
```

### 4. Tests
```bash
pytest tests/ -v
```

---

## 🔑 Login Malumotlari (Default)

| Rol | Username | Password | Yaratish |
|-----|----------|----------|----------|
| Admin | admin_main | admin_pass | python create_admin.py |
| Operator | operator_karim | op_pass123 | CLI ro'yxatdan o'tish |
| User | user_ali | user_pass | CLI ro'yxatdan o'tish |

---

## 📱 Telefon Formati

```
✅ +998 93 123 45 67   (To'g'ri)
✅ +998 90 999 88 77   (To'g'ri)
❌ 99893123456789      (Yo'q: + kerak)
❌ +998 9 123 45 67    (Yo'q: raqam to'liq)
```

---

## 🎮 Har bir Rol uchun Menyu

### Admin Menyu (Script orqali yaratiladi)
```
1. Mashina kiritish (boshqa uchun)
2. Mashina chiqarish
3. Park holatini ko'rish
4. Barcha foydalanuvchilar ro'yxati
5. Ogohlantirishlar
6. Logout
```

### Operator Menyu (CLI orqali)
```
1. Mashina kiritish
2. Mashina chiqarish
3. Park holatini ko'rish
4. Barcha foydalanuvchilar
5. Ogohlantirishlar
6. Logout
```

### User Menyu (CLI orqali)
```
1. O'z mashinamni kiritish
2. O'z mashinamni chiqarish
3. Park holatini ko'rish
4. Slot bron qilish
5. Bronni bekor qilish
6. Mening ogohlantirishlarim
7. Logout
```

---

## 🔐 Rol Imkoniyatlari

```
┌─────────────────────┬──────┬──────────┬──────┐
│ Operatsiya          │Admin │Operator  │User  │
├─────────────────────┼──────┼──────────┼──────┤
│ Mashina kiritish    │  ✅  │   ✅     │  ✅* │
│ Mashinani chiqarish │  ✅  │   ✅     │  ✅* │
│ Foydalanuvchilarni  │  ✅  │   ✅     │  ❌  │
│ ko'rish             │      │          │      │
│ Slotni bron qilish  │  ✅  │   ❌     │  ✅  │
│ Bron bekor qilish   │  ✅  │   ❌     │  ✅  │
│ Park holati ko'rish │  ✅  │   ✅     │  ✅  │
│ Ogohlantirishlari   │  ✅  │   ✅     │  ✅* │
│ ko'rish             │      │          │      │
└─────────────────────┴──────┴──────────┴──────┘
* Faqat o'z mashinasi/xabarlari
```

---

## 📚 Dokumentatsiya

| File | Tushuntirish |
|------|-------------|
| README.md | Tezkor boshlash |
| ARCHITECTURE.md | Texnik arxitektura |
| TZ.md | Uzbek talablar |
| ROLE_SYSTEM.md | Rol tafsilotlari |
| **USAGE_GUIDE.md** | 👈 Boshlang |
| DEPLOYMENT.md | Production |
| PROJECT_SUMMARY.md | Xulosa |

---

## 🏗️ Loyiha Tuzilishi

```
parking/
  ├── models/          (User, Car, Payment)
  ├── core/            (Business logic)
  ├── views/           (UI layer)
  ├── storage.py       (JSON storage)
  └── auth.py          (Authentication)

user/
  └── service.py       (AuthService)

config/
  └── settings.py      (Global settings)

tests/
  ├── test_auth.py
  └── test_parking.py

cli.py                 (Main interface)
main.py                (Entry point)
```

---

## 🧪 Test Natijasi

```bash
✅ test_register_and_login         PASSED
✅ test_enter_and_exit_fee          PASSED
✅ test_parking_full                PASSED
✅ test_plate_validation            PASSED

4/4 PASSED ✓
```

---

## ⚡ Tez Operatsiyalar

### Admin mashinani kiritish:
```
Menu: 1
Raqam: 10C234BD
Ega: operator_karim
→ ✓ Kiritildi
```

### User mashinasini chiqarish:
```
Menu: 2
Raqam: 20D456EF
→ ✓ To'lov: 15000 UZS
```

### Foydalanuvchilarni ko'rish:
```
Menu: 4 (Admin/Operator)
→ Jadval: Foydalanuvchi | Telefon | Rol
```

---

## 💾 Data Fayllari

```
data.json           → Live data
demo_data.json      → Demo data
test_data.json      → Test fixtures
```

---

## 🔍 Debugging Komandalari

```bash
# Testlarni ishga tushirish
pytest tests/ -v

# Demo
python demo_three_tier_system.py

# CLI
python main.py

# Fayllarni ko'rish
ls -la parking/
ls -la tests/
```

---

## 📊 Jadval Formatteri

**Users:**
```
Foydalanuvchi  | Telefon           | Rol     
admin_user     | +998 90 123 45 67 | admin   
```

**Park Status:**
```
Slot | Holat | Raqam    | Ega        | Vaqt
0    | Band  | 10C234BD | admin_user | 2026-01-20T...
```

**Menu:**
```
Raqam | Variant
1     | Mashina kiritish
```

---

## 🔒 Xavfsizlik

| Feature | Status |
|---------|--------|
| Password Hashing | SHA-256 ✅ |
| Role-based Access | ✅ |
| Phone Validation | +998 ✅ |
| Admin Protection | ADMIN_2024 ✅ |

---

## 🎓 Foydalanish Yo'li

1. **Birinchi:** README.md + demo
2. **Ikkinchi:** USAGE_GUIDE.md
3. **Uchinchi:** CLI `python main.py`
4. **To'rtinchi:** Tests `pytest tests/ -v`

---

## ✅ Checklist

- [x] 3-tier role system
- [x] Phone validation
- [x] Table UI
- [x] Documentation
- [x] Tests (4/4 pass)
- [x] Demo script
- [x] Security
- [x] Uzbek language

---

## 🔒 Maxfiy Kodlar

```
Admin yaratish = python create_admin.py (script orqali)
Operator = CLI orqali ro'yxatdan o'tish (1=Operator)
User = CLI orqali ro'yxatdan o'tish (2=User)

⚠️ Admin CLI orqali yaratilmaydi!
```

---

## 📞 Qo'llab-Quvvatlash

- 📧 Email: support@
- 💬 Telegram: @
- 🔗 GitHub: https://github.com/

---

## 🚀 Status

```
✅ DEVELOPMENT:   Complete
✅ TESTING:       4/4 PASSED
✅ DOCUMENTATION: 7 files
✅ PRODUCTION:    Ready
```

---

**Version:** 2.0  
**Status:** ✅ Production Ready  
**Language:** Python 3.12 + Uzbek  
**Last Update:** 2026-01-20
