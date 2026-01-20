from parking.core.parking import Parking
from parking.storage import JSONStorage
from parking.core.utils import format_notifications_table, format_users_table, format_menu
from user.service import AuthService


def run():
    storage = JSONStorage("data.json")
    auth = AuthService(storage)
    parking = Parking(storage)

    print("\n=== Parking tizimi - Konsol ===")
    main_menu = [
        ("1", "Ro'yxatdan o'tish"),
        ("2", "Kirish"),
        ("3", "Park holatini ko'rish (umumiy)"),
        ("4", "Dasturdan chiqish")
    ]

    while True:
        print("\n" + format_menu(main_menu))
        choice = input("Tanlang: ").strip()

        if choice == "1":
            # Ro'yxatdan o'tish
            username = input("Foydalanuvchi nomi: ").strip()
            password = input("Parol: ")
            
            # Faqat Operator yoki User rol tanlang
            role_choice = input("Rol tanlang (1=Operator, 2=User) [2]: ").strip()
            role = "operator" if role_choice == "1" else "user"
            
            # Telefon raqami kiritish
            while True:
                phone = input("Telefon nomeringiz (+998 ** *** ** **): ").strip()
                if auth.phone_valid(phone):
                    if auth.royxatdan_otish(username, password, phone, role=role):
                        print(f"✓ Ro'yxatdan o'tdingiz (Rol: {role})")
                    else:
                        print("✗ Ro'yxatdan o'tishda xatolik (foydalanuvchi mavjud?)")
                    break
                else:
                    print("✗ Telefon noto'g'ri. Format: +998 ** *** ** ** (masalan: +998 93 123 45 67)")

        elif choice == "2":
            # Login
            username = input("Foydalanuvchi nomi: ").strip()
            password = input("Parol: ")
            
            if auth.login(username, password):
                print("✓ Kirish muvaffaqiyatli")
                
                # Foydalanuvchining rolini olish
                users = storage.get("users")
                current_user = next((u for u in users if u.get("username") == username), {})
                role = current_user.get("role", "user")
                
                # Rolga qarab menyuni ko'rsatish
                _show_role_menu(role, username, parking, storage)
            else:
                print("✗ Login yoki parol noto'g'ri")

        elif choice == "3":
            # Umumiy park holati (login qilmasdan)
            print(parking.view_table())

        elif choice == "4":
            print("\nDastur tugadi.")
            break

        else:
            print("✗ Noto'g'ri tanlov")


def _show_role_menu(role, username, parking, storage):
    """Rolga qarab menyu ko'rsatish"""
    
    if role == "admin":
        _admin_menu(username, parking, storage)
    elif role == "operator":
        _operator_menu(username, parking, storage)
    else:  # user
        _user_menu(username, parking, storage)


def _admin_menu(username, parking, storage):
    """Admin menyu: hamma narsani boshqaradi"""
    admin_menu = [
        ("1", "Mashina kiritish (boshqa foydalanuvchi uchun)"),
        ("2", "Mashina chiqarish"),
        ("3", "Park holatini ko'rish"),
        ("4", "Barcha foydalanuvchilar ro'yxati"),
        ("5", "Ogohlantirishlar"),
        ("6", "Logout")
    ]
    
    while True:
        print("\n[ADMIN MENYU]")
        print(format_menu(admin_menu))
        choice = input("Tanlang: ").strip()
        
        if choice == "1":
            # Mashina kiritish
            while True:
                reg = input("Avtomobil raqami (masalan: 10C234BD): ").strip()
                if parking.plate_valid(reg):
                    owner = input("Egasi (foydalanuvchi nomi): ").strip()
                    if parking.enter(reg, owner):
                        print("✓ Mashina kiritildi")
                    else:
                        print("✗ Bo'sh slot yo'q")
                    break
                else:
                    print("✗ Noto'g'ri raqam")
        
        elif choice == "2":
            # Mashina chiqarish
            reg = input("Avtomobil raqami: ").strip()
            result = parking.exit(reg)
            if result:
                print(f"✓ To'lov: {result.get('amount')} {result.get('currency')}")
            else:
                print("✗ Bunday mashina topilmadi")
        
        elif choice == "3":
            print(parking.view_table())
        
        elif choice == "4":
            users = storage.get("users")
            print(format_users_table(users))
        
        elif choice == "5":
            notes = storage.get("notifications")
            if not notes:
                print("Ogohlantirish yo'q")
            else:
                print(format_notifications_table(notes))
        
        elif choice == "6":
            break
        
        else:
            print("✗ Noto'g'ri tanlov")


def _operator_menu(username, parking, storage):
    """Operator menyu: parkovkani va foydalanuvchilarni nazorat qiladi"""
    operator_menu = [
        ("1", "Mashina kiritish"),
        ("2", "Mashina chiqarish"),
        ("3", "Park holatini ko'rish"),
        ("4", "Barcha foydalanuvchilar"),
        ("5", "Ogohlantirishlar"),
        ("6", "Logout")
    ]
    
    while True:
        print("\n[OPERATOR MENYU]")
        print(format_menu(operator_menu))
        choice = input("Tanlang: ").strip()
        
        if choice == "1":
            # Mashina kiritish
            while True:
                reg = input("Avtomobil raqami: ").strip()
                if parking.plate_valid(reg):
                    owner = input("Egasi (foydalanuvchi nomi): ").strip()
                    if parking.enter(reg, owner):
                        print("✓ Mashina kiritildi")
                    else:
                        print("✗ Bo'sh slot yo'q")
                    break
                else:
                    print("✗ Noto'g'ri raqam")
        
        elif choice == "2":
            # Mashina chiqarish
            reg = input("Avtomobil raqami: ").strip()
            result = parking.exit(reg)
            if result:
                print(f"✓ To'lov: {result.get('amount')} {result.get('currency')}")
            else:
                print("✗ Bunday mashina topilmadi")
        
        elif choice == "3":
            print(parking.view_table())
        
        elif choice == "4":
            users = storage.get("users")
            print(format_users_table(users))
        
        elif choice == "5":
            notes = storage.get("notifications")
            if not notes:
                print("Ogohlantirish yo'q")
            else:
                print(format_notifications_table(notes))
        
        elif choice == "6":
            break
        
        else:
            print("✗ Noto'g'ri tanlov")


def _user_menu(username, parking, storage):
    """Foydalanuvchi menyu: faqat o'z mashinasini kiritadi/chiqaradi"""
    user_menu = [
        ("1", "O'z mashinamni kiritish"),
        ("2", "O'z mashinamni chiqarish"),
        ("3", "Park holatini ko'rish"),
        ("4", "Slot bron qilish"),
        ("5", "Bronni bekor qilish"),
        ("6", "Mening ogohlantirishlarim"),
        ("7", "Logout")
    ]
    
    while True:
        print("\n[FOYDALANUVCHI MENYU]")
        print(format_menu(user_menu))
        choice = input("Tanlang: ").strip()
        
        if choice == "1":
            # O'z mashinasini kiritish
            while True:
                reg = input("Avtomobil raqami: ").strip()
                if parking.plate_valid(reg):
                    if parking.enter(reg, username):
                        print("✓ Mashinangiz kiritildi")
                    else:
                        print("✗ Bo'sh slot yo'q")
                    break
                else:
                    print("✗ Noto'g'ri raqam")
        
        elif choice == "2":
            # O'z mashinasini chiqarish
            reg = input("Avtomobil raqami: ").strip()
            result = parking.exit(reg)
            if result:
                print(f"✓ To'lov: {result.get('amount')} {result.get('currency')}")
            else:
                print("✗ Bunday mashina topilmadi")
        
        elif choice == "3":
            print(parking.view_table())
        
        elif choice == "4":
            # Bron qilish
            slot_str = input("Slot raqami (bo'sh = avtomatik): ").strip()
            slot = int(slot_str) if slot_str.isdigit() else None
            res = parking.reserve(username, slot)
            if res:
                print(f"✓ Bron tasdiqlandi — slot {res.get('slot')}")
            else:
                print("✗ Bron qilishning iloji yo'q")
        
        elif choice == "5":
            # Bronni bekor qilish
            slot_str = input("Slot raqami (bo'sh = hammasini bekor): ").strip()
            slot = int(slot_str) if slot_str.isdigit() else None
            if parking.cancel_reservation(username, slot):
                print("✓ Bron bekor qilindi")
            else:
                print("✗ Bron topilmadi")
        
        elif choice == "6":
            notes = storage.get("notifications")
            my_notes = [n for n in notes if n.get("username") == username]
            if not my_notes:
                print("Ogohlantirish yo'q")
            else:
                print(format_notifications_table(my_notes))
        
        elif choice == "7":
            break
        
        else:
            print("✗ Noto'g'ri tanlov")


if __name__ == "__main__":
    run()
