number = int(input("enter number: "))

for row in range(number):
    for column in range(number):
        if row == 0 or column == number //2:
            print("T",end=" ")
        else:
            print(" ",end=" ")
    print()