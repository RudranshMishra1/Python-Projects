class Animal:

    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")

class Dog(Animal):

    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
        

dog = Dog("Bruno", "Golden Retriever")
dog.introduce()
print(dog.breed)