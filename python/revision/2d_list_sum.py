list1 = [[1,2,3],
         [4,5,6],
         [7,8,9]
        ]
print("sum of 1st raw is: ",list1[0][0] + list1[0][1] + list1[0][2])
print("sum of 2nd raw is: ",list1[1][0] + list1[1][1] + list1[1][2])
print("sum of 3rd raw is: ",list1[2][0] + list1[2][1] + list1[2][2])

print("sum of 1st column is: ",list1[0][0] +list1[1][0] + list1[2][0])
print("sum of 2nd column is: ",list1[0][1] +list1[1][1] + list1[2][1])
print("sum of 3rd column is: ",list1[0][2] +list1[1][2] + list1[2][2])

print("sum of 1st cross is: ", list1[0][0] + list1[1][1] + list1[2][2])
print("sum of 2nd cross is: ", list1[0][2] + list1[1][1] + list1[2][0])