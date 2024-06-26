# Display the largest and smallest value from 3 values

def compare():
    if num1>num2 and num1>num3:
        print("num 1 is greater")
        if num2<num3:
            print("num 2 is smaller")
        else:
            print("num 3 is smaller")
    if num2>num1 and num2>num3:    
        print("num 2 is greater")     
        if num1<num3:         
            print('num 1 is smaller')     
        else:         
            print('num 3 is smaller') 
    if num3>num1 and num3>num2:      
        print('num 3 is greater')      
        if num1<num2:         
            print('num 1 is smaller')      
        else:         
            print('num 2 is smaller')

num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
num3 = int(input("enter number 3: ")) 
compare()