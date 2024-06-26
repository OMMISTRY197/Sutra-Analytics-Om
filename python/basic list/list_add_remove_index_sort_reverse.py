fruits = ["apple", "mango", "cherry", "orange", "grapes"]
print("original list: ",fruits)

fruits.insert(2,"om")
fruits.insert(4,"arya")
print("added element list: ",fruits)

fruits.pop(1)
fruits.pop(3)
print("removed element list: ",fruits)

fruits.sort()
print("alphabetical sorted list: ",fruits)

# fruits.sort(reverse=True)
# print("reversed list: ",fruits)

# fruits.reverse()
# print("reversed list 2: ",fruits)

print("reversed list 3: ",fruits[::-1])