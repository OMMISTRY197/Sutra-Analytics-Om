#         * 
#       *   * 
#     *       * 
#   *           * 
# *               *         

number=int(input("enter number: "))

for row in range(number):
    for j in range(number-row-1):
        print(" ",end=" ")
    for j in range(2*row+1):
        if j==0 or j == 2*row:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

