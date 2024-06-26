#Display that the number is divisible by 2

def div(num):
    if num %2 == 0:
        return "number is div by 2"
    else:
        return "number is not divisible by 2"

user = int(input("enter number: ")) 
print(div(user))