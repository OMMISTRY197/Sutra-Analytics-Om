#Find armstrong number without using inbuilt function.
    
for num in range(0,1001):    
   sum = 0    
   temp = num    
   while temp > 0:    
       digit = temp % 10    
       sum += digit ** 3    
       temp //= 10    
       if num == sum:    
        print(num)