#Check whether the entered string is palindrome or not

str = input(("Enter a string:"))  
if(str==str[::-1]):  
      print("The string is a palindrome")  
else:  
      print("The string is not a palindrome")  