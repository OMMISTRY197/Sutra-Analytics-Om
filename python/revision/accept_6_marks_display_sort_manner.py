# Write a program to accept marks of 6 students and display them in a sorted manner.

m1 = int(input("enter m1: "))
m2 = int(input("enter m2: "))
m3 = int(input("enter m3: "))
m4 = int(input("enter m4: "))
m5 = int(input("enter m5: "))
m6 = int(input("enter m6: "))

list1 = [m1, m2, m3, m4, m5, m6]
list1.sort()
print(list1)