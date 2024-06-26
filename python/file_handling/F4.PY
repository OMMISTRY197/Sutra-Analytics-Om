import os

with open("../PYTHON/file_handling/demo6.txt","w+") as file:
    file.write("this file is of different method")
    file.close()

#rename the file
os.rename("../PYTHON/file_handling/demo6.txt", "../PYTHON/file_handling/hello6.txt") 

#remove the file
os.remove("../PYTHON/hello6.txt")