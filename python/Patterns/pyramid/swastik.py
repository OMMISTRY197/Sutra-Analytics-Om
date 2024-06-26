# *   * * * 
# *   *     
# * * * * * 
#     *   * 
# * * *   * 

number = int(input("enter number: "))
if number%2 == 0:
    number+=1

for row in range(number):
    for column in range(number):
        # if (row == number//2):
        if (row == number//2) or (column == number//2) or (row == 0 and column > number//2) or (row == number-1 and column < number//2) or (column == 0 and row < number//2) or (column == number-1 and row > number//2):
            print("*",end=" ")
        # elif row == 0 and column == 0 and column == 2 and column == 3: 
        #     print("* ",end=" ")
        else:
            print(" ",end=" ")
    print()