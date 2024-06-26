# find a minimun value and maximun value from the given list.

elelist = [1, 80, 70, 75, 85, 90, 45, 104, 0]

min_num = elelist[0]
max_num = elelist[0]

for num in elelist:
    if num < min_num:
        min_num = num 
    if num > max_num:
        max_num = num

print("minimum number is:",min_num)
print("maximum number is:",max_num)