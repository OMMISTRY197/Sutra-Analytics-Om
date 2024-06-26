# Ask the user for a range for ex user entered 5 
# Now ask 5 times for the numbers like 
# 1st time enter the number : 10
# 2nd time : 20
#  as it is
# And then print all 5 numbers in a list

user_range = int(input("enter a number: "))
store_list = []

for number in range(user_range):
    ask_number = int(input("enter the {}st number: ".format(number+1)))
    store_list.append(ask_number)
print(store_list)
