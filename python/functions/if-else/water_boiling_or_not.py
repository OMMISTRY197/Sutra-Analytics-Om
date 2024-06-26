#water is boiling or not.

def water(cel):
    if cel > 100:
        print("water is boiling at",user,"celcius")
    else:
        print("water is not boiling")
    return water

user = int(input("enter number: "))
print(water(user))