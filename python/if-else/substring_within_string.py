#Write a Program to search for a substring within a string

main_string = input("Enter a string: ")
substring = input("Enter a substring to search: ")
if substring in main_string:
    print(f"The substring '{substring}' is found in the string.")
else:
    print(f"The substring '{substring}' is not found in the string.")
