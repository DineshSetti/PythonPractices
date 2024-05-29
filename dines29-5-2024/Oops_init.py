class Mobile:
    def __init__(self,brand,camera,ram,rom,battery):
        self.brand=brand
        self.camera=camera
        self.ram=ram
        self.rom=rom
        self.battery=battery
    def specification(self):
        print(self.brand)
        print(self.camera)
        print(self.ram)
        print(self.rom)
        print(self.battery)
obj=Mobile("apple","48mp","8gb","128gb","5000mah")
obj.specification()
for i in range(3):
    obj2=Mobile("vivo","50mp","4gb","33gb","100mah")
    obj2.specification()


class Employe:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display (self):
        print(self.name)
        print(self.age)
obj=Employe("dinesh",25)
obj.display()
