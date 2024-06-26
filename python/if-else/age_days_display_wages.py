# Accept the age, gender (M,F), number of days and display the wages accordingly:                                         
#  Age                            Gender                            Wage/Day
# >=18 and <30                      M                                  700
#     ____                          F                                  750
# >=30 and <=40                     M                                  800
#     ____                          F                                  850

age = int(input("enter your age: "))
gender = (input("enter your gender M/F: ")).lower()
days = int(input("enter working days: "))

if age>=18 and age<30 and gender == "male":
   wage = days * 700
   print(wage)  
elif age>=18 and age<30 and gender == "female":
    wage = days * 750
    print(wage)
elif age>=30 and age<=40 and gender == "male":
    wage = days * 800
    print(wage)
elif age>=30 and age<=40 and gender == "female":
    wage = days * 850
    print(wage)
else:
    print("please enter valid value")

