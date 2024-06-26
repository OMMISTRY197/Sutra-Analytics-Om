#      1     
#     1 2    
#    1   2   
#   1     2  
#  1       2 
#   1     2  
#    1   2   
#     1 2    
#      1

number= int(input("enter number: "))
number+=1

for row in range(1,number):
    for column in range(1,2*number):
        if (column==2*number//2 and row==1) or (row+column == number+1 and row<number):
            print(1,end="")
        elif column>number and column-row==number-1 and row<number:
             print(2,end="")
        else:
            print(" ",end="")
    print()
for row in range(number-2,0,-1):
    for column in range(1,2*number):
        if (column==2*number//2 and row==0) or (row+column == number+1 and row<number):
            print(1,end="")
        elif column>number and column-row==number-1 and row<number:
             print(2,end="")
        else:
            print(" ",end="")
    print()