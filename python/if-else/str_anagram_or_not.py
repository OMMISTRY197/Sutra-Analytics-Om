#Write a program to check two words are anagrams or not

str1 = "Race"
str2 = "Care"

if(len(str1) == len(str2)):
    
    if(str1 == str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")
else:
    print(str1 + " and " + str2 + " are not anagram.")