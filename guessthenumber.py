#!/usr/bin/env python3

import random

magic_number = random.randint(1,11)

guess = 500

num_guesses = 0

player = input("plaese tell me your name: ")

while not int(guess) == magic_number:

    guess = input("I have chosen a number between 1-10, please try to guess it: ")

    num_guesses += 1

    if int(guess) == magic_number:
        print("congrats {0}, you guessed it in {1} tries".format(player,num_guesses))
    else:
        print("Sorry, you did not guess correctly!")
