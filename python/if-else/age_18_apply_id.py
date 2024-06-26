age = int(input("enter your age: "))

if age>=18:
    apply = input("you have voter id? ").lower()
    if apply == 'no':
        print("please apply for voter id card")
    else:
        print("you are eligible for voting")
else:
    print("you are not eligible for voting")