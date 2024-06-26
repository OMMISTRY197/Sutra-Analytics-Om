#Write a program to check if a string contains only alphabetic characters.

str = input("Enter a string:")

if str.isalpha():
    print("The string contains only alphabetic characters.")
else:
    print("The string contains non-alphabetic characters.")