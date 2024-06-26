#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# number = int(input("enter number: "))

# for row in range(number):
#     for space in range(number-row-1):
#         print(" ",end="")
#     for column in range(2*row+1):
#         print("*",end="")
#     print()
#     if row==number-1:
#         for row in range(number-2,-1,-1):
#                 for space in range(number-row-1):
#                  print(" ",end="")
#                 for column in range(2*row+1):
#                     print("*",end="")
#                 print()



# for row in range(number-2,-1,-1):
#     for space in range(number-row-1):
#         print(" ",end="")
#     for column in range(2*row+1):
#         print("*",end="")
#     print()

n = int(input("Enter Numnber:"))
rs = n-1
sp=n-1
for row in range(2*n-1):
    if row<=n-1:
        totalColumn=row+1
        totalSpace=sp
        sp-=1
    else:
        totalColumn=rs
        if row==n:
            sp+=1
        sp+=1
        totalSpace= sp 
        rs-=1
    for space in range(totalSpace):
        print(" ",end='')
    for col in range(2*totalColumn-1):
        print("*",end="")
    print()