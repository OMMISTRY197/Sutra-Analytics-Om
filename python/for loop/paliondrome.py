string=input("Enter string : ")
revstr = ""
for i in string:
    revstr=i+revstr
print("Reversed string:",revstr)
if(string==revstr):
    print("The string is palindrome")
else:
    print("string is not palindrome")