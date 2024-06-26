# "Write a program to accept percentage and display the category as per the following criteria:                                      Percentage                                              Category
# <40                                                               Failed 
# >=40 and <55                                               Fair
# >=55 and <65                                             Good
# >=65                                                        Excellent
# "

percentage = int(input("enter percentage: "))

if percentage>=65:
    print("excellent")
elif percentage>=55 and percentage<65:
    print("good")
elif percentage>=40 and percentage<55:
    print("fair")
else:
    print("failed")
