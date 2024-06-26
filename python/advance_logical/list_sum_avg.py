myArr = [
    [1, "Smit", 60, 70, 30, 50, 70, 100],
    [2, "maulik", 50, 40, 30, 50, 70, 240],
    [3, "mehul", 40, 60, 50, 80, 100],
    [4, "Manthan", 45, 54, 50, 80, 100],
    [5, "Abhishek", 55, 43, 50, 80, 100]
]

for row in myArr:
    student_id, name, *marks = row
    sum_marks = sum(marks)
    avg_marks = sum_marks / len(marks) 

    print("Row {} Sum = {} , avg= {:.2f}".format(student_id, sum_marks, avg_marks))
