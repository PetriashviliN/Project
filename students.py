# სტუდენტების მართვის სისტემა

# ეს კოდი იყენებს ობიექტურ პროგრამირებას ანუ ჩვენ ვქმნით "კლასებს" რაც ნიშნავს 
# რეალურ სამყაროს ობიექტების მოდელირებას (მაგ: სტუდენტი, პერსონა და ა.შ.)

#  Person — მშობელი კლასი
# ეს კლასი წარმოადგენს ზოგად პერსონას მას აქვს მხოლოდ ერთი თვისება — სახელი

class Person:
    def __init__(self, name):
        # self.name ნიშნავს რომ თითოეულ ობიექტს ექნება თავისი სახელი
        self.name = name

    # ეს მეთოდი გამოიყენება პერსონის შესახებ ინფორმაციის ჩვენებისთვის
    def display_info(self):
        print(f"სახელი: {self.name}")


#  Student — მემკვიდრეობს Person კლასს
# მემკვიდრეობა ნიშნავს რომ Student იღებს Person-ის თვისებებს (სახელი და display_info)
# დამატებით Student-ს თავისი უნიკალური თვისებები აქვს roll_number და grade

class Student(Person):
    def __init__(self, name, roll_number, grade):
        # super().__init__() ნიშნავს რომ ვიყენებთ მშობლის კონსტრუქტორს
        super().__init__(name)
        self.roll_number = roll_number
        self.grade = grade

    # პოლიმორფიზმი ვქმნით იგივე მეთოდს რაც მშობელს აქვს მაგრამ ჩვენი საკუთარი ვერსია
    def display_info(self):
        super().display_info()  # ჯერ ვაჩვენებთ სახელს (მშობლის მეთოდით)
        print(f"სიის ნომერი: {self.roll_number}")
        print(f"შეფასება: {self.grade}")
        print("-" * 30)


#  StudentManager  სტუდენტების სია და მართვა
# ამ კლასის საშუალებით შეგვიძლია სტუდენტების დამატება, ძებნა, შეფასების განახლება და სიის ჩვენება

class StudentManager:
    def __init__(self):
        # self.students არის სია სადაც ყველა სტუდენტის ობიექტი იქნება შენახული
        self.students = []

    def add_student(self, student):
        # სიის ბოლოს ვამატებთ სტუდენტს
        self.students.append(student)
        print("სტუდენტი წარმატებით დაემატა!")

    def show_all_students(self):
        if not self.students:
            print("ტუდენტების სია ცარიელია.")
        else:
            print("\n ყველა სტუდენტი:")
            for student in self.students:
                # აქ გამოვიყენებთ display_info მეთოდს — ეს არის პოლიმორფული გამოძახება
                student.display_info()

    def search_by_roll(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print("ნაპოვნი სტუდენტი:")
                print('\n')
                student.display_info()
                return
        print("ასეთი ნომრის მქონე სტუდენტი ვერ მოიძებნა.")

    def update_grade(self, roll_number, new_grade):
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                print('\n')
                print("შეფასება წარმატებით განახლდა!")
                return
        print("ასეთი ნომრის მქონე სტუდენტი ვერ მოიძებნა.")


#  დახმარების ფუნქციები (ვალიდაცია)

# ეს ფუნქცია ამოწმებს რომ რიცხვი შევიყვანოთ როგორც სიის ნომერი
def get_valid_roll_number():
    while True:
        roll_input = input("შეიყვანეთ სიის ნომერი (მხოლოდ რიცხვი): ")
        if roll_input.isdigit():
            return int(roll_input)
        else:
            print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი.")

# ეს ფუნქცია ამოწმებს რომ შეფასება იყოს სწორი — A-F
def get_valid_grade():
    while True:
        grade = input("შეიყვანეთ შეფასება (A-F): ").upper()
        if grade in ['A', 'B', 'C', 'D', 'E', 'F']:
            return grade
        else:
            print("გთხოვთ შეიყვანოთ სწორი შეფასება (A-F).")


#  მთავარი მენიუ
# ეს ფუნქცია მართავს მთელ პროგრამას რაც მთავარია ვაძლევთ მომხმარებელს არჩევანს სხვადასხვა მოქმედებაზე

def main():
    # ვქმნით StudentManager ობიექტს ამით ვმართავთ სტუდენტების სიას
    manager = StudentManager()

    while True:
        # მენიუ ვიზუალურად
        print("\n სტუდენტების მართვის მენიუ")
        print("1 ახალი სტუდენტის დამატება")
        print("2 ყველა სტუდენტის ნახვა")
        print("3 სტუდენტის ძებნა ნომრით")
        print("4 შეფასების განახლება")
        print("5 გასვლა")

        choice = input("აირჩიეთ მოქმედება (1-5): ")

        if choice == "1":
            name = input(" შეიყვანეთ სტუდენტის სახელი: ").strip()
            roll_number = get_valid_roll_number()
            grade = get_valid_grade()
            student = Student(name, roll_number, grade)
            manager.add_student(student)

        elif choice == "2":
            manager.show_all_students()

        elif choice == "3":
            roll_number = get_valid_roll_number()
            manager.search_by_roll(roll_number)

        elif choice == "4":
            roll_number = get_valid_roll_number()
            new_grade = get_valid_grade()
            manager.update_grade(roll_number, new_grade)

        elif choice == "5":
            print(" პროგრამა დასრულდა. ნახვამდის!")
            break

        else:
            print(" გთხოვთ აირჩიოთ სწორი ნომერი (1-5).")


#  პროგრამის გაშვება
# თუ ეს ფაილი პირდაპირ გავუშვით მაშინ main() დაიწყებს მუშაობას

if __name__ == "__main__":
    main()
