#Write a program to extract a substring from a string using slicing.

string = "ommistry"
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)
print(string[s1])
print(string[s2])
print(string[s3])