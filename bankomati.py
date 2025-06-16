# ეს პროგრამა არის მარტივი ბანკომატის სიმულაცია
# მომხმარებელს შეუძლია: რეგისტრაცია, შესვლა, ბალანსის ნახვა, თანხის შეტანა და გატანა

# ვიბრუნებთ ფაილების გამოყენებას მომხმარებლის მონაცემების შესანახად
import os

# ფაილი სადაც ყველა მომხმარებლის ინფორმაცია შეინახება
USER_FILE = "users.txt"


# მომხმარებლის რეგისტრაციის ფუნქცია
def register():
    print("\n--- რეგისტრაცია ---")
    username = input("შეიყვანეთ ახალი მომხმარებლის სახელი: ").strip()
    password = input("შეიყვანეთ პაროლი: ").strip()

    # ვამოწმებთ უკვე არსებობს თუ არა ეს სახელი
    if user_exists(username):
        print("ესეთი მომხმარებელი უკვე არსებობს. სცადეთ სხვა სახელი.")
        return

    # თუ მომხმარებელი ახალია ვქმნით ჩანაწერს და ვწერთ ფაილში (საწყისი ბალანსით 0)
    with open(USER_FILE, "a") as f:
        f.write(f"{username},{password},0\n")

    print("რეგისტრაცია წარმატებით დასრულდა!")


# შესვლის ფუნქცია
def login():
    print("\n--- მომხმარებლის შესვლა ---")
    username = input("შეიყვანეთ მომხმარებლის სახელი: ").strip()
    password = input("შეიყვანეთ პაროლი: ").strip()

    # ვკითხულობთ ფაილს და ვამოწმებთ არსებობს თუ არა ეს მომხმარებელი და პაროლი სწორია თუ არა
    with open(USER_FILE, "r") as f:
        for line in f:
            saved_username, saved_password, balance = line.strip().split(",")
            if username == saved_username and password == saved_password:
                print("წარმატებით შეხვედით სისტემაში!")
                return username  # ვაბრუნებთ მომხმარებლის სახელს

    print(" არასწორი მომხმარებლის სახელი ან პაროლი.")
    return None  # თუ არ დაემთხვა ვაბრუნებთ None-ს


# ფუნქცია ამოწმებს არსებობს თუ არა მომხმარებელი

def user_exists(username):
    # თუ ფაილი არ არსებობს ჯერ, მაშინ არავინ არ არის დარეგისტრირებული
    if not os.path.exists(USER_FILE):
        return False

    with open(USER_FILE, "r") as f:
        for line in f:
            saved_username = line.strip().split(",")[0]
            if saved_username == username:
                return True

    return False

# ფუნქცია აბრუნებს მომხმარებლის ბალანსს
def get_balance(username):
    with open(USER_FILE, "r") as f:
        for line in f:
            saved_username, _, balance = line.strip().split(",")
            if saved_username == username:
                return float(balance)
    return 0.0


# ფუნქცია ანახლებს მომხმარებლის ბალანსს
def update_balance(username, new_balance):
    lines = []

    # ვკითხულობთ ყველა ხაზს და ვცვლით მხოლოდ იმ მომხმარებლის ბალანსს, ვისაც ვეძებთ
    with open(USER_FILE, "r") as f:
        for line in f:
            saved_username, password, balance = line.strip().split(",")
            if saved_username == username:
                lines.append(f"{username},{password},{new_balance}\n")
            else:
                lines.append(line)

    # ვწერთ ყველა სტრიქონს თავიდან ფაილში
    with open(USER_FILE, "w") as f:
        f.writelines(lines)


# თანხის შეტანის ფუნქცია
def deposit(username):
    print("\n--- თანხის შეტანა ---")
    amount = input("შეიყვანეთ თანხა შესატანად: ")

    if not amount.isdigit():
        print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი.")
        return

    amount = float(amount)
    balance = get_balance(username)
    balance += amount

    update_balance(username, balance)
    print(f"თანხა წარმატებით შეიტანეთ! თქვენი ახალი ბალანსია: {balance} ლარი")


# თანხის გატანის ფუნქცია
def withdraw(username):
    print("\n--- თანხის გატანა ---")
    amount = input("შეიყვანეთ თანხა გასატანად: ")

    if not amount.isdigit():
        print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი.")
        return

    amount = float(amount)
    balance = get_balance(username)

    if amount > balance:
        print("თქვენ არ გაქვთ საკმარისი თანხა ანგარიშზე.")
        return

    balance -= amount
    update_balance(username, balance)
    print(f"თანხა გატანილია. თქვენი ახალი ბალანსია: {balance} ლარი")


# მომხმარებლის მენიუ შესვლის შემდეგ
def user_menu(username):
    while True:
        print(f"\nმოგესალმებით, {username}!")
        print("1. ბალანსის ნახვა")
        print("2. თანხის შეტანა")
        print("3. თანხის გატანა")
        print("4. გამოსვლა")

        choice = input("აირჩიეთ მოქმედება (1-4): ")

        if choice == "1":
            balance = get_balance(username)
            print(f"თქვენი ბალანსია: {balance} ლარი")
        elif choice == "2":
            deposit(username)
        elif choice == "3":
            withdraw(username)
        elif choice == "4":
            print("გამოსვლა ანგარიშიდან...")
            break
        else:
            print("არასწორი არჩევანი. სცადეთ თავიდან.")


# მთავარი მენიუ — პროგრამის საწყისი ნაწილი
def main_menu():
    while True:
        print("\n=====================")
        print("ბანკომატის მენიუ")
        print("=====================")
        print("1. რეგისტრაცია")
        print("2. შესვლა")
        print("3. პროგრამიდან გამოსვლა")

        choice = input("აირჩიეთ მოქმედება (1-3): ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                user_menu(user)
        elif choice == "3":
            print("ნახვამდის!")
            break
        else:
            print("არასწორი არჩევანი. სცადეთ თავიდან.")


# აქედან იწყება პროგრამის გაშვება
if __name__ == "__main__":
    main_menu()
