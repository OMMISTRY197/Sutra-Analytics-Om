str = input("Enter a string: ") #taking a string from user & storing into variable.
list1 = list(str) #converting the string into list & storing into variable.
len = len(list1) #storing the length of the list into a variable.
revstr = "" #defining an empty variable (which will be updated & will be final result to check palindrome).
i = len - 1 #value of i will be used in loop.

while i >= 0:
    revstr = revstr + list1[i] #concatenating & updating the "revstr" defined variable.
    i = i - 1 #decreasing the value of i to reach from the last index to first index.

if str == revstr: #the two string is same or not?
    print(str, " is palindrome") #if same.
else:
    print(str, " isn't palindrome") #if not same.