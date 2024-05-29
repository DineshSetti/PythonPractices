class school:
    def Firstclass(self):
        print("strength is 10 members")

    def Secondclass(self):
        print("strength is 20 members")
class college(school):
    def Firstyear(self):
        print("strength is 30 members")

    def Secondyear(self):
        print("strength is 40 members")
class btech(college):
    def thirdyear(self):
        print("strength is 50 members")

    def finalyear(self):
        print("strength is 60 members")
obj=btech()
obj.Firstclass()
obj.Secondclass()
obj.Firstyear()
obj.Secondyear()
obj.thirdyear()
obj.finalyear()