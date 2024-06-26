# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

number = int(input("enter number: "))

for row in range(number-1,-1,-1):
    #for space 
    for space in range(number - row - 1):  
        print(" ",end=" ")
    for column in range(row + 1):
        print("*",end=" ")
    print()