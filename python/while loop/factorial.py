#factorial using while loop.

number = int(input("enter number: "))
fact = 1

while number > 0:
    fact *= number  #fact = fact * number 
    number -= 1     #number = number - 1
print(fact)

# factorial using for loop.

number = int(input("enter number: "))
fact = 1

for i in range(1,number+1):
    fact = fact * i
print(fact)