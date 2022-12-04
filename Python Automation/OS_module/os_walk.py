'''
import os
path="C:\\Users\\Admin\\Desktop\\CloudTrail"
print("------------------------------")
for i in list(os.walk(path)):
    y = list(i)
    for x in range(0,len(i), +1):
        print(y[x])

'''
'''
import os
s_str=input("Enter a file that needs to be searched : ")
path="c:\\"
for r,d,f in os.walk(path):
    for j in f:
        if j==s_str:
            print(os.path.join(r,j))

'''

#captaring drive name 
import string 
import os
pd_name=string.ascii_letters
for i in pd_name:
    if os.path.exists(i+":\\"):
        print(i)

    