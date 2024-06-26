#  ABCDEFGHI
#   ABCDEFG
#    ABCDE
#     ABC
#      A

size = int(input("enter number: "))
alpha = 65

for row in range(size-1,-1,-1):
    for space in range(size-row):
        print(" ",end="")
    for column in range(2*row+1):
        print(chr(alpha + column),end="")
    print()