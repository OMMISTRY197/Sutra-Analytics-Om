#Find armstrong number without using inbuilt function
'''if we need a armstrong number, we have to find power of the all digits
in the number. here we have number 153 so found the power of the 1,5 &3 and then 
+ of 3 digits we got result = 153''' 

number = str(int(input("Enter number: ")))
digit = 0
for i in number:
    digit = digit + int(i)**len(number)
if int(number) == digit:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
