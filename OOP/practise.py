class Vehicle:

    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):

    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model

    def start(self):
        print("Car Started")


car = Car("Tesla", "Model 3")
car.start()
print(car.brand, car.model)