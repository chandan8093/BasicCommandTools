'''
user_string=input("Enter a string ")
action_on_strings=input("Enter your action on your strings (valid action are : upper|lower|title)")

if  action_on_strings=="lower":
    print(user_string.lower())
elif action_on_strings=="upper":
    print(user_string.upper())
elif action_on_strings=="title":
    print(user_string.title())
else:
    print("Inavlid action")

'''


#To use a command line argument(sys.argv) follow below steps
import sys

if len(sys.argv)!=3:
    print(f"Valid Action Requied\n choose argument as  : <your string> < title|lower|upper>")
    sys.exit()
user_string=sys.argv[1]
action_on_strings=sys.argv[2]
print(sys.argv)
if  action_on_strings=="lower":
    print(user_string.lower())
elif action_on_strings=="upper":
    print(user_string.upper())
elif action_on_strings=="title":
    print(user_string.title())
else:
    print("Inavlid action")


