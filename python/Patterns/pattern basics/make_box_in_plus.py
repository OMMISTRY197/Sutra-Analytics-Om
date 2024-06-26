# * * * * * 
# *   *   * 
# * * * * * 
# *   *   * 
# * * * * * 

number = int(input("enter number: "))
if number%2==0:
    number+=1
for row in range(number):
    for column in range(number):
        if row == 0 or row == number-1 or column == 0 or column == number-1 or row == number //2 or column == number//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()