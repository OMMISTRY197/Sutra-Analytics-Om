# "Accept the following from the user and calculate the percentage of class attended:
# 1)Total number of working days 
# 2)Total number of days for absent. 
# After calculating percentage show that,if the percentage is less than 
# 75 than student will not be able to sit in exam.

working_days = int(input("total number of working days: "))
absent_days = int(input("total number of absent days: "))

percentage = working_days * 100 / absent_days
print("percentage of present days: ",percentage)

if percentage>=75:
    print("Congras! you are able to sit in the exam")
else:
    print("sorry! you are not able to sit in exam")

