   #Type_Function( -->
a=1
print(type(a))

b=1.23
print(type(b))

c= "Dinesh"
print(type(c))

D=True
print(type(D))


    #isinstance() Function -->
class Demo():
    pass
class Demo1():
    pass
obj=Demo()
print(type(obj))
print(isinstance(obj,Demo1))
print(isinstance(10,int))
print(issubclass(Demo,object))
print(issubclass(Demo1,object))
print(issubclass(str,object))

     #callable

class one:
    pass
class two:
    def __init__(self):
        self.names="dinesh"
    pass
x=two()
print(callable(two))

#getter & #setters

print(getattr(x,"names"))
