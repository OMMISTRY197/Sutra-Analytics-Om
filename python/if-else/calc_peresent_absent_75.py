# Take working days and absent days from the user , count present days with help of 
#it and then count percentage of working days , if per > 75 you are eligible for exam otherwise not...

working_days = int(input("Enter the number of working days: "))
absent_days = int(input("Enter the number of absent days: "))
if working_days < 0 or absent_days < 0:
    print("Please enter valid positive numbers for working days and absent days.")
total_days = working_days + absent_days
present_days = working_days
percentage = (present_days / total_days) * 100
print(percentage)
if percentage > 75:
    print("Congratulations! You are eligible for the exam.")
else:
    print("Sorry, you are not eligible for the exam. Attendance is below 75%.")
