a=(lambda x,y : x+y) (1,2)
print(a)


b=(lambda x,y : x*y) (1,2)
print(b)

c=(lambda x,y :x if x>y else y) (20,10)
print(c)

c=(lambda x,y :x if x>y else y) (20,50)
print(c)

c=(lambda x :"even number" if x%2==0 else "odd number") (20)
print(c)

c=(lambda x :"even number" if x%2==0 else "odd number") (25)
print(c)

