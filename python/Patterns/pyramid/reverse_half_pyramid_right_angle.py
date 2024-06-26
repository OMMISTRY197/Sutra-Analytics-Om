# * * * * * 
# * * * * 
# * * * 
# * * 
# *

number = int(input("enter number: "))

for row in range(number,0,-1):
    for column in range(row):
        print("*",end=" ")
    print()