list1=[1,2,5,"chandan",9.8]
print(list1[3])
print(list1[-2])
print(list1[-2][1])

print(f'{list1}')
list1[0]=23
print(f'{list1}')

#copy
my_list=list1
my_copy_list=list1.copy()

print(f'{id(my_list)}\n{id(list1)} \n{id(my_copy_list)}')


#append,insert 

print(f"-------------Append , Insert function -------")
x=[1,5,9,7,56,"k2cloud"]
x.append(89)
print(f"values after appending : {x}")
x.insert(-1,"gupta")
print(f"values after Inserting : {x}")


#extend vs append
print(f"\n\n\n<---------------Diff b/w Extend and Append >")
l1=[1,2,3,4]
l2=[5,6]
'''
l1.append(l2)
print(f"When you append list is : {l1}")
'''
l1.extend(l2)
print(f"When you extend list is : {l1}")


#POP(index) ,Remove(list values)
print(f"\n\n\n<---------------Diff b/w pop vs remove >")
l3=[1,2,3,4]
l4=[5,6,78]
no=eval(input("Input a number or string to remove from list : "))
l3.pop(1)
print(f"When you pop list is : {l3}")

l4.remove(no)
print(f"When you remove list is : {l4}")

#Sort,Reverse
print(f"<------------SORT / REVERSE Operation ---------------->")
t1=[76,19,78,890,723,868]
print(f"Before sorting : {t1}")
#t1.sort(reverse=True)
t1.reverse()
print(f"AFter sorting/revering : {t1}")
