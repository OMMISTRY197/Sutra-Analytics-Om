# "Take a 2d list (For example :  [[Radhika,Khilwani,22]] ) 
# , Take atleast 10 data as in example , store information name,age,address .
# You have to print it like The name is Radhika ,  and The lastname is Khilwani
# and The age is 22."

data = [["radhika","khilwani",22],
        ["om","mistry",17],
        ["arya","patel",22],
        ["jay","panchal",21],
        ["smit","soni",24],
        ["vinay","rathod",19],
        ["saket","tarwani",40],
        ["mahir","mistry",18],
        ["vedanshu","patel",19],
        ["aryan","ojha",18]
]
for i in data:
    fname , lname , age = i
    a = "the name is: {0} last name is: {1} and age is {2}"
    print(a.format(fname,lname,age))