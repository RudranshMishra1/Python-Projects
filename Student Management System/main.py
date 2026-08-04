students = []

class Student:

    def __init__(self,name,age,rollNo,course):
        self.name = name
        self.age = age
        self.rollNo = rollNo
        self.course = course

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"RollNo: {self.rollNo}")
        print(f"Course: {self.course}")
        print("-" * 25)

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday! {self.name} is now {self.age} years old.")

    def coursee(self,newCourse):
        self.course = newCourse
        print(f"{self.name}'s course has been changed to {self.course}")

while True:
    print("\n===== STUDENT MANAGEMENT =====\n")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Birthday")
    print("5. Change Course")
    print("6. Delete Student")
    print("7. Exit")

    user = input("Choose an option: ")

    if user == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        roll_no = input("Enter Roll no.: ")
        course = input("Enter Course: ")
        student = Student(name,age,roll_no,course)
        students.append(student)

        print("Student added Successfully ✅")

    elif user == "2":
        if not students:
            print("No students found.")
        else:
            for student in students:
                "\n"
                student.introduce()

    elif user == "3":
        roll = input("Enter the roll number: ")
        found = False
        for student in students:
            if student.rollNo == roll:
                student.introduce()
                found = True
                break

        if not found:
            print("Student not found")

    elif user == "4":
        roll = input("Enter the roll number: ")

        for student in students:
            if student.rollNo == roll:
                student.birthday()
                break
        else:
            print("Student not found")

    elif user == "5":
        roll = input("Enter the roll number: ")
        newCourse = input("Enter new course: ")

        for student in students:
            if student.rollNo == roll:
                student.coursee(newCourse)
                break
        else:
            print("Student not found")

    elif user == "6":
        roll = input("Enter the roll number: ")

        for student in students:
            if student.rollNo == roll:
                students.remove(student)
                print("Student deleted successfully.")
                break
        else:
            print("Student not found")

    elif user == "7":
        print("Thank you for using Student Management System.")
        break
    else:
        print("Please choose a valid option (1-7)")