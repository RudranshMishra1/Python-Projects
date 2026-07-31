'''
rock, paper  = paper
scissor,paper = scissor
rock,scissor = rock
1 = rock
2 = paper
3 = scissor
'''

import random

choices = ["scissor", "paper", "rock"]
print("Thank you for visiting this game, type Exit to end the program")

while True:


    ai = random.choice(choices)
    user = input("Chosse rock, paper or scissor: ")

    if ai == "scissor" and user == "rock":
        print("Congratulations🎉, you won")
        print(f"Computer choosed {ai}")

    elif ai == "rock" and user == "paper":
        print("Congratulations🎉, you won")
        print(f"Computer choosed {ai}")

    elif ai == "paper" and user == "scissor":
        print("Congratulations🎉, you won")
        print(f"Computer choosed {ai}")

    if user == "scissor" and ai == "rock":
        print("You lost🙁, Computer wins")
        print(f"Computer choosed {ai}")

    elif user == "rock" and ai == "paper":
        print("You lost🙁, Computer wins")
        print(f"Computer choosed {ai}")

    elif user == "paper" and ai == "scissor":
        print("You lost🙁, Computer wins")
        print(f"Computer choosed {ai}")

    elif user == ai:
        print("It's a draw!")

    elif user == "exit":
        print("Thanks for playing.")
        break