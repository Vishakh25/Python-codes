import random

def roll_dice():
    return random.randint(1, 6)

print("Welcome to the Dice Game: ")

while True:
    choice = input("\nPress Enter to roll the dice or type 'exit' to quit: ")
    if choice.lower() == 'exit':
        print("Thanks for playing the game: ")
        break
    result = roll_dice()
    print(f"You rolled: {result}")
