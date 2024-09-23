from abc import ABC , abstractmethod
class Vehicle:
    def __init__(self,fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
    @abstractmethod
    def drive(self):
        pass
    @abstractmethod
    def refuel(self):
        pass

class Car(Vehicle):
    def drive(self,distance):
        self.distance = distance
        if self.distance * self.fuel_consumption > self.fuel_quantity:
            return f'khong du nhien lieu de di het {self.distance}'
        else:
            self.fuel_quantity = self.fuel_quantity - self.distance*(self.fuel_consumption + 0.9)
            return self.fuel_quantity
    def refuel(self,refuels):
        self.refuels = refuels
        self.fuel_quantity = self.fuel_quantity + self.refuels
        return self.fuel_quantity

class Truck(Vehicle):
    def drive(self,distance):
        self.distance = distance
        if self.distance * self.fuel_consumption > self.fuel_quantity*0.95:
            return f'khong du nhien lieu de di het {self.distance}'
        else:
            self.fuel_quantity = self.fuel_quantity - self.distance*(self.fuel_consumption + 1.6)
            return self.fuel_quantity
    def refuel(self,refuels):
        self.refuels = refuels
        self.fuel_quantity = self.fuel_quantity + self.refuels*0.95
        return self.fuel_quantity
        

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)