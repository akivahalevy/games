#!/usr/bin/python

magic_number = 5

guess = input("I have chosen a number between 1-10, please try to guess it: ")

if int(guess) == magic_number:
    print("You guessed it!")
else:
    print("Sorry, you did not guess correctly!")
