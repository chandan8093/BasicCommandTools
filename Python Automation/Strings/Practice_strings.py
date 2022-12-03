import os
tw=os.get_terminal_size().columns
my_str=input("Enter A string : ")
#just is to adjust your string to left or right side 
print("cenetr",my_str.center(tw).title())
print(f"{my_str.ljust(122)}\n {my_str.rjust(122)}")