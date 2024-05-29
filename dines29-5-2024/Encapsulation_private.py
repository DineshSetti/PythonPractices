class A:
    def __init__(self,a,b):
        self.__a=a
        self.__b=b
    def hello(self):
        print(self.__a)
        print(self.__b)
obj=A(10,20)
obj.hello()