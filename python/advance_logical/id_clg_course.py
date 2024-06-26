college = [
    [101, "Gls"], [102, "Vidhyanagri"],
    [103, "GrowMore"]
]
courses = [
    [501, "Java"], [502, "C++"],
    [503, "Php"], [504, "Python"],
    [505, "Advance.Net"]
]

output = []

for clg_id, clg_name in college:
    for course_id, course_name in courses:
        clg_course = "['clg_id:{0}', 'clg_name:{1}', 'course_id:{2}', 'course_name:{3}']".format(clg_id,clg_name,course_id,course_name)
        output.append(clg_course)
print(output)