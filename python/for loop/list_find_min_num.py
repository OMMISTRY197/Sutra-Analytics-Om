# Find minimum number of list Without using inbuilt methods

list = [11,5,8,19,2,25]
min_num = list[0]

for num in list:
    if num < min_num:
        min_num = num
print("minimum number is:",min_num)
