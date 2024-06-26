#sort the list without using in-built method.

lst = [4, 8, 67, 78, 23, 45, 12, 13, 15, 16, 14, 11, 26, 65, 2, 5,  3, 6, 7]
n = len(lst)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]
print("Sorted list:", lst)