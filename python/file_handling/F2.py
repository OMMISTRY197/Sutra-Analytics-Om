file = open('../PYTHON/file_handling/demo1.txt','w')  #file creating and writing
file.write("this is demo 1 file..")
file.close()

file = open('../PYTHON/file_handling/demo1.txt','a')  #append in existing file
file.write("this is append method")
file.close()

file = open('../PYTHON/file_handling/demo1.txt','r')  #read the file
print(file.read())

file1 = open("../PYTHON/file_handling/demo3.txt","w")
file1.write("this is demo 2 file.......")
file1.close()

file1 = open("../PYTHON/file_handling/demo2.txt","x")  #only file creating
file1.close()

import os
os.remove("../PYTHON/file_handling/demo2.txt") #file deleting method1

if os.path.exists("../PYTHON/file_handling/demo2.txt"): #file deleting method2
  os.remove("../PYTHON/file_handling/demo2.txt")
else:
  print("The file does not exist")

os.rmdir("myfolder")  #You can only remove empty folders.