# "Take a list of atleast 7 colours and print them like this :
# Blue
# B
# L
# U
# E"

colors = ["blue", "red", "yellow", "green", "white", "pink", "purple"]

for col in colors:
    print(col)
    for letter in col:
        print(letter)