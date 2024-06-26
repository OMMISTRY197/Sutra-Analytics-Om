#Write a program to interchange first and last element in a list.

list1 = ["Red","Green","White" ,"Black"]
print("original list : ", list1)
list1[0] , list1[-1] = list1[-1] , list1[0]
print("interchanged list: ",list1)