list1 = [11,22,9,78,45,15]
min_num = list1[0]
max_num = list1[0]

for num in list1:
    if num < min_num:
        min_num = num

    if num > max_num:
        max_num = num
        
print(min_num)
print(max_num)