#         * 
#       *   * 
#     *       * 
#   *           * 
# * * * * * * * * * 

number = int(input("enter number: "))

for row in range(number):
    for column in range(number-row-1):
        print(" ",end=" ")
    for column in range(2*row+1):
        if column == 0 or column == 2*row or row == number-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()