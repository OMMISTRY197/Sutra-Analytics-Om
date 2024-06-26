#Write a program to check if a string contains only alphabetic characters

def alphabetic(string1):
    if string1.isalpha():
        return "The string contains only alphabetic characters."
    else:
        return "The string contains non-alphabetic characters."
    
string1 = input("enter string: ")
print(alphabetic(string1))