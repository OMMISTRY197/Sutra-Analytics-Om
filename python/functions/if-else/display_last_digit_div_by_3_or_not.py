# Display the last digit of the given number and check
# whether it is divisible by 3 or not

def checkdiv(last_digit):
    if last_digit%3==0:
        return "last digit is div by 3"
    else:
        return "last digit is not div by 3"
    
number = int(input("Enter a number: "))
last_digit = number % 10

print(checkdiv(last_digit))