def sum(addmethod):
    def inner(x,y):
        if (x%2==0 and y%2==0):
            addmethod(x,y)
        else:
            print("enter even numbers")
    return inner
@sum
def add(a,b):
    print(a+b)
add(2,4)