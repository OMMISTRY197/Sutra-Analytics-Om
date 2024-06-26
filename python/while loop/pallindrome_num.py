#find palindrome number 

num = int(input("enter number: "))
rev = 0
temp = num

while num > 0:
    rem = num%10
    rev = rev*10 + rem
    num = num // 10
if temp == rev:
    print("number is palindrome")
else:
    print("number is not palindrome")