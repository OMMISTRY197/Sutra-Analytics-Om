import random

r_p_s = ['Rock','Paper','Scissors']
computer = c = 0
player = p = 0

while True:
    computer_choice = random.choice(r_p_s)
    player = input("\nRock, Paper, Scissors (Q for quit): ").capitalize()

    if player.upper() == 'Q':
        print("Final Score: Computer = " + str(c) + " & player = " + str(p))
        if p > c:
            print("Player is won the game")
        elif p == c:
            print("Score Tied")
        elif p < c:
            print("Computer is won the game")
        break

    elif player == computer_choice:
        print("Result: Tie")

    elif player == 'Rock':
        if computer_choice == 'Scissors':
            print("Result: Player Won")
            p += 1
        else:
            print("Result: Computer Won")
            c += 1

    elif player == 'Paper':
        if player == 'Rock':
            print("Result: Player Won")
            p += 1
        else:
            print("Result: Computer Won")
            c += 1

    elif player == 'Scissors':
        if computer_choice == 'Paper':
            print("Result: Player Won")
            p += 1
        else:
            print("Result: Computer Won")
            c += 1

    else:
        print("'Rock, Paper & Scissors only!!")
        # break

    print("Player: " +player)
    print("Computer: " + computer_choice)
