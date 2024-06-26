# Take two list and match duplicate numbers and output in list. 
# Print which is duplicate without using inbuilt function

list1 = [1, 2, 3, 4, 5, 5, 6, 7]
list2 = [5, 6, 7, 8, 9, 9, 10]

duplicate = []

for num1 in list1:
    for num2 in list2:
        if num1 == num2 and num1 not in duplicate:
            duplicate.append(num1)
print("duplicate numbers:", duplicate)
