# 3-Tier Role System Implementation

## Xulosa (Overview)

Parking tizimi endi **3 ta rol** bilan ishlaydi:

1. **Admin** — Asosiy raqib, hamma operatsiyalarni boshqaradi
2. **Operator** — Parking operatorlari, mashinalar kiritish/chiqarish va foydalanuvchilarni nazorat qiladi  
3. **User** — Oddiy foydalanuvchi, faqat o'z mashinasini kiritadi/chiqaradi va bronlaydi

---

## 1. Admin Role (Asosiy raqib)

### Yaratish (Script orqali):
```bash
python create_admin.py

Admin foydalanuvchi nomi: admin_main
Admin parol: secure_password_123
Admin telefon: +998 90 123 45 67

✓ Admin yaratildi!
```

⚠️ **Admin faqat code orqali yaratiladi, CLI orqali emas!**

### Admin menyu operatsiyalari:
- **Mashina kiritish** — Boshqa foydalanuvchi uchun mashina kiritish
- **Mashina chiqarish** — Istalgan mashinani chiqarish
- **Park holati** — Barcha slotlarni ko'rish
- **Barcha foydalanuvchilar** — Tizimning hamma foydalanuvchilarini ko'rish
- **Ogohlantirishlar** — Hamma xabarlarni ko'rish
- **Logout** — Dasturdan chiqish

### Admin mexaniki:
```python
# Admin hisob code orqali yaratiladi
# CLI orqali admin yaratish imkoni yo'q!
python create_admin.py
```

---

## 2. Operator Role (Operator)

### Yaratish (CLI orqali):
```
Ro'yxatdan o'tish → Rol tanlang → 1=Operator → Telefon raqami
```

Keying operatorlar **ordinary users** sifatida CLI orqali ro'yxatdan o'tishlari mumkin.

### Operator menyu operatsiyalari:
- **Mashina kiritish** — Mashinalarni sistemaga kiritish
- **Mashina chiqarish** — Mashinalarni sistemadan chiqarish
- **Park holati** — Parking holatini ko'rish
- **Barcha foydalanuvchilar** — Foydalanuvchilar ro'yxatini ko'rish
- **Ogohlantirishlar** — Ogohlantirish xabarlarini ko'rish
- **Logout** — Chiqish

### Operatskiy vazifalar:
```python
# Operator can enter/exit cars (for any owner)
parking.enter(registration, owner)
parking.exit(registration)

# Operator can view all users
users = storage.get("users")
```

---

## 3. User Role (Foydalanuvchi)

### Yaratish (CLI orqali):
```
Ro'yxatdan o'tish → Rol tanlang → 2=User (default) → Telefon raqami
```

### User menyu operatsiyalari:
- **O'z mashinamni kiritish** — Faqat o'z mashinasini kiritish
- **O'z mashinamni chiqarish** — Faqat o'z mashinasini chiqarish
- **Park holati** — Parking holatini ko'rish
- **Slot bron qilish** — Parking slotini oldinga bron qilish
- **Bronni bekor qilish** — Bron bekor qilish
- **Mening ogohlantirishlarim** — Shaxsiy xabarlarini ko'rish
- **Logout** — Chiqish

### Foydalanuvchi mexaniki:
```python
# User can only enter their own car
parking.enter(registration, username)  # username == owner

# User can only exit their own car
parking.exit(registration)

# User can reserve slots
parking.reserve(username, slot)

# User can only see their own notifications
my_notes = [n for n in notifications if n["username"] == username]
```

---

## CLI Implementation

### Main Menu (login qilmasdan):
```
1. Ro'yxatdan o'tish
2. Kirish  
3. Park holatini ko'rish (umumiy)
4. Dasturdan chiqish
```

### Registration Flow (CLI):
```
1. Foydalanuvchi nomi so'roqlang
2. Parol so'roqlang
3. Operator/User tanlash:
   - 1 = Operator
   - 2 = User (default)
4. Telefon raqami so'roqlang (+998 format)
```

⚠️ **Admin faqat `create_admin.py` script orqali yaratiladi!**

### Login & Menu Selection:
```
1. Username va password kiriting
2. Sistema rolni tekshiradi
3. Rolga qarab menyu ko'rsatadi:
   - Admin => Admin menyu (_admin_menu)
   - Operator => Operator menyu (_operator_menu)
   - User => User menyu (_user_menu)
```

---

## Code Changes

### cli.py
- `ADMIN_SECRET_CODE = "ADMIN_2024"` — Maxfiy kod
- `_show_role_menu(role, username, parking, storage)` — Rolga qarab menyu
- `_admin_menu()` — Admin operatsiyalari
- `_operator_menu()` — Operator operatsiyalari
- `_user_menu()` — User operatsiyalari

### Telefon Validation
```python
# Format: +998 ** *** ** **
# Masalan: +998 93 123 45 67
auth.phone_valid(phone)
```

### Table Formatters
```python
format_users_table(users)  # Displays: Foydalanuvchi | Telefon | Rol
format_parking_table()     # Displays: Slot | Holat | Raqam | Ega | Vaqt
format_menu(options)       # Displays: Raqam | Variant
```

---

## Test Results

```
✅ test_auth.py::test_register_and_login PASSED
✅ test_parking.py::test_enter_and_exit_fee PASSED
✅ test_parking.py::test_parking_full PASSED
✅ test_parking.py::test_plate_validation_rejects_invalid PASSED
```

All 4 tests pass with new phone validation and 3-tier role system.

---

## Demo Script

Run `demo_three_tier_system.py` to see all roles in action:

```bash
python demo_three_tier_system.py
```

Output:
- 3 ta foydalanuvchi yaratiladi (admin, operator, user)
- Ularning rollari jadval bilan ko'rsatiladi
- Turli operatsiyalar amalga oshiriladi
- Park holati ko'rsatiladi

---

## Xavfsizlik Eslatmalari (Security Notes)

1. **Admin kodi hardcoded**: Production uchun `config/settings.py` ga ko'chiring
2. **SHA-256 hashing**: Parolar `user/service.py` da hashed saqlanadi
3. **Rol-based access**: CLI har bir rolga qarab turli menyularni ko'rsatadi
4. **Phone validation**: +998 formatini qat'iy tekshiradi

---

## Navbatdagi Bunyodlar (Future Enhancements)

1. 🔐 Password hashing → passlib ga o'tish
2. 📧 Email notifications → OTP sistema
3. 💳 Payment integration → UZS to'lovlari
4. 📱 Mobile app → Flask/Django REST API
5. 🗄️ PostgreSQL → ma'lumotlar bazasiga o'tish

---

## Foydalanish (Usage)

### Terminal orqali:
```bash
python main.py
```

### Test orqali:
```bash
pytest tests/ -v
```

### Demo orqali:
```bash
python demo_three_tier_system.py
```

---

**Yaratilgan:** 2026-01-20  
**Versiya:** 2.0 (3-Tier Role System)  
**Til:** Uzbek + Python 3.12
