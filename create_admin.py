#!/usr/bin/env python3
"""
Admin hisob yaratish script
Faqat ichki ishlatish uchun - CLI orqali emas!

Misal:
    python create_admin.py
    Admin username: admin_main
    Admin password: secure_password_123
    Admin telefon: +998 90 123 45 67
    
    ✓ Admin yaratildi!
    Operatorlar bu admin hisobidan dostup oladi.
"""

from parking.storage import JSONStorage
from user.service import AuthService

def create_admin():
    """Admin hisob yaratish"""
    storage = JSONStorage("data.json")
    auth = AuthService(storage)
    
    print("\n" + "="*50)
    print("ADMIN YARATISH SCRIPT (ICHKI ISHLATISH)")
    print("="*50)
    
    # Admin ma'lumotlarini so'rash
    username = input("\nAdmin foydalanuvchi nomi: ").strip()
    
    # Username mavjud tekshirish
    users = storage.get("users")
    if any(u.get("username") == username for u in users):
        print(f"✗ Foydalanuvchi '{username}' allaqachon mavjud!")
        return False
    
    password = input("Admin parol: ")
    
    # Telefon validatsiyasi
    while True:
        phone = input("Admin telefon nomerini kiriting (+998 ** *** ** **): ").strip()
        if auth.phone_valid(phone):
            break
        print("✗ Telefon noto'g'ri. Format: +998 ** *** ** ** (masalan: +998 90 123 45 67)")
    
    # Admin yaratish
    result = auth.royxatdan_otish(username, password, phone, role="admin")
    
    if result:
        print("\n" + "="*50)
        print("✅ ADMIN YARATILDI!")
        print("="*50)
        print(f"\nUsername: {username}")
        print(f"Telefon:  {phone}")
        print(f"Rol:      admin")
        print("\n📝 Eslatma:")
        print("   - Operatorlar cli.py orqali ro'yxatdan o'tishlari mumkin")
        print("   - Bu admin hisobi faqat ichki ishlatish uchun!")
        print("   - Parol xavfsiz saqlang!")
        print("\n" + "="*50)
        return True
    else:
        print(f"✗ Admin yaratishda xatolik!")
        return False


if __name__ == "__main__":
    create_admin()
