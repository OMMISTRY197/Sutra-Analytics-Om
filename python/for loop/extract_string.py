# "Write a Python program to extract numbers from a given string.          
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: [12, 45]"

number1 = []

string1 = "red 12 black 45 green"

newList = string1.split(" ")
print(newList)

numbers = newList[1],newList[3]
print(list(numbers))

for i in numbers:
    number1.append(int(i))
print(number1)
