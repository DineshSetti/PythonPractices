for i in range(30,0,-3):
    if i%3==0:
        print(i)
    else:
        print("not found")


for i in range(30,0,-3):
    if i%3==5:
        print(i)
    else:
        print("not found")

a=20
b=10
if a>=b:
    print("a is greater than b")
elif a<=b:
    print("a is less tha b")
else:
    print("not found")


a=10
b=50
if a>=b:
    print("a is greater than b")
elif a<=b:
    print("a is less than b")
else:
    print("not found")

marks=45
if marks >18:
    print("you are passed")
elif marks>35:
    print("first class")
else:
    print("you are failed")


marks=int(input("enter your marks : "))
if marks >18:
    print("you are passed")
elif marks>35:
    print("first class")
else:
    print("you are failed")