#!/usr/bin/python

import random

magic_number = random.randint(1,21)

guess = 500

while not int(guess) == magic_number:

    guess = input("I have chosen a number between 1-20, please try to guess it: ")

    if int(guess) == magic_number:
        print("You guessed it!")
    else:
        print("Sorry, you did not guess correctly!")
