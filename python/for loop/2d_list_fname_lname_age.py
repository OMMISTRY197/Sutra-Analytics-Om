# "Take a 2d list (For example :  [[Radhika,Khilwani,22]] ) , Take atleast 10 data as in example ,
# store information name,age,address .
# You have to print it like The name is Radhika ,  and The lastname is Khilwani and The age is 22."

data_list = [
    ["Radhika", "Khilwani", 22],
    ["Om", "Mistry", 17],
    ["Aryan", "Ojha", 18],
    ["Rudraksh", "Jani", 15],
    ["Vedanshu", "Patel", 22],
    ["Mahir", "Mistry", 19],
    ["Malav", "Mistry", 20],
    ["Kushal;", "Mehta", 10],
    ["Harsh", "Misrty", 27],
    ["Jenish", "Patel", 31]
]

for data in data_list:
    first_name, last_name, age = data
    print(f"the name is \'{first_name}\', and The lastname is \'{last_name}\', and The age is \'{age}\'.")