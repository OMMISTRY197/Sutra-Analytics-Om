#"Write a Python program to convert a given heterogeneous list of scalars into a string.
#Original list:['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
#Convert the heterogeneous list of scalars into a string:
#Red,100,-50,green,w,3,r,12.12,False"

original_list = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
convert_string = ""

for heterogeneous in original_list:
    convert_string = convert_string + str(heterogeneous) + ","
print(convert_string)