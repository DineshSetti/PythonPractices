from array import *
#arr=array('i',[1,2,3,-4,-5,6,7])
#print(arr.buffer_info())
arr=array('i',[1,2,3,4,5,6,])
#print(arr[2])
arr.reverse()
print(arr[2])


from array import *
arr1=array('i',[10,20,30,40,50])
for i in range(5):
    print(arr1[i])



from array import *
arr2=array('u',['a','b','c','d'])
for x in range(len(arr2)):
    print(arr2[x])




from array import *
arr3=array('u',['x','y','z'])
for y in arr3:
    print(y)



from array import *
arr4=array('i',[100,200,300,400,500])
arr5=array(arr4.typecode,(a for a in arr4))
for z in arr5:
    print(z)



from array import *
arr=array('i',[800,400,900,200,100])
arr=array('i',sorted(arr))
print(arr)


from array import *
arr1=array('i',[800,400,900,200,100])
arr2=array('i',[10,40,90,20,10])
for i in arr2:
    arr1.append(i)
print(arr1)
arr1=array('i',sorted(arr1))
print(arr1)


from array import *
arr1=array('i',[800,400,900,200,100])
arr2=array('i',[10,40,90,20,10])
arr1.extend(arr2)
print(arr1)