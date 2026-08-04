class Animal:

    def sound(self):
        print("Some animal sound")

class Dog(Animal):

    def sound(self):
        print("Woof! Woof!")

class Cat(Animal):

    def sound(self):
        print("Meow!")


dog = Dog()
dog.sound()

cat = Cat()
cat.sound()