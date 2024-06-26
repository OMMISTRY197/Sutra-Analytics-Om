# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10

number = int(input("enter number: "))
num = 1
for row in range(1,number+1):
    for column in range(1,row+1):
        print(num,end=" ")
        num = num + 1
    print()