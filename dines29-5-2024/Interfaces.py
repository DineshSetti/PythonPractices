from abc import ABC,abstractmethod
class vehicle(ABC):
     @abstractmethod
     def car(self):
         pass
     def Bike(self):
         pass
class Tata(vehicle):
    def car(self):
        print("this is tata car")
    def Bike(self):
        print("this is tata bike")
class Honda(vehicle):
    def car(self):
        print("this is honda car")
    def Bike(self):
        print("this is honda bike")

obj=Tata()
obj1=Honda()
obj.car()
obj.Bike()
obj1.car()
obj1.Bike()

