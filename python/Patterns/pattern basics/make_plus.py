#     +     
#     +     
# + + + + + 
#     +     
#     + 

number = int(input("enter number: "))
if number%2==0:
    number+=1
for row in range(number):
    for column in range(number):
        if column == number//2 or row == number//2:
            print("+",end=" ")
        else:
            print(" ",end=" ")
    print()