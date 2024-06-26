# given 2d list no sum karavano & badhi list na sum ne different list ma store karavano
# and je different list ma sum aayo tene 1 list ma convert karine tene 1 list ma sum karvano.
list1 = [[1,2,3,4],
         [5,6,7],
         [[8,9,10],[20,21,21],
         [["Shakti","harsh"],["Prem","Smit","Kishan"]]]
        ]

list_1_row = [list1[0][0] + list1[0][1] + list1[0][2] + list1[0][3]]
print("sum of 1st row: ", list_1_row)

list_2_row = [list1[1][0] + list1[1][1] + list1[1][2]]
print("sum of 2nd row: ", list_2_row)

list_3_row_1_column = [list1[2][0][0] + list1[2][0][1] + list1[2][0][2]]
print("sum of 3rd row & 1st column: ",list_3_row_1_column )

list_3_row_2_column = [list1[2][1][0] + list1[2][1][1] + list1[2][1][2]]
print("sum of 3rd row & 2nd column: ", list_3_row_2_column)

sumOfAllList = list_1_row + list_2_row + list_3_row_1_column + list_3_row_2_column
print(sumOfAllList)
sum2 = sum(sumOfAllList)
print([sum2])

# list1_1 = [list1[2][2][0][0]]
# print(list1_1)
# list1_2 = [list1[2][2][0][1]]
# print(list1_2)
# list1_3 = [list1[2][2][1][0]]
# print(list1_3)
# list1_4 = [list1[2][2][1][1]]
# print(list1_4)
# list1_5 = [list1[2][2][1][2]]
# print(list1_5)

# con_string = list1_1 + list1_2 + list1_3 + list1_4 + list1_5
# print(con_string)

# con_string.append("radhika")
# con_string.append("maulik")
# print(con_string)

# con_string[4],con_string[1],con_string[2],con_string[3],con_string[5],con_string[6] = con_string[1],con_string[5],con_string[3],con_string[6],con_string[2],con_string[4]
# print(con_string)

# print(con_string.remove("Shakti"))
# print(con_string)

# con_string.insert(2,"om")
# print(con_string)
# con_string.insert(4,"arya")
# print(con_string)
# con_string.pop(6)
# print(con_string)