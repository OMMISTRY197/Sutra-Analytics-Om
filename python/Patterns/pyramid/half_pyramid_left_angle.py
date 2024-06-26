#         *          #eg; number=5 - row etle ke row e 0 hse ane 
#       * *          -1 etle ek vakhat minus thase(5-0-1=4),
#     * * *          # loop na darek iteration ma row + thati jase mate 
#   * * * *          mate (5-1-1=4) & so on... 
# * * * * *

number = int(input("enter number: "))

for row in range(number):
    #for space 
    for space in range(number - row - 1):  
        print("_",end=" ")
    for column in range(row + 1):
        print("*",end=" ")
    print()