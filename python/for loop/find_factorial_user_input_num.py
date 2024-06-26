# Take a number from the user and find the factorial of the respected number.

number = int(input("enter the number to be factorial: "))
factorial = 1

for i in range(1,number+1):
    factorial = factorial * i 
print(factorial)