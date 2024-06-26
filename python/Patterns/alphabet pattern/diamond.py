#      A
#     ABC
#    ABCDE
#   ABCDEFG
#  ABCDEFGHI
#   ABCDEFG
#    ABCDE
#     ABC
#      A

size = int(input("enter size: "))
alpha = 65

for row in range(size):
    for space in range(size-row):
        print(" ",end="")
    for column in range(2*row+1):
        print(chr(alpha + column),end="")
    print()

for row in range(size-2,-1,-1):
    for space in range(size-row):
        print(" ",end="")
    for column in range(2*row+1):
        print(chr(alpha + column),end="")
    print()