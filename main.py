from parking.storage import JSONStorage
from parking.auth import AuthService
from parking.parking import Parking


def run():
    storage = JSONStorage("data.json")
    auth = AuthService(storage)
    parking = Parking(storage)

    print("Parking tizimi - Konsol")
    while True:
        print("\n1) Register  2) Login  3) View parking  4) Exit program")
        choice = input("Tanlang: ")
        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")
            ok = auth.register(u, p)
            print("Ro'yxatdan o'tildi." if ok else "Foydalanuvchi mavjud.")
        elif choice == "2":
            u = input("Username: ")
            p = input("Password: ")
            if auth.login(u, p):
                print("Kirish muvaffaqiyatli.")
                # user menu
                while True:
                    print("\n1) Enter car 2) Exit car 3) View parking 4) Logout")
                    c = input("Tanlang: ")
                    if c == "1":
                        reg = input("Reg number: ")
                        ok = parking.enter(reg, u)
                        print("Mashina kiritildi." if ok else "Joy yo'q.")
                    elif c == "2":
                        reg = input("Reg number: ")
                        res = parking.exit(reg)
                        if res:
                            print(f"To'lov: {res['amount']}")
                        else:
                            print("Bunday mashina topilmadi.")
                    elif c == "3":
                        print(parking.view())
                    elif c == "4":
                        break
                    else:
                        print("Noto'g'ri tanlov.")
            else:
                print("Login yoki parol noto'g'ri.")
        elif choice == "3":
            print(parking.view())
        elif choice == "4":
            print("Dastur tugadi.")
            break
        else:
            print("Noto'g'ri tanlov.")


if __name__ == "__main__":
    run()
