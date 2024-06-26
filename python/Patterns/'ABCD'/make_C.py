number = int(input("enter number: "))

for row in range(number):
    for column in range(number):
        if row == 0 or row == number-1 or column==0: 
            print("C",end=" ")
        else:
            print(" ",end=" ")
    print()