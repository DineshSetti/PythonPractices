class Mobile:
    def sim(self):
        print("jio")
class Camera(Mobile):
    def camera(self):
        print("48mp")
class Ram(Mobile):
    def ram(self):
        print("8gb")
obj=Camera()
obj.camera()
obj.sim()
obj2=Ram()
obj2.ram()
obj.sim()