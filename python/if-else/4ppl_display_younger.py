#Accept the age of 4 people and display the younger one.

age1 = int(input("Enter the Age of om:"))
age2 = int(input("Enter the Age of aryan:"))
age3 = int(input("Enter the Age of rudraksh:"))
age4 = int(input("Enter the Age of mahir:"))

if age1<age2 and age1<age3 and age1<age3:
	print("The Youngest Age is om")
elif age2<age1 and age2<age3 and age2<age4:
	print("The Youngest Age is aryan")
elif age3<age1 and age3<age2 and age3<age4:
	print("The Youngest Age is rudraksh")
else:
	print("The Youngest Age is mahir")