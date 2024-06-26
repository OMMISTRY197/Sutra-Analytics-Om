# "Write a Python program to convert a given heterogeneous list of scalars into a string.Original list:
# ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
# Convert the heterogeneous list of scalars into a string:
# Red,100,-50,green,w,3,r,12.12,False"\

list = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
converted_string = ""

for element in list:
    converted_string += str(element) + ','
print(converted_string)
