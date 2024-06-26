list1 = [1,2,1,3,4,2,1,5,6]
non_repeatable_numbers = []

for num in list1:
    if list1.count(num) == 1:
        non_repeatable_numbers.append(num)
print(non_repeatable_numbers)