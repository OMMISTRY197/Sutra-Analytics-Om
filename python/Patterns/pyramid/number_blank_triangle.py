#     1    
#    1 2   
#   1   2  
#  1     2 
# 123456789

number = 5
n = 1

for row in range(1,number+1):
    for column in range(1,2*number):
        if (column==2*number//2 and row==1) or (row+column == number+1 and row<number):
            print(1,end="")
        elif column>number and column-row==number-1 and row<number:
             print(2,end="")
        elif row==number:
            print(n,end="")
            n+=1
        else:
            print("_",end="")
    print()
