#Write a program in which you have to take 2 variables and user input for them and check the largest one ,
# the smallest one and check if the first variable is divisible by the second one.

variable1 = float(input("Enter the first variable: "))
variable2 = float(input("Enter the second variable: "))

# Check and print the largest and smallest variables
if variable1 > variable2:
    print("variable1 is the largest")
    print("variable2 is the smallest")
elif variable1 < variable2:
    print("variable2 is the largest")
    print("variable1 is the smallest")
else:
    print("Both variables are equal")

# Check and print if the first variable is divisible by the second one
    
if variable2 != 0 and variable1 % variable2 == 0:
    print("variable1 is divisible by variable2")
elif variable2 == 0:
    print("Cannot divide by zero.")
else:
    print("variable1 is not divisible by variable2")