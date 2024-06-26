# Write a Python program to display the first and last colors from the following list.

list = ["red", "blue", "green", "yellow", "violet"]
new_list = list[::len(list)-1]
print(new_list)
