list1 = [1,2,1,3,4,2,1,5,6]
list2 = []
duplicate_list = []

for num in list1:
    if num not in list2:
        list2.append(num)
    elif num not in duplicate_list:
        duplicate_list.append(num)
print(duplicate_list)