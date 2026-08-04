class Student:

    school = "ABC Public School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def birthday(self):
        self.age += 1

    def change_name(self,new_name):
        self.name = new_name


student1 = Student("Rahul", 20)
student1.birthday()

student1.change_name("Rohan")
student1.introduce()
Student.school = "XYZ Public School"
print("School:",student1.school)