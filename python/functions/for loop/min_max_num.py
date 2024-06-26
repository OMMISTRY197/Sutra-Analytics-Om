def min_max():
    return min_max
list1 = [11,12,13,14,15]
min_num = list1[0]
max_num = list1[0]

for num in list1:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
print('minimum number is:',min_num)
print('maximum number is:',max_num)