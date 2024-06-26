a = [1,2,3,5,7]
b = [4,5,6,5,6]

if len(a) < len(b):
    a.append('om')
elif len(a) > len(b):
    b.append('om')
else:
    a.append('om')
    b.append('om')

a,b = b,a
print('A =',a)
print('B =',b)