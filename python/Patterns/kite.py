#             * 
#           * * * 
#         * * * * * 
#       * * * * * * * 
#     * * * * * * * * * 
#   * * * * * * * * * * * 
# * * * * * * * * * * * * * 
#   * * * * * * * * * * * 
#     * * * * * * * * * 
#       * * * * * * * 
#         * * * * *
#           * * *
#             *
#           * * *
#         * * * * *

number = int(input("enter number: ")) 

for row in range(number):
    for space in range(number-row-1):
        print(" ",end=" ")
    for column in range(2*row+1):
        print("*",end=" ")
    print()

for row in range(number-2,-1,-1):
    for space in range(number-row-1):
        print(" ",end=" ")
    for column in range(2*row+1):
        print("*",end=" ")
    print()

for row in range(1,number//2):
    for space in range(number-row-1):
        print(" ",end=" ")
    for column in range(2*row+1):
        print("*",end=" ")
    print()