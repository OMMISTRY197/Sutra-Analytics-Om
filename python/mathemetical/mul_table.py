start = int(input("enter number of table you want to start : "))
end = int(input("enter the number of table you want to end: "))
for i in range(start,end+1):
    for j in range(1,11):
        print(i , "x" , j , "=" , i*j)
    print()