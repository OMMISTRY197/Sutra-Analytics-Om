number = 5

# for row in range(number):
#     for space in range(number-row-1):
#         print("_",end="")
#     for column in range(2*row+1):
#         print("*",end="")
#     print()

for row in range(number):
    for column in range(number):
        if column < number-row-1:
            print("",end=" ")
        else:
            print("*",end=" ")
    print()


number = 5
space = number
for row in range(number):
    if row == 0:
        space-=1
        print(' '*space,end="")
        print("*")

    else:
        space-=1
        print(' '*space,end="")
        print('*' * (2*row+1))
