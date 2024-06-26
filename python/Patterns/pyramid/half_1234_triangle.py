#     1
#    123
#   12345
#  1234567
# 123456789

number = int(input("enter number: "))

for row in range(1,number+1):
    for space in range(number-row):
        print(" ",end="")
    for column in range(2*row-1):
        print(column+1,end="")
    print()