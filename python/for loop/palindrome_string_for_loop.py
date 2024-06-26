string = input("enter string: ")
revstr = ""

for i in string:
    revstr += i
print("reversed string: ",revstr)
if string == revstr:
    print("string is palindrome")
else:
    print("string is not palindrome")
