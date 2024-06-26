myArr = [[101, "Smit", "C++", 105],
[102, "Harsh", "java", 106],
[103, "Punam", "Python", 105],
[104, "Bunty", "NodeJs", 107],
[105, "Kishan","Prajapati",''],
[106, "Vinay","Mistry",''],
[107, "Amit","Panchal",''],
[108, "Ram","PHP",106]
]

for sub_list in myArr:
    if sub_list[-1]:
        sub_list[-1] = myArr[sub_list[-1] - 101][1]
print(myArr)