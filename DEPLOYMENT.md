# 3-Tier Parking Sistem - Deploy va Sozlash

## 📦 Talablar

- Python 3.8+
- Linux/macOS/Windows
- ~50 MB disk space

## 🔧 O'rnatish (Installation)

### 1. Repozitoriyani klonlash
```bash
git clone https://github.com/yourusername/Parking_tizimi_PBL.git
cd Parking_tizimi_PBL
```

### 2. Virtual environment yaratish
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# yoki
.venv\Scripts\activate  # Windows
```

### 3. Dependensiyalarni o'rnatish
```bash
pip install -r requirements.txt
pip install pytest  # testlar uchun
```

### 4. Konfiguratsiyani tekshirish
```bash
cat config/settings.py
```

Defaults:
```python
PARKING_SLOTS = 10
RATE_UZS_PER_HOUR = 2000.0
ADMIN_SECRET_CODE = "ADMIN_2024"  # CHANGE THIS IN PRODUCTION!
```

---

## 🚀 Ishga Tushirish

### Interaktiv rejimda:
```bash
python main.py
```

### Test rejimda:
```bash
pytest tests/ -v
```

### Demo rejimda:
```bash
python demo_three_tier_system.py
```

---

## 📋 Dastlabki Sozlash

### Step 1: Admin yaratish (Script orqali)
```bash
python create_admin.py

Admin foydalanuvchi nomi: admin_main
Admin parol: secure_password_123
Admin telefon: +998 90 123 45 67
```

✅ Admin yaratildi!

### Step 2: Operatorlarni qo'shish (CLI orqali)
```bash
python main.py
Tanlang: 1 (Ro'yxatdan o'tish)
Rol: 1 (Operator)
```

### Step 3: Foydalanuvchilarni qo'shish (CLI orqali)
```bash
python main.py
Tanlang: 1 (Ro'yxatdan o'tish)
Rol: 2 (User)
```

---

## 🔒 Xavfsizlik Sozlamalari

### Production uchun:

#### 1. Admin parolini xavfsiz saqlash
**create_admin.py** skripti orqali admin yaratayotganda kuchli parol kiriting:
```bash
python create_admin.py

Admin parol: YourVeryStrongPassword12345!@#
```

#### 2. Script faylini o'chirish (optional)
Admin yaratgandan keyin:
```bash
# Keying admin yaratishning oldini olish uchun
chmod 000 create_admin.py
# yoki o'chirish
rm create_admin.py
```

#### 3. Parol xashlashni kuchaytirib turish
**user/service.py** ni yangilang (Future):
```python
# FROM: hashlib.sha256()
# TO: from passlib.context import CryptContext
# crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
```

#### 4. Telefon validatsiyasini qat'iy saqlash
**parking/auth.py** ga qo'shimcha tekshiruv:
```python
def phone_valid(phone):
    # +998 formatni qat'iy tekshirish
    pattern = r'^\+998\s\d{2}\s\d{3}\s\d{2}\s\d{2}$'
    return bool(re.match(pattern, phone))
```

---

## 📊 Data Backup

### Haftasiga bir marta backup qiling:
```bash
cp data.json data.json.backup.$(date +%Y-%m-%d)
```

### Backup dan qaytarish:
```bash
cp data.json.backup.2026-01-20 data.json
```

---

## 🐛 Debugging

### Log-larni ko'rish:
```bash
# Demo bilan
python demo_three_tier_system.py 2>&1 | tee app.log

# Testlar bilan
pytest tests/ -v -s 2>&1 | tee test.log
```

### Common issues:

| Muammo | Yechim |
|--------|--------|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| `Invalid phone format` | `+998 XX YYY ZZ AA` formatini tekshiring |
| `Admin kodi noto'g'ri` | `ADMIN_2024` ni eng ko'pik! |
| `Port already in use` | CLI server portini o'zgartiring |

---

## 📈 Monitoring

### System Health Check:
```bash
#!/bin/bash
# health_check.sh

echo "=== Parking System Health Check ==="

# Check Python
python --version

# Check files
echo "Files:"
ls -lh data.json config/settings.py

# Check tests
pytest tests/ -q

# Check storage
echo "Data size:"
du -h data.json

echo "=== HEALTHY ✓ ==="
```

### Cron job (Linux/macOS):
```bash
# Har kuni soat 2:00 da backup qiling
0 2 * * * /path/to/backup.sh

# Har soat health check qiling  
0 * * * * /path/to/health_check.sh
```

---

## 📱 Rol-ga Qarab Izlashlar

### Admin izlashlar:
- `admin@parksystem.com` — hamma xabarlar
- `admin-panel/` — admin panel
- `ADMIN_2024` — maxfiy kod

### Operator izlashlar:
- `operator@parksystem.com` — opertor xabarlari
- `operator-dashboard/` — operator panel

### User izlashlar:
- `user@parksystem.com` — user xabarlari
- `my-cars/` — mening mashinalarim
- `my-reservations/` — mening bronlarim

---

## 🔄 Versiyalarni O'nglash

### Version 1.0 → 2.0 (3-Tier Role System)
```
git pull origin main
pip install -r requirements.txt
python demo_three_tier_system.py
```

### Backward compatibility:
```python
# Old code still works
auth.royxatdan_otish("user", "pass", "phone")  # ✅
# New code with roles
auth.royxatdan_otish("user", "pass", "phone", role="operator")  # ✅
```

---

## 🌐 API (Future)

### REST Endpoints (coming soon):
```
POST /api/auth/register
POST /api/auth/login
GET /api/parking/status
POST /api/parking/enter
POST /api/parking/exit
GET /api/users
GET /api/users/{id}
```

---

## 📞 Qo'llab-Quvvatlash

### Savollar:
- 📧 Email: support@parksystem.uz
- 💬 Telegram: @parksystem_bot
- 🔗 GitHub Issues: github.com/yourrepo/issues

### Dokumentatsiya:
- [README.md](README.md) — Umumiy malumot
- [ARCHITECTURE.md](ARCHITECTURE.md) — Arxitektura
- [ROLE_SYSTEM.md](ROLE_SYSTEM.md) — Rol sistema
- [USAGE_GUIDE.md](USAGE_GUIDE.md) — Foydalanish
- [TZ.md](TZ.md) — Texnik talablar

---

## ✅ Deployment Checklist

- [ ] Python 3.8+ o'rnatilgan
- [ ] Virtual environment aktivlashtirilgan
- [ ] `pip install -r requirements.txt` bajarilgan
- [ ] Tests `pytest tests/ -v` bilan o'tgan
- [ ] Admin kodi o'zgartirilgan
- [ ] `data.json` backup qilingan
- [ ] `config/settings.py` tekshirilgan
- [ ] Demo `python demo_three_tier_system.py` bilan o'tgan
- [ ] Cron job-lar o'rnatilgan (optional)
- [ ] Documentation o'qilgan

---

## 📅 Production Timeline

| Sana | Faza | Status |
|------|------|--------|
| 2026-01-20 | v2.0 3-Tier Roles | ✅ Done |
| 2026-02-15 | API REST | 🔄 WIP |
| 2026-03-01 | Mobile App | 📅 Planned |
| 2026-04-01 | PostgreSQL | 📅 Planned |
| 2026-05-01 | Azure Cloud | 📅 Planned |

---

## 🎓 Foydalanish Qo'llanmalari

1. **Birinchi marta:**
   - [README.md](README.md) ni o'qing
   - `python demo_three_tier_system.py` ni ishga tushiring
   - [USAGE_GUIDE.md](USAGE_GUIDE.md) ni o'qing

2. **Qo'shimcha tafsilot:**
   - [ROLE_SYSTEM.md](ROLE_SYSTEM.md) — Rol tafsilotlari
   - [ARCHITECTURE.md](ARCHITECTURE.md) — Texnik arxitektura
   - [TZ.md](TZ.md) — Texnik talablar

3. **Debugging:**
   - Tests: `pytest tests/ -v`
   - Demo: `python demo_three_tier_system.py`
   - Logs: `tail -f app.log`

---

**Created:** 2026-01-20  
**Last Updated:** 2026-01-20  
**Version:** 2.0  
**Language:** Python 3.12 + Uzbek
