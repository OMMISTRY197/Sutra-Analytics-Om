# "Take a list of atleast 7 colours and print them like this :
# Blue
# B
# L
# U
# E"

colors = ["Blue", "Red", "Green", "Yellow", "Orange", "Purple", "Pink"]

for color in colors:
    print(color)
    for letter in color:
        print(letter.upper())
    
