class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Rahul", 20)
student2 = Student("Aman", 22)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)

class Car:

    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model 3", 2024)


print(car1.brand, car1.model, car1.year)
print(car2.brand, car2.model, car2.year)