# A 
# B C 
# D E F 
# G H I J 
# K L M N O

number = int(input("enter number: "))
alpha = 65
for row in range(1,number+1):
    for column in range(1,row+1):
        print(chr(alpha),end=" ")
        alpha = alpha + 1
    print()