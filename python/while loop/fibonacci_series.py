#fibonacci series using while loop

print("fibonacci numbers between 0 to 50 are:")
a , b = 0 , 1
print(a)
print(b)
while b < 50:
    a , b = b , a + b 
    print(b)
