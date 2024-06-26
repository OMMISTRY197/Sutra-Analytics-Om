class average:
    def list1(listavg):
        sum = 0
        for num in listavg:
            sum +=num
        avg = sum/len(listavg)
        print(avg)
    

listavg = [11,12,13,14,15,16]
avg = average.list1(listavg)
obj = average()
obj.list1
