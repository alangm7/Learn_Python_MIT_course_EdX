"""The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
"""

from random import randint

number = input('Please think w number between 0 and 100: ')

print ('Is your secret number ' + str(randint(0,100)))

print ("Enter 'h' to indicate the guess is too hight. Enter 'l' to indicate the guess is low. Enter 'c' to indicate I guessed correctly.) + str(number)")
