# Number Guessing Game
import random

def play_game():
    print("\nWelcome to Number Guessing Game")

    print("Select Difficulty Level:")
    print("1. Easy (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard (1 - 200)")

    level = input("Enter choice: ")

    if level == '1':
        max_num = 50
    elif level == '2':
        max_num = 100
    elif level == '3':
        max_num = 200
    else:
        print("Invalid choice! Default set to Medium.")
        max_num = 100

    secret = random.randint(1, max_num)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess number (1-{max_num}): "))
            attempts += 1

            if guess == secret:
                print(f"Correct! You guessed in {attempts} attempts.")
                break
            elif guess > secret:
                print("Too High!")
            else:
                print("Too Low!")

        except ValueError:
            print("Please enter a valid number.")

while True:
    play_game()
    again = input("\nDo you want to play again? (y/n): ")
    if again.lower() != 'y':
        print("Thanks for playing")
        break