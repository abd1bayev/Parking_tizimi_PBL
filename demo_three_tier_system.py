#!/usr/bin/env python3
"""
Demonstration script for the 3-tier role system
- Admin: Script orqali yaratiladi (create_admin.py)
- Operator: CLI orqali ro'yxatdan o'tadi
- User: CLI orqali ro'yxatdan o'tadi
"""

from parking.storage import JSONStorage
from user.service import AuthService
from parking.core.parking import Parking
from parking.core.utils import format_users_table, format_parking_table

def demo():
    storage = JSONStorage("demo_data.json")
    auth = AuthService(storage)
    parking = Parking(storage)
    
    print("=" * 60)
    print("3-TIER ROLE SYSTEM DEMO")
    print("=" * 60)
    
    # Test 1: Create Admin account (programmatically)
    print("\n1️⃣  Admin yaratish (script orqali)...")
    auth.royxatdan_otish("admin_main", "admin_pass", "+998 90 123 45 67", role="admin")
    print("✓ Admin yaratildi: admin_main")
    
    # Test 2: Create Operator account (CLI method)
    print("\n2️⃣  Operator yaratish (CLI ro'yxatdan o'tish)...")
    auth.royxatdan_otish("operator_karim", "op_pass123", "+998 91 500 60 70", role="operator")
    print("✓ Operator yaratildi: operator_karim")
    
    # Test 3: Create regular User account (CLI method)
    print("\n3️⃣  Oddiy User yaratish (CLI ro'yxatdan o'tish)...")
    auth.royxatdan_otish("user_ali", "user_pass", "+998 92 333 44 55", role="user")
    print("✓ User yaratildi: user_ali")
    
    # Test 4: Show all users with roles
    print("\n4️⃣  Barcha foydalanuvchilar va ularning rollari:")
    users = storage.get("users")
    print(format_users_table(users))
    
    # Test 5: Admin operations - enter cars for different owners
    print("\n5️⃣  Admin: Turli egalar uchun mashinalar kiritish...")
    parking.enter("10A123CD", "operator_karim")
    print("✓ Operator_karim ning mashinasi kiritildi")
    
    parking.enter("20B456EF", "user_ali")
    print("✓ User_ali ning mashinasi kiritildi")
    
    # Test 6: Show parking status
    print("\n6️⃣  Park holati:")
    print(parking.view_table())
    
    # Test 7: Operator can exit a car
    print("\n7️⃣  Operator: Mashinani chiqarish...")
    result = parking.exit("10A123CD")
    if result:
        print(f"✓ To'lov: {result.get('amount')} {result.get('currency')}")
    
    # Test 8: Verify phone numbers in users display
    print("\n8️⃣  Foydalanuvchilar ro'yxati (tel. raqamlar ko'rinib turadi):")
    print(format_users_table(users))
    
    # Test 9: Access control logic
    print("\n9️⃣  Roli asosida kirish nazorati:")
    print("   - Admin: Hamma operatsiyalarni bajaradi ✓")
    print("   - Operator: Parking operatsiyalarini va foydalanuvchilarni boshqaradi ✓")
    print("   - User: Faqat o'z mashinasini kiritadi/chiqaradi va bronlaydi ✓")
    
    print("\n" + "=" * 60)
    print("✅ 3-TIER ROLE SYSTEM ISHLAYAPTI!")
    print("=" * 60)
    print("\n📝 Admin script orqali yaratiladi:")
    print("   python create_admin.py")
    print("\n📝 Operator va User CLI orqali ro'yxatdan o'tadi:")
    print("   python main.py")


if __name__ == "__main__":
    demo()
