#Write a program that sorts a list of numbers in ascending and descending order using the sort() method.

#ascending

list = [100, 200, 500, 600, 300]
list.sort()
print(list)

list1 = [100.43, 50.72, 90.65, 16.00, 04.41]
list1.sort()
print(list1)

str = ["hello", "apple", "xerox", "data", "good"]
str.sort()
print(str)

#descending

list = [100, 200, 500, 600, 300]
list.sort(reverse=True)
print(list)

list1 = [100.43, 50.72, 90.65, 16.00, 04.41]
list1.sort(reverse=True)
print(list1)

str = ["hello", "apple", "xerox", "data", "good"]
# str.sort(reverse=True)
str.sort()
str.reverse()
print(str)