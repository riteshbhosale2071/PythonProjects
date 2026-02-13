# Rock, Paper, Scissor game
import random

options = ["rock", "paper", "scissors"]
computer = random.choice(options)

user = input("rock/paper/scissors: ")

if user == computer:
    print("Draw")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win")
else:
    print("You lose. Computer win", computer)