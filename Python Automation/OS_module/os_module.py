#os.sep(separator)

import os 
print(os.sep)
print(os.getcwd()) #current working directory
print(os.listdir())
#print(f'new file added in current directory : [basic.md] {os.mkdir("basic1.md")}')
print(os.rmdir(""))
#print(os.environ)
'''
print(os.getuid())
print(os.getpid())
print(os.getgid())

'''

#os.path
#os.system
x=input("enter a valid windwos command")
ex=os.system(x)
if ex==0:
    print("command executed successfully")
else:
    print("command us")