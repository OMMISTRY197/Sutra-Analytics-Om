# pass_total = 33*5
# print("total passing marks: ", pass_total)

python = int(input("enter marks of python: "))
java = int(input("enter marks of java: "))
html = int(input("enter marks of html: "))
css = int(input("enter marks of css: "))
php = int(input("enter marks of php: "))

# if python >100 or java >100 or html>100 or css >100 or php >100:
#     print("please enter marks between 1-100") 
# else:
total = python + java + html + css + php
print("total marks: ", total)

percentage = total*100 / 500
print("percentage is: ", percentage)

if python <33 or java <33 or html <33 or css <33 or php <33:
    print("your are fail!!!")
else: 
        if percentage >= 90:
            print("your grade is A")
        elif percentage <90 and percentage >=80:
            print("your grade is B")
        elif percentage <80 and percentage >=65:
            print("your grade is C")
        elif percentage <65 and percentage >=50:
            print("your grade is D")
        elif percentage <50 and percentage >=33:
            print("your grade is E")