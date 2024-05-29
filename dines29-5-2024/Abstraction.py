from abc import ABC,abstractmethod

class vehicle:
    @abstractmethod
    def tyres(self):
        pass
class bike(vehicle):
    def tyres(self):
        print("2 tyres")
class car(vehicle):
    def tyres(self):
        print("4 tyres")

class lorry(vehicle):
    def tyres(self):
        print("14 tyres")

obj=bike()
obj1=car()
obj2=lorry()

obj.tyres()
obj1.tyres()
obj2.tyres()
