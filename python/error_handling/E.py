# try: 
#     raise SyntaxError ("Hii")
# except NameError:
#     print ("An exception")
#     raise
# except SyntaxError:
#     print ("Su kare che laaa")
    

   
a = [1, 2, 3]
try: 
    print("Second element = ",a[1])
    print("Fourth element = ",a[3])
    # raise IndexError("Heloo")
except IndexError:
    print ("An error occurred")
    # raise
except SyntaxError:
    print("Hii Smarty")
finally:
    print('This is always executed')