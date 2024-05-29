class Mobile:
    def sim(self):
        print("jio")
class Camera:
    def camera(self):
        print("48mp")
class Ram(Mobile,Camera):
    def ram(self):
        print("8gb")
obj=Ram()
obj.sim()
obj.camera()
obj.ram()