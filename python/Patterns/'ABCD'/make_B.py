number = int(input("enter number: "))

for row in range(number):
    for column in range(number):
        if column == 0 or column == number-1 or row == 0 or row == number-1 or row == number//2:
            print("B",end=" ")
        else:
            print(" ",end=" ")
    print()