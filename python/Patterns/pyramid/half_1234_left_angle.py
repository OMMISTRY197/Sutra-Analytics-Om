#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5 

number = int(input("enter number: "))

for row in range(1,number+1):
    for space in range(number-row):
        print(" ",end=" ")
    for column in range(row):
        print(column +1,end=" ")
    print()