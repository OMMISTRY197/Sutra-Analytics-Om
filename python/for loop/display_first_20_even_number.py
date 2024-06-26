# *Display the first 20 even numbers
num = int(input("enter number: "))
for num in range(1,2 * num + 1):
    if num %2 == 0:
        print(num)
