file2 = open("../PYTHON/file_handling/demo4.txt","w")
file2.close()

file2 = open("../PYTHON/file_handling/demo4.txt","a")
file2.write("hello om")
file2.close()

file2 = open("../PYTHON/file_handling/demo4.txt","r+")  #tema navi file create na thay, te file ne read &write kare.
file2.write("how are you?")
file2.seek(0)     #pointer ne 0 upar lai jase, jo aa na lakhiye to last ma je write karyu hoy tyathi read kare.
# print(file2.tell()) #pointer ni location return kare
r = file2.read()
print(r)
file2.close()

file3 = open("../PYTHON/file_handling/demo5.txt","w+") #te file ne write & read kare, te new file pn create kari de.
file3.write("this file is used for learning purpose")
file3.seek(0)
print(file3.read())
file3.close()

file3 = open("../PYTHON/file_handling/demo7.txt","a+")  # a+ for apend and read both 
file3.write("  ...thank you for using file")            # create a new file if no exist
file3.close()
