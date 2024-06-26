def grade(num):
    if num>=90:
        return "Your grade is A"
    elif num>=80 and num<90:
        return "Your grade is B"
    elif num>=65 and num<80:
        return "Your grade is C"
    elif num>=50 and num<65:
        return "Your grade is D"
    elif num>=33 and num<50:
        return "You get passing marks"
    else:
        return("You are fail!")
    
user = int(input("enter your marks: "))
print(grade(user))