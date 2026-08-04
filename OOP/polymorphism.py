class Bird:

    def move(self):
        print("Flying")


class Fish:

    def move(self):
        print("Swimming")


animals = [Bird(), Fish()]

for animal in animals:
    animal.move()