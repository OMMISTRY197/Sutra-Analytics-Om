# Display the last digit of the given number and check whether it is divisible by 3 or not

num=int(input("Enter a number:"))
lastdigit = num%10
if(lastdigit %3==0):
    print("number is divisible by 3 ".format(lastdigit))
else:
    print("number is not divisible by 3".format(lastdigit))
