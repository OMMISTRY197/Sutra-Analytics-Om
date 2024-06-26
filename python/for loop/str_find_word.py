# Take one string in static or take input and find where is the word in string 
# which is input by user if they dont match then retake until not match

# string1 = str(input("enter a word: ")).lower()
# string2 = "hello"

# if string1 == string2:
#     print("words matched")
# else:
#     print("words are not matched")

string1 = "hello"

for i in string1:
    user_input = str(input("enter a word: ")).lower()
    if user_input == string1:
        print("words matched")
    else:
        print("words are not matched")