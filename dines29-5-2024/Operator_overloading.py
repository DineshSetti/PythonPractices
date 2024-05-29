
class one:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return ((self.a+other.a)+(self.b+other.b))
obj1=one(1,2)
obj2=one(3,4)
print(obj1+obj2)
