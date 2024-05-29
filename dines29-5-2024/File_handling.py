import os

s=open('File_handling.txt',mode='r')
print(s.read())
s.close()



#
# a=open('File_handling.txt',mode='w')
# print(a.write("python practice  "))
# s.close()



# b=open('File_handling.txt',mode='a')
# print(b.write("in pycharm"))
# s.close()



f=open('File_handling.txt',mode='w')
print(f.write("python practice in laptop "))
f.close()



b=open('File_handling.txt',mode='a')
print(b.write("in pycharm"))
b.close()



b=open('File_handling.txt',mode='r')
print(b.readline())
print(b.readline())
print(b.readline())
b.close()


import os
#k=open('Abc.txt',mode='r')
#k.close()
#os.rename('Abc.txt','BBA.txt')

#import os
#l=open('File_handling.txt3',mode='r')
#l.close()
#os.remove('File_handling.txt3')

#import os
#m=open('FH','w')
#m.close()
#os.rename('FH','File_Handling5.txt')

import os
n=open('File_Handling5.txt',mode='r')
n.close()
os.remove('File_Handling5.txt')

