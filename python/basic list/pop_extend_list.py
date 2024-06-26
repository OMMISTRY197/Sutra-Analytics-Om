#This program demonstrates the pop() method for removing an element by index

list = [2, 3, 5, 7]
new_list = list.pop(2)
print('Removed Element:', new_list)
print('Updated List:', list)

#the extend() method for extending a list with another list.

l1 = [1,2,3,4,5,6]
l2 = [7,8,9,1,2,3]
l1.extend(l2)
print(l1)