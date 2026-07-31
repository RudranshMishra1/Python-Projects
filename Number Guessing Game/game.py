import random

num = random.randint(1,100)
attempts = 0

while True:
    attempts +=1
    try:
        user = int(input("Guess a number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if num == user:
        print("Congratulations⭐, You guessed the number.")
        print(f"You guessed it in {attempts} attempts!")
        break

    elif num>user:
        print("Your guess is lower than the number: ")

    elif num<user:
        print("Your guess is higher than the number: ")