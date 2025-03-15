class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"\nThis car is a {self.year} {self.make} {self.model}."

createdCar = Car("Toyota", "Corolla", 2020)

print(createdCar.description() + "\n")
