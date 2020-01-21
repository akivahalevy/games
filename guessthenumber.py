#!/usr/bin/env python3

import random

# here we are picking a random number between 1,10
magic_number = random.randint(1,11)

# setting initial guess
guess = 500

# how many guesses the palyer made so far
num_guesses = 0

player = input("plaese tell me your name: ")

# here we start our main loop for our program
while not int(guess) == magic_number:

    # asking the player to plaese pick a number
    guess = input("I have chosen a number between 1-10, please try to guess it: ")

    # add 1 to the number of guesses
    num_guesses += 1

    if int(guess) == magic_number:
        print("congrats {0}, you guessed it in {1} tries".format(player,num_guesses))

    elif int(guess) > magic_number:
        print("Sorry, too high! guess a lower number please!")

    elif int(guess) < magic_number:
        print("Sorry, too low! guess a higher number please!")