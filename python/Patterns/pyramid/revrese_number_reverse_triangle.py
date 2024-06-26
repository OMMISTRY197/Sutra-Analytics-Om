# 7 6 5 4 3 2 1 
#   5 4 3 2 1 
#     3 2 1 
#       1 

number = 5

for row in range(number-2,-1,-1):
    for space in range(number-row):
        print(" ",end=" ")
    for column in range(2*row,-1,-1):
        print(column+1,end=" ")
    print()