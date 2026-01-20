# Parking Tizimi - 3-Tier Role System (v2.0)

Oddiy konsolga yo'naltirilgan Parking tizimi (Python). **3-tier role system** bilan: Admin (script), Operator (CLI), va User (CLI).

## 🚀 Tez Start

### 1. Virtual environment
```bash
source .venv/bin/activate
```

### 2. Paketlar o'rnatish
```bash
pip install -r requirements.txt
```

### 3. Admin yaratish (Script orqali)
```bash
python create_admin.py

Admin foydalanuvchi nomi: admin_main
Admin parol: secure_password_123
Admin telefon: +998 90 123 45 67
```

### 4. CLI ishga tushurish
```bash
python main.py
```

## ✨ Asosiy Xususiyatlar

- ✅ **3-Tier Role System** — Admin (script), Operator (CLI), User (CLI)
- ✅ **Phone Validation** — +998 format
- ✅ **Foydalanuvchi ro'yxatdan o'tish va login**
- ✅ **Avtomobil kirishi/chiqishi** — slotlarni boshqarish
- ✅ **Bronlash va bronni bekor qilish**
- ✅ **To'lovlarni hisoblash** — soatiga stavka (UZS)
- ✅ **JSON saqlash** — `data.json`
- ✅ **Jadval UI** — formatted jadvalda hammasini ko'rish
- ✅ **Automated tests** — 4/4 ✅

## 📁 Struktura

```
parking/          → Core package
  ├── core/       → Business logic
  ├── models/     → Data models
  └── views/      → UI formatters

user/service.py   → AuthService
cli.py            → Main interface
create_admin.py   → Admin script
tests/            → Automated tests
```

## 🎯 Setup

**Admin:** `python create_admin.py` (script orqali)  
**Operator/User:** `python main.py` (CLI orqali)

## 📚 Documentation

Batafsil: [USAGE_GUIDE.md](USAGE_GUIDE.md), [QUICK_REFERENCE.md](QUICK_REFERENCE.md), [ROLE_SYSTEM.md](ROLE_SYSTEM.md)

## 🧪 Tests

```bash
pytest tests/ -v
# 4/4 PASSED ✅
```

## 🔐 Security

- ✅ Password hashing (SHA-256)
- ✅ Role-based access control
- ✅ Phone validation (+998 format)
- ✅ Admin protection (script orqali)

---

**Version:** 2.0 | **Status:** ✅ Production Ready | **Language:** Python 3.12 + Uzbek
