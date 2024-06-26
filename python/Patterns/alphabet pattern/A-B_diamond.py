#      A     
#     A B
#    A   B
#   A     B
#  A       B
#   A     B
#    A   B
#     A B
#      A

size = int(input("eneter size: "))
size += 1
alpha = 65
beta = 66

for row in range(1,size):
    for column in range(1,2*size):
        if (column==2*size//2 and row==1) or (row+column == size+1 and row<size):
            print(chr(alpha),end="")
        elif column>size and column-row==size-1 and row<size:
             print(chr(beta),end="")
        else:
            print(" ",end="")
    print()

    if row == size-1:
        for row in range(size-2,0,-1):
            for column in range(1,2*size):
                if (column==2*size//2 and row==0) or (row+column == size+1 and row<size):
                    print(chr(alpha),end="")
                elif column>size and column-row==size-1 and row<size:
                    print(chr(beta),end="")
                else:
                    print(" ",end="")
            print()