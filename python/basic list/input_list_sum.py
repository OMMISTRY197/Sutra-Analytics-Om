#Input a list from user and sum of list elements and average of it

el1 = int(input("enter list element-1: "))
el2 = int(input("enter list element-2: "))
el3 = int(input("enter list element-3: "))
el4 = int(input("enter list element-4: "))
el5 = int(input("enter list element-5: "))

num = [el1,el2,el3,el4,el5]

print(num)

print("sum of list is: ", sum(num))

print("avg of list is: ",sum(num) / 2)