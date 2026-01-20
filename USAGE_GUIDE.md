# 3-Tier Role System - Foydalanish Qo'llanmasi

## 🚀 Tezkor Boshlash

### 1. Admin yaratish (Script orqali)

```bash
python create_admin.py

Admin foydalanuvchi nomi: admin_main
Admin parol: secure_password_123
Admin telefon: +998 90 123 45 67
```

✅ Admin yaratildi!

#### Operator yaratish:
```
Tanlang: 1 (Ro'yxatdan o'tish)
Foydalanuvchi nomi: karim_op
Parol: op123456
Admin kodi: (bo'sh - Enter)
Rol: 1 (Operator)
Telefon: +998 91 500 60 70
```
✅ Operator yaratildi!

#### User yaratish:
```
Tanlang: 1 (Ro'yxatdan o'tish)
Foydalanuvchi nomi: ali_user
Parol: user123
Rol: 2 (User) yoki (bo'sh)
Telefon: +998 92 333 44 55
```
✅ User yaratildi!

---

## 🔑 Har bir Rol uchun Amallar

### 👨‍💼 Admin Operatsiyalari

**Login:**
```
Tanlang: 2 (Kirish)
Foydalanuvchi: admin_main
Parol: secure_password_123
```

**Admin Menyu:**
```
[ADMIN MENYU]
Raqam | Variant
------+----------------------------------
1     | Mashina kiritish (boshqa uchun)
2     | Mashina chiqarish
3     | Park holatini ko'rish
4     | Barcha foydalanuvchilar ro'yxati
5     | Ogohlantirishlar
6     | Logout
```

**Misollar:**

1️⃣ **Operator uchun mashina kiritish:**
```
Admin menyu: 1
Avtomobil raqami: 10C234BD
Egasi: karim_op
→ ✓ Mashina kiritildi
```

2️⃣ **Mashinani chiqarish:**
```
Admin menyu: 2
Avtomobil raqami: 10C234BD
→ ✓ To'lov: 0.0 UZS
```

3️⃣ **Park holatini ko'rish:**
```
Admin menyu: 3
→ Hamma slotlar ko'rsatiladi
```

4️⃣ **Foydalanuvchilarni ko'rish:**
```
Admin menyu: 4
→ Jadval: Foydalanuvchi | Telefon | Rol
```

---

### 🏢 Operator Operatsiyalari

**Login:**
```
Tanlang: 2 (Kirish)
Foydalanuvchi: karim_op
Parol: op123456
```

**Operator Menyu:**
```
[OPERATOR MENYU]
Raqam | Variant
------+---------------------------
1     | Mashina kiritish
2     | Mashina chiqarish
3     | Park holatini ko'rish
4     | Barcha foydalanuvchilar
5     | Ogohlantirishlar
6     | Logout
```

**Misollar:**

1️⃣ **Mashina kiritish (o'z vazifasida):**
```
Operator menyu: 1
Avtomobil raqami: 20D567EF
Egasi: ali_user
→ ✓ Mashina kiritildi
```

2️⃣ **Mashinani chiqarish:**
```
Operator menyu: 2
Avtomobil raqami: 20D567EF
→ ✓ To'lov: 15000 UZS
```

3️⃣ **Foydalanuvchilarni ko'rish:**
```
Operator menyu: 4
→ Hamma foydalanuvchilar jadvalda ko'rsatiladi
```

---

### 👤 User Operatsiyalari

**Login:**
```
Tanlang: 2 (Kirish)
Foydalanuvchi: ali_user
Parol: user123
```

**User Menyu:**
```
[FOYDALANUVCHI MENYU]
Raqam | Variant
------+----------------------------------
1     | O'z mashinamni kiritish
2     | O'z mashinamni chiqarish
3     | Park holatini ko'rish
4     | Slot bron qilish
5     | Bronni bekor qilish
6     | Mening ogohlantirishlarim
7     | Logout
```

**Misollar:**

1️⃣ **O'z mashinasini kiritish:**
```
User menyu: 1
Avtomobil raqami: 30E891GH
→ ✓ Mashinangiz kiritildi
```

2️⃣ **O'z mashinasini chiqarish:**
```
User menyu: 2
Avtomobil raqami: 30E891GH
→ ✓ To'lov: 20000 UZS
```

3️⃣ **Slotni bron qilish:**
```
User menyu: 4
Slot raqami: (bo'sh - avtomatik)
→ ✓ Bron tasdiqlandi — slot 5
```

4️⃣ **Bronni bekor qilish:**
```
User menyu: 5
Slot raqami: 5
→ ✓ Bron bekor qilindi
```

5️⃣ **Mening ogohlantirishlarim:**
```
User menyu: 6
→ Faqat shu user ning xabarlari ko'rsatiladi
```

---

## 📋 Jadval Formatlari

### Foydalanuvchilar Jadv ali
```
Foydalanuvchi  | Telefon           | Rol     
---------------+-------------------+---------
admin          | +998 90 123 45 67 | admin   
karim_op       | +998 91 500 60 70 | operator
ali_user       | +998 92 333 44 55 | user    
```

### Park Holati Jadv ali
```
Slot | Holat  | Raqam    | Ega      | Kirish vaqti           
-----+--------+----------+----------+------------------------
0    | Band   | 10C234BD | karim_op | 2026-01-20T15:20:12
1    | Bo'sh  |          |          |                         
2    | Bo'sh  |          |          |                         
3    | Bo'sh  |          |          |                         
...
```

### Menyu Jadv ali
```
Raqam | Variant
------+----------------------------------
1     | Mashina kiritish
2     | Mashina chiqarish
3     | Park holati
...
```

---

## 🔐 Maxfiy Kodlar va Talqinlar

| Rol      | Admin Kodi   | Telefo Format       | Status    |
|----------|--------------|-------------------|-----------|
| Admin    | ADMIN_2024   | +998 90-99 *** ** ** | Maxfiy  |
| Operator | (yo'q)       | +998 90-99 *** ** ** | Ochiq   |
| User     | (yo'q)       | +998 90-99 *** ** ** | Ochiq   |

### Telefon Formatini Tushunish:
```
✓ +998 93 123 45 67  — To'g'ri
✗ 998 93 123 45 67   — Yo'q (+ kerak)
✗ +998 9 123 45 67   — Yo'q (ikki raqam kerak)
✗ +998 93 1 45 67    — Yo'q (to'liq format kerak)
```

---

## 📊 Rol Imkoniyatlari Solishtirmasi

| Operatsiya | Admin | Operator | User |
|-----------|-------|----------|------|
| Mashina kiritish (boshqa uchun) | ✅ | ✅ | ❌ |
| Mashina kiritish (o'zining) | ✅ | ✅ | ✅ |
| Mashinani chiqarish | ✅ | ✅ | ✅ (faqat o'zi) |
| Foydalanuvchilar ro'yxati | ✅ | ✅ | ❌ |
| Slotni bron qilish | ✅ | ❌ | ✅ |
| Ogohlantirishlarni ko'rish | ✅ (hamma) | ✅ (hamma) | ✅ (shaxsiy) |
| Admin kodini kiriting | ✅ (ADMIN_2024) | ❌ | ❌ |

---

## 🧪 Test va Demo

### Hamma testlarni o'tkazish:
```bash
pytest tests/ -v
```

### 3-Tier rol sistemasini demo:
```bash
python demo_three_tier_system.py
```

### CLI interaktiv rejimda:
```bash
python main.py
```

---

## 🐛 Tez-tez Solagular

**S:** Admin kodini unutdim!  
**J:** `ADMIN_2024` ni yana kiriting. Production uchun `config/settings.py` ga o'zgartiring.

**S:** Telefon noto'g'ri deb aytadi!  
**J:** Format: `+998 XX YYY ZZ AA` (masalan: `+998 93 123 45 67`)

**S:** Boshqa user uchun mashina kirita olamman?  
**J:** Faqat Admin yoki Operator - `Mashina kiritish` menyu bandiga kirishingiz kerak.

**S:** Mening ogohlantirishlari nima?  
**J:** Faqat User menyu: `Mening ogohlantirishlarim` → shaxsiy xabarlar ko'rsatiladi.

---

## 📞 Har bir rol uchun Telefon Misollari

| Rol      | Telefon Misollar         |
|----------|--------------------------|
| Admin    | +998 90 123 45 67        |
|          | +998 91 500 60 70        |
|          | +998 92 999 88 77        |
| Operator | +998 93 111 22 33        |
|          | +998 94 444 55 66        |
| User     | +998 95 777 88 99        |
|          | +998 96 321 654 987      |

---

## ✨ Xulosa

Siz endi 3 ta rol bilan ishlatasiz:
- 🔒 **Admin** — Barcha operatsiyalar
- 💼 **Operator** — Parking operatsiyalari
- 👤 **User** — Shaxsiy operatsiyalar

Har bir rol o'z menyusi, o'z imkoniyatlari va o'z cheklantirmalari bilan fariqi!

---

**Last Updated:** 2026-01-20  
**Version:** 2.0
