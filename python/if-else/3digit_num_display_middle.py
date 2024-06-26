#Display that the given number is 3 digit number or not and also display the second/middle number

number = int(input("Enter a number: "))
if 100 <= number <= 999:
    print("number is a 3-digit number")
            
    second_digit = (number // 10) % 10
    print(f"The second (middle) digit is: {second_digit}")
else:
    print(f"{number} is not a 3-digit number.")
