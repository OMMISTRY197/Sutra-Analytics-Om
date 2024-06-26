#Take two list number of elements and find same Number and print the numbers of list

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_numbers = []
for number1 in list1:
    for number2 in list2:
        if number1 == number2:
            common_numbers.append(number1)
print("common numbers: ", common_numbers)
