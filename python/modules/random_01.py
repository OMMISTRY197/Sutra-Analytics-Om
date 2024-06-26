import random
                        #random.random()
print(random.random())  #return any value between 0 to 1.

list1 = [1, 2, 3, 4, 5, 6]    #random.choice()
print(random.choice(list1))   #return any value from the list,string or tuple.
string = "om_mistry"
print(random.choice(string))
tuple1 = (1, 2, 3, 4, 5)
print(random.choice(tuple1))

list1 = [1, 2, 3, 4, 5]        #random.sample(sequence,length)
print(random.sample(list1,3))  #return any value from the list,string or tuple.
list2 = (4, 5, 6, 7, 8)
print(random.sample(list2,4))
list3 = "45678"
print(random.sample(list3,3))

sample_list = [1, 2, 3, 4, 5]    #random.shuffle(sequence,function)
print("Original list : ")        #Shuffling means changing the position of the elements of the sequence.
print(sample_list)
random.shuffle(sample_list)
print("After the first shuffle: ")
print(sample_list)
random.shuffle(sample_list)
print("After the second shuffle: ")
print(sample_list) 

print(random.randint(5, 15))     #random.randint(start,end)
print(random.randint(-10, -2))   #used to generate random integers between the given range.

print(random.randrange(100,200))  #random.randrange(start,stop,step)
print(random.randrange(100))      #start Optional. An integer specifying at which position to start. Default 0
print(random.randrange(10,20,2))  #stop	Required. An integer specifying at which position to end.
                                  #step	Optional. An integer specifying the incrementation. Default 1

random.seed(3)                    #random.seed(num)
print(random.randint(1, 1000))    #it can generate same random numbers on multiple executions of the code
random.seed(3)
print(random.randint(1, 1000))