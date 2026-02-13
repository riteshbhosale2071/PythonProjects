# Dice Roller Game
import random

print("Welcome to the Dice Roller!")
print("Press Enter to roll the dice or type 'q' to quit.")

while True:
    user_input = input("Roll the dice? ")

    if user_input.lower() == 'q':
        print("Thanks for playing!")
        break

    dice_number = random.randint(1, 6)
    print(f"You rolled: {dice_number}\n")