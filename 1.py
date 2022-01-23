# number guessing
from random import *
guess = 0
# define a number
computernum = randint(1, 1000)
# game loop
while (guess != computernum):
    #read number
    guess = int(input("Guess a number:"))
    #evaluate number
    if guess == computernum:
        print("Correct!")
    elif guess < computernum:
        print("guess too low")
    elif guess > computernum:
        print("guess too high")