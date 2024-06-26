# take a number from the user and then number is divisible by 2 & 3 return yes.

def div(num):
    if num %2 == 0 and num %3 == 0:
        return "num is div by 2 & 3"
    else:
        return "num is not div by 2 & 3"
user = int(input("enter the number: "))
print(div(user))