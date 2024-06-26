#find the duplicates

myArr = [1,2,3,4,5,6,7,8,9]
secArr = [5,4,7,1,11,9]

duplicate = []

for num1 in myArr:
    for num2 in secArr:
        if num1 == num2 and num1 not in duplicate:
            duplicate.append(num1)
print(duplicate)
        
