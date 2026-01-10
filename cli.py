from parking.core.parking import Parking
from parking.storage import JSONStorage
from user.service import AuthService


def run():
    storage = JSONStorage("data.json")
    auth = AuthService(storage)
    parking = Parking(storage)

    print("Parking tizimi - Konsol")
    while True:
        print("\n1) Ro'yxatdan o'tish  2) Kirish  3) Park holati  4) Dasturdan chiqish")
        choice = input("Tanlang: ")
        if choice == "1":
            u = input("Foydalanuvchi nomi: ")
            p = input("Parol: ")
            # role tanlash: default user, mumkin admin ham kiritish
            role_in = input("Role (user/admin) [user]: ").strip().lower()
            role = role_in if role_in in ("admin", "user") else "user"
            # Email to'g'ri kiritilmaguncha so'raymiz
            while True:
                e = input("Email: ")
                if auth.email_valid(e):
                    ok = auth.royxatdan_otish(u, p, e, role=role)
                    if ok:
                        print("Ro'yxatdan o'tildi.")
                    else:
                        print("Ro'yxatdan o'tishda xatolik (foydalanuvchi mavjud yoki boshqa muammo).")
                    break
                else:
                    print("Email noto'g'ri. Iltimos qayta kiriting.")
                    try:
                        storage.append("notifications", {"username": u, "message": "Email noto'g'ri kiritildi", "time": auth._now()})
                    except Exception:
                        pass
        elif choice == "2":
            u = input("Foydalanuvchi nomi: ")
            p = input("Parol: ")
            if auth.login(u, p):
                print("Kirish muvaffaqiyatli.")
                # aniqlaymiz foydalanuvchi roli (admin yoki oddiy)
                users = storage.get("users")
                current_user = next((x for x in users if x.get("username") == u), {})
                role = current_user.get("role", "user")
                # user menu
                while True:
                    if role == "admin":
                        print("\n[Admin] 1) Mashina kiritish  2) Mashina chiqarish  3) Park holati  4) Ogohlantirishlar  5) Foydalanuvchilar  6) Logout")
                    else:
                        # Regular user: limited menu (view + reservation)
                        print("\n1) Park holati  2) Bron qilish  3) Bronni bekor qilish  4) Ogohlantirishlar  5) Logout")
                    c = input("Tanlang: ")
                    if role != "admin" and c == "1":
                        print(parking.view_table())
                    elif role != "admin" and c == "2":
                        slot_in = input("Slot raqamini kiriting (bo'sh qoldiring — avtomatik tanlanadi): ")
                        slot = int(slot_in) if slot_in.strip().isdigit() else None
                        res = parking.reserve(u, slot)
                        if res:
                            print(f"Bron tasdiqlandi — slot {res.get('slot')}")
                        else:
                            print("Bron qilishning iloji yo'q.")
                    elif role != "admin" and c == "3":
                        slot_in = input("Agar ma'lum slot bekor qilinishi kerak bo'lsa raqamini kiriting (bo'sh = hammasini bekor qiladi): ")
                        slot = int(slot_in) if slot_in.strip().isdigit() else None
                        ok = parking.cancel_reservation(u, slot)
                        print("Bron bekor qilindi." if ok else "Bron topilmadi.")
                    elif role != "admin" and c == "4":
                        notes = storage.get("notifications")
                        my_notes = [n for n in notes if n.get("username") == u]
                        if not my_notes:
                            print("Ogohlantirish yo'q.")
                        else:
                            for n in my_notes:
                                print(f"{n.get('time')}: {n.get('message')}")
                    elif role != "admin" and c == "5":
                        break
                    elif c == "1":
                        # so'rovni takroriy tekshirish: noto'g'ri raqam qabul qilinmasin
                        while True:
                            reg = input("Avtomobil raqami: ")
                            if parking.plate_valid(reg):
                                owner = u
                                if role == "admin":
                                    o2 = input("Egasini kiriting (bo'sh = siz): ")
                                    if o2.strip():
                                        owner = o2.strip()
                                ok = parking.enter(reg, owner)
                                if ok:
                                    print("Mashina kiritildi.")
                                else:
                                    print("Joy yo'q.")
                                break
                            else:
                                print("Avtomobil raqami noto'g'ri formatda. Iltimos qayta kiriting (masalan: 10C234BD).")
                    elif c == "2":
                        reg = input("Avtomobil raqami: ")
                        if role == "admin":
                            o2 = input("Agar kerak bo'lsa egasini kiriting (bo'sh = nomalum): ")
                            if o2.strip():
                                pass
                        res = parking.exit(reg)
                        if res:
                            amt = res.get("amount")
                            cur = res.get("currency", "UZS")
                            print(f"To'lov: {amt} {cur}")
                        else:
                            print("Bunday mashina topilmadi.")
                    elif c == "3":
                        print(parking.view_table())
                    elif c == "4":
                        notes = storage.get("notifications")
                        my_notes = [n for n in notes if n.get("username") == u]
                        if not my_notes:
                            print("Ogohlantirish yo'q.")
                        else:
                            for n in my_notes:
                                print(f"{n.get('time')}: {n.get('message')}")
                    elif c == "5" and role == "admin":
                        # show users for admin
                        users = storage.get("users")
                        for uu in users:
                            print(f"{uu.get('username')} - {uu.get('email')} - role={uu.get('role')}")
                    elif c == "5" and role != "admin":
                        break
                    elif c == "6" and role == "admin":
                        break
                    elif c == "5":
                        break
                    else:
                        print("Noto'g'ri tanlov.")
            else:
                print("Login yoki parol noto'g'ri.")
        elif choice == "3":
            print(parking.view_table())
        elif choice == "4":
            print("Dastur tugadi.")
            break
        else:
            print("Noto'g'ri tanlov.")


if __name__ == "__main__":
    run()
