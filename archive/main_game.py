#!/usr/bin/env python
# coding: utf-8

import difflib
import hangman
import random
from random import randint
import games
from speech import sayit



yes = ["yes", "sure", "fine", "all right", "Y", "y", "yeah", "affirmative", "true", "yep", "ok", "okay", "why not", "alright"]




#Remember to put a while loop at the begining of the code of the game for this def to work 
def PlayAgain(game, input_method=input):
    global yes
    while 1:
        game(input_method=input_method)
        sayit("do you want to play again?")
        answer = input_method()

        if answer in yes:
            continue
            
        else:
            break

import hangman

def ChooseGame(input_method=input):
    sayit("Hello")
    quit_choices = ("quit", "exit", "i'm done", "bye")
    game_choices = {('rock paper scissors', 'rps', 'rock', 'paper','scissors'):games.ropapsic, 
            ('hangman','hang man'):hangman.game_hang, 
            ('memory game',):games.memoryGame
        }
    while 1:
        sayit("Choose a game: Rock paper scissors, Hangman, Memory game or quit.")

        choiceGame = input_method()
        if difflib.get_close_matches(choiceGame.lower(), quit_choices):
            return
        for key,value in game_choices.items():
            if difflib.get_close_matches(choiceGame.lower(), key):
                PlayAgain(value, input_method=input_method)
                break
        else:
            sayit("Sorry, I didn't understand the game you wanted to play")



if __name__=="__main__":
    ChooseGame()

