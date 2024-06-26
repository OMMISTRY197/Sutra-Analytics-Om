#   * * *     * * * 
#  * * * *   * * * * 
#  * * * * * * * * * 
#   * * * * * * * * 
#    * * * * * * * 
#     * * * * * * 
#      * * * * * 
#       * * * * 
#        * * * 
#         * * 
#          *  
#  hash code to print heart is (0x2665)

number = int(input("enter number: "))
        
for row in range(number//2,number-1):
    #first triangle
    for space in range(number-row-1):
        print(" ",end="")
    for column in range(row+1):
        print("*",end=" ")

    #second triangle
    for space in range(2*(number-row-1)):
        print(" ",end="")
    for column in range(row+1):
        print("*",end=" ")
    print()

#reverse triangle
for row in range(2*number-1,0,-1):
    for space in range(2*number-row):
        print(" ",end="")
    for column in range(row,0,-1):
        print("*",end=" ")
    print()