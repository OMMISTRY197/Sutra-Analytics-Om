# a = [1,2,3,5,7]
# b = [4,5,6,5,6,8]

# Swap both value if 'a' undefined then put name same as b
# Output:
# A = [ 4, 5, 6, 5, 6, 8 ] B = [ 1, 2, 3, 5, 7, 'kishan' ]

a = [1,2,3,5,7]
b = [4,5,6,5,6,8]

a,b = b,a
print(a)
print(b)

b.append("kishan")
print(b)