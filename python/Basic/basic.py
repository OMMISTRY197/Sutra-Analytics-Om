'''print("hello world")

a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a%b)'''

#find reminder when number is divisible by 2

'''num = int(input("enetr number: "))
if(num %2==0):
    print("number is divisible by 2")
else:
    print("number is not divisible by 2")'''

#find the average of two numbers entered by the user.

'''a=int(input("enter first value:"))
b=int(input("enter first value:"))
avg = (a + b)/2
print("average value is: %0.2f" %avg)'''

#calculate cube of a number entered by the user.

'''a=int(input("enter first value:"))
cube=a*a*a
print("The Cube of a Given Number {0}  = {1}".format(a, cube))'''

#Check the type of the variables assigned using input() function.

'''num = int(input("enter value:"))
print(type(num))'''

#Check the length of a string entered by the user.

'''string = input("enter string:")
print(len(string))'''

#Display the last digit from the value entered by user

'''number = int(input("Enter any Number: "))
last_digit = number % 10
print("The last digit in a given number %d = %d" %(number, last_digit))'''

#Write a program to count the number of words in the given string.

'''str = "ommistry"
print(str.count("m"))'''

#Write a program to display the length of the given string.

'''str = "ommistry"
print(len(str))'''

#Write a program to accept marks of 6 students and display them in a sorted manner

'''s1 = int(input("Marks of 1st student : "))
s2 = int(input("Marks of 2nd student : "))
s3 = int(input("Marks of 3rd student : "))
s4 = int(input("Marks of 4th student : "))
s5 = int(input("Marks of 5th student : "))
s6 = int(input("Marks of 6th student : "))
SortedMarks = [s1, s2, s3, s4, s5, s6]
SortedMarks.sort()
print(SortedMarks)'''

#Write a program to split a string into a list of words.

'''str = "hello om mistry"
print(str.split())'''

#Write a program to display a string from the user and display it in the upper case and take other string and display it in lowercase.

'''str = "Hello Om Mistry"
print(str)
print(str.lower())
print(str.upper())'''

#Display the string accepted from the user in title case.

'''str = "om mistry"
print(str.title())'''

#Write a program to generate quotient and reminder of two numbers division.

'''q, r = divmod(10, 3)
print("Quotient: ", q)
print("Remainder: ", r)'''
 
#Write a program to calculate square of a number entered by the user.

'''a=7
square = a*a
print(square)'''

# Accept strings from the users and concate them.

'''str1 = "Hello"
str2 = "Om"
str3 = str1 + str2
print(str3)'''

#Write a program to replace a string accepted from the user.

'''str = "my hobby is playing cricket"
print(str.replace("cricket" , "carrom"))'''

#Write a program to format a string using the format() method.

'''name = "Om"
age = 17
message = "My name is {0} and I am {1} years old".format(name, age)
print(message)'''

#Calculate the length of the string accepted by the user.   text = input("Enter a string: ")

'''str = input("enter a string:")
print(len(str))'''

#Write a program to detect double spaces and remove in a string.

'''str = "This  is  a     simple       string"
str = ' '.join( str.split())
print(str)'''

#Write a program to display a user entered name followed by Good Afternoon using input() function.

'''str = str(input("enter value"))
print("Good Afternoon",str)'''

# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

'''fname = input("enter your first name :")
lname = input("enter your last name :")
print("Hello " + lname + " " + fname)'''

#STRING:   hello!this is internship by sutra analytics.Write a program to display the given string in title case.(first alphabet of each word should be in uppercase.)

'''str = "hello! this is internship by sutra analytics."
print(str.title())'''

# Write a program to remove leading(from the beginning) and trailing(at the end) whitespace from a string accpeted by the user.

'''str = '\tHi, how are you?\n '
print(str)
new_str = str.strip()
print(new_str) '''

#Write a program to fill   in a letter template given below with name and date.

# letter = '''Dear <|NAME|>,You are selected!
# Date: <|DATE|> '''
# name = input("Enter Your Name")
# date = input("Enter Date")
# letter = letter.replace("<|NAME|>", name)
# letter = letter.replace("<|DATE|>", date)
# print(letter)

#Write the program to calculate and display the total amount payable by Ananya:Ananya purchased 5 pencils and 2 erasers at the cost of Rs 7 and Rs 5 respectively.

'''pencil=5
pencil_price=7
pencil_total=pencil*pencil_price
eraser=2
eraser_price=5
eraser_total=eraser*eraser_price
print(pencil_total + eraser_total)'''

#Write the output of the following:a)>>>(2**5)

'''power = 2**5
print(power)'''

#Write a program that analyzes a text document, counting the number of words, sentences, and characters without using functions.

'''doc = "hello, how are you? i'm good. what about you?.txt"
print(doc.count('e'))
print(doc.split())
sentence = doc.count('.') + doc.count(',') + doc.count('?')
print(sentence)'''

#split string

'''a = "hello world"
print(a.split(" "))'''

#multiline string

'''a = """hi
how
are
you!"""
print(a)'''

#looping through a string
 
'''for x in "banana":
    print(x)'''

#string length

'''a = "hello"
print(len(a))'''

#string checking

'''a = "hello i am om"
print("am" in a)
print("aryan" not in a)
if "am" in a :
    print("yes")'''

#string slicing

'''a = "hello om mistry"
print(a[2:5])
print(a[2:10:2])

b = "Hello,World!"
print(b[:5])
print(b[6:])
print(b[-5:-2])'''

#capitalize,casefold

'''a = "hello, My Name Is Om Mistry"
print(a.capitalize())
print(a.casefold())'''


#center

'''a = "hello, My Name Is Om Mistry"
print(a.center(100))'''

#find , index

'''a = "hello,welcome to the world"
print(a.find("w"))
print(a.index("w"))'''

#format

'''fname = "om"
age = 17
txt1 = f"my name is {fname} and age is {age}".format(fname="om",age=17)              #named indexes
txt2 = "my name is {0} and age is {1}".format("om",17)                               #numbetred indexes
txt3 = "my name is {} and age is {}".format("om",17)                                 #empty placeholders
print(txt1)
print(txt2)
print(txt3)'''

#formatmaps

'''a = "Ommistry12"
print(a.isalnum())
print(a.isalpha())
print(a.isascii())
b = "12345000"
# print(b.isdigit())
print(b.isdecimal())
c = "hello"
print(c.isidentifier())
d = "Hello Welcome"
print(d.istitle())'''

#join

'''list = ["hello", "om", "how", "are", "you"]
p = " ".join(list)
print(p)'''