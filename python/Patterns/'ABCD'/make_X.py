number = int(input("enter number: "))

for row in range(number):
    for column in range(number):
        if column == row or row+column == number-1: 
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()