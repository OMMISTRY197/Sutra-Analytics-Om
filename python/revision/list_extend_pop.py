# This program demonstrates the pop() method for removing an element by index 
# and the extend() method for extending a list with another list.

list1 = [11,12,13,14]
list2 = [15,16,17,18]

list1.extend(list2)
print(list1)

list3 = [11,12,13,14]
list3.pop(0)
print(list3)