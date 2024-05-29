class A:
    def __init__(self,a,b):
        self._a=a
        self._b=b
class B(A):
    def hello(self):
        print(self._a)
        print(self._b)
obj=B(10,20)
obj.hello()