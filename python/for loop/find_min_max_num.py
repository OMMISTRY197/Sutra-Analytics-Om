#find a minimum number using for loop and without using in-built function

list = [11,22,7,50,30]
min_num = list[0]

for num in list:
    if num < min_num:
        min_num = num
print("minimum number is:",min_num)

#find a maximum number using for loop and without using in-built function

list = [11,22,7,50,30]
max_num = list[0]

for num in list:
    if num > max_num:
        max_num = num
print("maximum number is:",max_num)

#find a maximum & minimum number using for loop and without using in-built function

list = [11,22,7,50,30]
min_num = list[0]
max_num = list[0]

for num in list:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
print("minimum number is:",min_num)
print("maximum number is:",max_num)