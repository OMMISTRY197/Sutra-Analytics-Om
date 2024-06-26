# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

number = int(input("enter number: "))

for row in range(1,number+1):
    for column in range(row):
        print("*",end=" ")
    print()

for row in range(number-1,0,-1):
    for column in range(row):
        print("*",end=" ")
    print()

# n = int(input("Enter N:"))
# rs = n-1
# for row in range(0,2*n-1):
#     if row<=n-1:
#         totalColumn=row
#     else:
#         totalColumn=rs-1
#         rs-=1
        
#     for col in range(totalColumn+1):
#         print("*",end='')
    
#     print()