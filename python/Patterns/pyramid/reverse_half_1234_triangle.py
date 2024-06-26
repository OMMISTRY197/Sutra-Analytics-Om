#  123456789
#   1234567
#    12345
#     123
#      1

number = int(input("enter number: "))

for row in range(number-1,-1,-1):
    for space in range(number-row):
        print(" ",end="")
    for column in range(2*row+1):
        print(column+1,end="")
    print()