#Take a 1-100 numbers and the number which is divisable by 3,4,5 print all numbers in diffrent list

divisible_by_3_4_5 = []

for number in range(1, 101):
    if number % 3 == 0 and number % 4 == 0 and number % 5 == 0:
        divisible_by_3_4_5.append(number)
print("numbers divisible by 3, 4, and 5:", divisible_by_3_4_5)
