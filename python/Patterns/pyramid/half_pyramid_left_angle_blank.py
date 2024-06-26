#         * 
#       * * 
#     *   * 
#   *     * 
# * * * * * 

number = int(input("enter number: "))

for row in range(number):
    for column in range(number):
        if row == number-1 or column == number-1 or row+column == number-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()