#     *  *
#    **  **
#   ***  ***
#  ****  ****
# *****  *****

# *****  *****
#  ****  ****
#   ***  ***
#    **  **
#     *  *

number = int(input("enter number: "))
row1 = 1
row2 = number

for row in range(number):
    for space in range(number-row-1):
        print(" ",end="")
    for column in range(row+1):
        print("*",end="")
    print("  ",end="")
    while row1<=number:
        for column1 in range(1,row1+1):
            print("*",end="")
        row1+=1
        break
    print()
print()

for row in range(number,0,-1):
    for space in range(number-row):
        print(" ",end="")
    for column in range(row):
        print("*",end="")
    print("  ",end="")
    while row2>=1:
        for column1 in range(1,row2+1):
            print("*",end="")
        row2-=1
        break
    print()