arr = [['smit+jay-patel+om'], ['smit+jay-patel','vinay+saket'], ['smit+jay-patel+arya','mahir+om']]
result = []

for list_part in arr:
    for strng in list_part:
        parts = strng.split('+')
        for part in parts:
            found = False
            for item in result:
                if part == item[0]:
                    item[1] += 1
                    found = True
            if not found:
                result.append([part,1])
# print(result)

final_result = []
for name,num in result:
    final_result.append([name])
    final_result.append([num])
print(final_result)