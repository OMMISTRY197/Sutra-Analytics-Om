#Take number of list and Find Duplicate values in list without using inbuilt function

list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
duplicatelist = []
for i in list:
    if i not in duplicatelist:
        duplicatelist.append(i)
print(duplicatelist)