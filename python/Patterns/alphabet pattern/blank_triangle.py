# ____A____
# ___A_B___
# __A___B__
# _A_____B_
# ABCDEFGHI


size = 5
alpha = 65
beta = 66

for row in range(1,size+1):
    for column in range(1,2*size):
        if (column==2*size//2 and row==1) or (row+column == size+1 and row<size):
            print(chr(alpha),end="")
        elif column>size and column-row==size-1 and row<size:
            print(chr(beta),end="")
        elif row==size:
            print(chr(alpha),end="")
            alpha+=1
        else:
            print("_",end="")
    print()