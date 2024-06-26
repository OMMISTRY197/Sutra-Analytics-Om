letter = input("Enter a letter: ")
result = ""
if letter.lower() in 'aeiou':
    result = "Vowel"
else:
    result = "Not a vowel"
print(f"The letter '{letter}' is {result}.")
