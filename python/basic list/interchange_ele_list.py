#Write a program to interchange first and last element in a list.

list = [1,2,3,4,5,6,7]
list[0], list[-1] = list[-1], list[0]
print(list)