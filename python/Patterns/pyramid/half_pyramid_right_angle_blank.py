# *
# * *       
# *   *     
# *     *   
# * * * * *

number = int(input("enter number: "))

for row in range(number):
    for column in range(number):
        if column == 0 or row == number-1 or row == column:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()