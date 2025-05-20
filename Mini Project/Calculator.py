import random

sect_num = random.randint(1, 100)

attempts = 0
print("Welcome to the Number Guessing Game")
print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < sect_num:
        print("Too low. Try again!")
    elif guess > sect_num:
        print("Too high. Try again!")
    else:
        print(f"Correct! The number was {sect_num}.")
        print(f"You guessed it in {attempts} attempts.")
        break
