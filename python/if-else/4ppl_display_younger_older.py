age1 = int(input("Enter age Person 1: "))
age2 = int(input("Enter age Person 2: "))
age3 = int(input("Enter age Person 3: "))
age4= int(input("Enter age Person 4: "))

if age1 > age2 and age1 > age3:     
    print('Person 1 is the oldest')     
    if age2 < age3:        
        print('Person 2 is the youngest')     
    else:         
        print('Person 3 is the youngest') 
if age2 > age1 and age2 > age3:    
    print('Person 2 is the oldest')     
    if age1 < age3:         
        print('Person 1 is the youngest')     
    else:         
        print('Person 3 is the youngest') 
if age3 > age1 and age3 > age2:      
    print('Person 3 is the oldest')      
    if age1 < age2:         
        print('Person 1 is the youngest')      
    else:         
        print('Person 2 is the youngest')

