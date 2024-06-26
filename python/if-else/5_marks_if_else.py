name = str(input("enter your name: "))

maths = int(input("enter marks of maths: "))
chemistry = int(input("enter marks of chemistry: "))
physics = int(input("enter marks of physics: "))
biology = int(input("enter marks of biology: "))
english = int(input("enter marks of english: "))

if maths<33 or chemistry<33 or physics<33 or biology<33 or english<33:
    print("You are fail!!")

else:

    total = maths + chemistry + physics + biology + english
    print("total marks is:",total)

    percentage = total * 100 / 500
    print("percentage is:",percentage)

    if percentage >= 90:
        print("your grade is A") 
    elif percentage >= 80:
        print("your grade is B")
    elif percentage >= 65:
        print("your grade is C")
    elif percentage >= 50:
        print("your grade is D")
    elif percentage >= 33:
        print("your grade is E")
