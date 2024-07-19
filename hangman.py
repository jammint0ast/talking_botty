#!/bin/python3
from hangman_helper import nouns, advanced_words, updatedashes
import hangman_helper
import random
from speech import sayit
secret = random.choice(nouns + advanced_words) 
words = ("dogs", "sun", "pizza", "deoxyribonucleic", "university")

dashes = "-" * len(secret)


def game_hang(input_method=input):
    global dashes
    tries = 10
    while tries > 0 :
      sayit("Guess a letter:")
      guess = input_method()
      if len(guess) !=1: 

        sayit ("You must only answer one letter at the time. Try again")
        continue

      elif guess in secret:
        sayit ("Correct")
        dashes = updatedashes(secret, dashes, guess)
        sayit (dashes)
      else:
        sayit ("Incorrect")
        tries -= 1
        sayit ("Tries left: " + str(tries))
      if dashes == secret:
        #sayit ("You won")
        break

    if tries == 0:
      sayit ("You lost, The word was: " + secret)

    else:
      sayit ("You won")
