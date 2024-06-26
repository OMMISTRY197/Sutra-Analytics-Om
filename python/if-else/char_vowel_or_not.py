#Write a program to check whether the character is vowel or not.

char = input("Enter a character:")   
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
if char in vowels:  
    print("The character is a vowel")  
else:  
    print("The character is not vowel")  