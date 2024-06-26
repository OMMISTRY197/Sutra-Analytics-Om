#Take number of list and Find Unique number in list without using inbult function

list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
uniquelist = []
for i in list:
    if i not in uniquelist:
        uniquelist.append(i)
print(uniquelist)