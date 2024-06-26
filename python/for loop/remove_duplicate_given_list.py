#list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]] remove duplicates from this list

list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
remove_list = []

for sublist in list:
    if sublist not in remove_list:
        remove_list.append(sublist)
print(remove_list)
