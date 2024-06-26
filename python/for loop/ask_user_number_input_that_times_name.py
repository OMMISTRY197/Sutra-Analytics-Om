# Ask the user for a range for ex user entered 5 
# Now ask 5 times for the names like 
# 1st time enter the name : Smit
# 2nd time : Radhika
#  as it is
# And then print all 5 names in a list

ask_range = int(input("enter number: "))
store_list= [] 
for number in range(ask_range):
    ask_name = str(input("enter {} name:".format(number+1)))
    store_list.append(ask_name)
print(store_list)