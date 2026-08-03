import random
from words import words

word = random.choice(words)

guessed_letter = []

lives = 8

while lives>0:
    guess = input("Guess a letter: ").lower()
    if guess == "quit":
        break
    guessed_letter.append(guess)
    word_complete = True

    for letter in word:
        if letter in guessed_letter:
            print(letter, end="")
        else:
            print("_", end="")
            word_complete = False
    print()

    if guess not in word:
        lives -=1
        print(f"Wrong guess ❌ Lives left: {lives}")
    if word_complete:
        print("Congratulation 🔥 You guessed the word!")
        break

    if lives == 0:
        print(f"Your are out of lives 💔, The word was: {word}")