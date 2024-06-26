lst = ['MI' , 'CSK' , 'RCB' , 'GT' , 'LSG' , 'KKR' , 'SRH' , 'DC']

for lst1 in range(len(lst)):
    for lst2 in range(len(lst)):
        if lst1 != lst2:
            print(f"{lst[lst1]} vs {lst[lst2]}")