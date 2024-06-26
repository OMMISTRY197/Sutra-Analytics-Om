number = int(input("enter number: "))
if number%2 == 0:
    number += 1
for row in range(number):
    for column in range(number):
        if column == 0 or column == number-1 or (row >= number//2 and (row==column or row+column == number-1)):
            print("W",end=" ")
        else:
            print(" ",end=" ")
    print()