#!/usr/bin/env python3

import os
import random

# here we are picking a random number between 1,10
magic_number = random.randint(1,10)

# setting initial guess
guess = 500

# how many guesses the player made so far
num_guesses = 0
guesses = []

os.system('say -v Samantha "please tell me your name"')
player = input("please tell me your name: ")

# here we start our main loop for our program
while not int(guess) == magic_number:

    # check number of guesses
    if num_guesses == 1:
        t = "try"
    else:
        t = "tries"

    # asking the player to please pick a number
    os.system('say "{0}, I have chosen a number between 1 and 10. Please try to guess it.  So far you have guessed {1} {2}."'.format(player, num_guesses, t))
    guess = input("I have chosen a number between 1-10, please try to guess it: ")

    # check the guess to make sure it is valid
    try:
        int(guess)
    except ValueError:
        os.system('say "{0}. {1} is not a valid number between 1 and 10.  Please try again"'.format(player, guess))
        guess = 500
        continue
    if int(guess) > 10 or int(guess) < 1:
        os.system('say "{0}. {1} is not a valid number between 1 and 10.  Please try again"'.format(player, int(guess)))
        guess = 500
        continue

    # add 1 to the number of guesses
    num_guesses += 1
    guesses.append(guess)

    if int(guess) == magic_number:
        if num_guesses == 1:
            t = "try"
        else:
            t = "tries"
        os.system('say -v Samantha "congratulations {0}, you guessed it in {1} {2}"'.format(player, num_guesses, t))
        print("congrats {0}, you guessed it in {1} tries".format(player,num_guesses))

    elif int(guess) > magic_number:
        os.system('say -v Samantha "Awwwwwwww poopies {0}, too high. Guess a lower number please!"'.format(player))
        print("Awwwwwwww poopies, too high! guess a lower number please!")

    elif int(guess) < magic_number:
        os.system('say -v Samantha "Awwwwwwww poopies {0}, too low. Guess a higher number please!"'.format(player))
        print("Awwwwwwww poopies, too low! guess a higher number please!")
