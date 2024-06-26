class min_max:

    def minmax(list1):
        min_num = list1[0]
        max_num = list1[0]
        for num in list1:
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num
        return min_num,max_num
    
list1 = [11,12,13,14,15]   
min_num,max_num = min_max.minmax(list1)
print('minimum number is:',min_num)
print('maximum number is:',max_num)

obj = min_max()
obj.minmax
