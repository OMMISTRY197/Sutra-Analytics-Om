# Check for voting...
# If the user's age is 18 or more ask for voting card and if he/she is not having it ask them for applying 
# And if the user's age is less than 18 he is not eligible for vote

age = int(input("enter age: "))

if age>=18:
    apply = input("you have voter i'd card? True/False ").lower()
    if apply == "true":
        print("good")
    else:
        print("please apply for water i'd card")
else:
    print("you are not eligible for vote")