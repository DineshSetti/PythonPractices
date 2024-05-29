class Student:
    def setName(self,name):
        self.name=name
    def setAge(self,Age):
        self.Age=Age
    def getName(self):
        return self.name
    def getAge(self):
        return self.Age
obj=Student()
obj.setName("Dinesh")
obj.setAge(22)
print(obj.getName())
print(obj.getAge())



class employee:
    def __init__(self):
        self.name="mmm"
        self.age=77
    def setName(self,name,age):
        self.name=name
        self.age =age

    def getName(self):
        return self.name,self.age


obj=employee()
obj.setName("hii",88)
print(obj.getName())



