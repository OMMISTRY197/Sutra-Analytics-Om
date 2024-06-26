# *Write a program that inputs an integer in range 0-999 and then prints if the integer entered is 1/2/3 digit number.

num=int(input("Enter a number : "))
if num<0:
    print("Invalid entry")
elif num<10:
    print("single digit number")
elif num<100:
    print("double digit number")
elif num<1000:
    print("Three digit number")
else:
    print("not vailed number, The number should between 0 to 999 only")