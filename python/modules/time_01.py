import time;
  
print(time.time())  ##prints the number of ticks spent since 12 AM, 1st January 1970
print(time.localtime(time.time()))  #returns a time tuple 
print(time.asctime(time.localtime(time.time())))  #returns the formatted time
 
for i in range(0,5):  
    print(i)  
    #Each element will be printed after 2 second  
    time.sleep(2)

