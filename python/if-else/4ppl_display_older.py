#Accept the age of 4 people and display the older one.

age1 = int(input("enter age1:"))
age2 = int(input("enter age2:"))
age3 = int(input("enter age3:"))
age4 = int(input("enter age4:"))

if age1>age2 and age1>age3 and age1>age4:
    print("you are adult")
elif age2>age1 and age2>age3 and age2>age4:
    print("you are young adult")
elif age3>age1 and age3>age2 and age3>age4:
    print("you are young")
else:
    print("you are minor")
