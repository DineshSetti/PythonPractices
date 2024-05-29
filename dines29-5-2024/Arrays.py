import copy
from array import *
arr1=array('i',[10,20,30,40,50])
for i in range (len(arr1)):
    print(arr1[i])



from array import *
arr2=array('i',[100,200,300,400,500])
arr2.pop(0)
print(arr2)



from array import *
arr2=array('i',[100,200,300,400,500])
arr2.remove(500)
print(arr2)



from array import *
arr2=array('i',[100,200,300,400,500])
arr2.reverse()
print(arr2)




from array import *
arr2=array('i',[100,200,300,400,500])
arr3=array(arr2.typecode,(i for i in arr2))
for x in arr3:
    print(x)



from array import *
arr5=array('u',['a','b','c','d'])
print(arr5)
arr6=array(arr5.typecode,(y for y in arr5))
arr6.remove('b')
for i in arr6:
    print(i)




from array import *
arr8=array('i',[1,2,3,4,5])
arr9=arr8
print(arr8,arr9)



from array import *
arr10=array('i',[1,2,3,4,5])
arr11=copy.deepcopy(arr10)
arr11.remove(4)
print(arr10,arr11)



from array import *
arr=array('i',[1,2,3,4,5])
b=arr.index(4)
print(b)



from array import *
arr=array('i',[1,2,3,4,5])
b=arr.count(4)
print(b)