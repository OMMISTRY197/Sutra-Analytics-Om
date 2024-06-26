#swap 2 list

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
for i in range(min(len(list1), len(list2))):
    list1[i], list2[i] = list2[i], list1[i]
print("List 1:", list1)
print("List 2:", list2)
