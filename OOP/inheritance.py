class Animal:

    def eat(self):
        print("Eating.....")

    def sleep(self):
        print("Sleeping.....")


class Dog(Animal):

    def bark(self):
        print("Barking.....")

class Cat(Animal):

    def meow(self):
        print("Meow....")

dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()