# "Accept the following from the user and calculate the percentage of class attended:
# 1)Total number of working days 
# 2)Total number of days for absent.
# After calculating percentage show that,if the percentage is less than 75,
# than student will not be able to sit in exam.


working_days = int(input("enter the working days: "))
absent_days = int(input("enter the absent days: "))

total_days = working_days + absent_days
percentage = working_days / total_days * 100
print(percentage)

if percentage >= 75:
    print("you are able to sit in exam")
else:
    print("you are not able to sit in exam")