class Mobiles:
    def phone(self):
        print("this is oppo ")
class Brand(Mobiles):
    def phone(self):
        print("this is apple")

obj=Brand()
obj.phone()

   #to Over-raid these use super() now see



   
class Mobiles:
    def phone(self):
        print("this is oppo ")
class Brand(Mobiles):
    def phone(self):
        print("this is apple")
        super().phone()

obj=Brand()
obj.phone()