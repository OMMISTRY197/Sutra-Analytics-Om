# "A company decided to give bonus to the employees as per the following criteria:                                      Time period of service                                      Bonus
# >10 years                                         10%
# >=6years and <=10years                            8%
# Less than 6 years                                 5%

emp = int(input("please enter your working years: "))

if emp>10:
    print("your salary will increment by 10%")
elif emp>=6 and emp<=10:
    print("your salary will increment by 8%")
else:
    print("your salary will increment by 5%")