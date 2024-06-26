def sum1(list1,sum):
    pairs = []
    if sum in list1:
        pairs.append((0,sum))
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] + list1[j] == sum:
                pair=((list1[i], list1[j]))
                if pair not in pairs and pair[::-1] not in pairs:
                    pairs.append(pair)

    return pairs

list1 = [1,2,1,2,1,2,1,2,3]
user_input = int(input("Enter Number: "))
pairs = sum1(list1,user_input)
print(pairs)

# in this, pela list ma element aapela hoy & user input kare je value teno sum list 
# mathi je elements no thato hoy teni pair return thavi joiye.

# jo list ma same value hoy to sum ma & return vakhate value repeat na thavi joiye

# user je value enter kare e list ma exist karti hoy to eni sathe default value
# 0 aavi joiye