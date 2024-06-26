# *****
# *   *
# *   *
# *   *
# *****

number = int(input("enter number: "))

for row in range(number):
    for column in range(number):
        if row == 0 or column == 0 or row == number-1 or column == number-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\r")  #\r = end line(cursor e biji line na starting ma jatu rahe)