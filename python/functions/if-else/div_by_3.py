#Display that the number is divisible by 3

def div(num):
    if num %3 == 0:
        print("num is div by 3")
    else:
        print("num is not div by 3")
    return div
user = int(input("enter number: "))
print(div(user))