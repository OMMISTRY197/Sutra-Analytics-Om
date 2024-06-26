#     A
#    B C
#   D   E
#  F     G
# HIJKLMNOP

size = int(input("enter size: "))
alpha = 65

for row in range(size):
    for space in range(size-row-1):
        print(" ",end="")
    for column in range(2*row+1):
        if column == 0 or column == 2*row or row == size-1:
            print(chr(alpha),end="")
            alpha+=1
        else:
            print("_",end="")
    print()