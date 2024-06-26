#Write a Python program to get the Fibonacci series between 0 and 50

a, b = 0, 1
print("Fibonacci series between 0 and 50:")
print(a)

for i in range(51):
    a, b = b, a + b
    if a <= 50:
        print(a)
    else:
        break