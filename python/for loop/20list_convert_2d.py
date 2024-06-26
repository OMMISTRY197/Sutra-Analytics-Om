# Take 20 number of list and convert in to two dimensional list 
#  output its"[[1,2],[3,4],[5,6],[7,8],[9,10].....]"

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

two_dimensional_list = []

for i in range(0, len(original_list), 2):
    pair = [original_list[i], original_list[i + 1]]
    two_dimensional_list.append(pair)
print("two-dimensional list:", two_dimensional_list)
