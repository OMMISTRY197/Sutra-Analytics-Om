def func(**name):
    print("first name is:",name["fname"])
    print("last name is:",name["lname"])

func(fname = str(input("Enter first name:")).capitalize(), lname = str(input("Enter last name:")).capitalize())
