# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

number = 5

for row in range(number-1,-1,-1):
    for space in range(number-row-1):
        print(" ",end="")
    for column in range(2*row+1):
        print("*",end="")
    print()

for row in range(1,number):
    for space in range(number-row-1):
        print(" ",end="")
    for column in range(2*row+1):
        print("*",end="")
    print()