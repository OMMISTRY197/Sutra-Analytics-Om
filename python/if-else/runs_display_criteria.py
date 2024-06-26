# Write a program to accept runs from the user and display the result as per the following criteria:          
# Marks                                                  Grade
# >=100                                                  Century
# >=50                                                     Fifty
# below 50                                Neither a century nor fifty

runs = int(input("enter runs: "))

if runs>=100:
    print("Century")
elif runs>=50:
    print("fifty")
else:
    print("Neither a century nor fifty")