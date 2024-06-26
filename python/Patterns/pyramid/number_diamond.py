#         1 
#       1 2 3 
#     1 2 3 4 5 
#   1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 9 
#   7 6 5 4 3 2 1 
#     5 4 3 2 1 
#       3 2 1 
#         1 

number = 5

for row in range(1,number+1):
    for space in range(number-row):
        print(" ",end=" ")
    for column in range(2*row-1):
        print(column+1,end=" ")
    print()
    if row == number:
        for row in range(number-2,-1,-1):
            for space in range(number-row-1):
                print(" ",end=" ")
            for column in range(2*row,-1,-1):
                print(column+1,end=" ")
            print()
