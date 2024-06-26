#"Take a string like this str = 'smit;soni;20;50;kishan;panchal;80;60;kishan;
# prajapati;90;100;jay;patel;60;50'.  in this string we have  name,surname,two 
# subject of marks find sum and avg and output like this [
#   [ 'smit soni', 70, 35 ],
#   [ 'kishan panchal', 140, 70 ],
#   [ 'kishan prajapati', 190, 95 ],
#   [ 'jay patel', 110, 55 ]
# ] ex: [Full Name , total marks, Avg]"

string1 = "smit;soni;20;50;kishan;panchal;80;60;kishan;prajapati;90;100;jay;patel;60;50"
data_list = string1.split(';')
print(data_list)

# ['smit', 'soni', '20', '50', 'kishan', 'panchal', '80', '60', 
#  'kishan', 'prajapati', '90', '100', 'jay', 'patel', '60', '50']

result_list = []
for i in range(0, len(data_list), 4):
    full_name = "{} {}".format(data_list[i], data_list[i + 1])
    print(full_name)

    marks_subject1 = int(data_list[i + 2])
    marks_subject2 = int(data_list[i + 3])
    total_marks = marks_subject1 + marks_subject2
    print(total_marks)
    
    average_marks = total_marks / 2
    print(average_marks)
    result_list.append([full_name, total_marks, average_marks])
print(result_list)