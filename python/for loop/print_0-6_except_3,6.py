#for loop, print 0 to 6 except 3 & 6.

for num in range(0,7):
    if num == 3 or num == 6:
        continue
    print(num)