l1 = [33, 35, 5, 10, 15, 20, 35]
l2 = [35, 34, 5, 17, 18]

combined_list = l1 + l2

unique_numbers = []
duplicate_numbers = []
one_list = []

for num in combined_list:
    if combined_list.count(num) == 1:
        unique_numbers.append(num)
    elif num not in duplicate_numbers:
        duplicate_numbers.append(num)
    if num not in one_list:
        one_list.append(num)
print("Unique numbers:", unique_numbers)
print("Duplicate numbers:",duplicate_numbers)
print("One List:",one_list)