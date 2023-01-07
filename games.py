import random
import time
from speech import sayit
import turtle
name = ["face.gif", "shiba.gif", "pikachu.gif", "orango.gif"]
op = ["rock", "paper", "scissors"]
score = 0
Computerscore = 0

from turtle import Screen, Turtle
from random import randint

screen = Screen()
screen.setup(500, 500)

def gotorandom(t): 
  x = randint(-180, 180)
  y = randint(-180, 180)
  t.goto(x,y)

def newturtle(image): 
  t = Turtle()
  screen.addshape("gameassets/"+image)
  t.shape("gameassets/"+image)
  t.penup()
  return t

turtles = []
def ropapsic():
 global score, Computerscore

 sayit("Chose one, rock, paper , scissors")

 text = input()

 bot = random.choice(op)


 sayit("The computer chose " + bot)


 outcome = [text, bot]

 playerwins = [["rock", "scissors"],["scissors", "paper"],["paper", "rock"]]

 if outcome in playerwins:
     sayit("You won")
     score += 1
     sayit("Your score: " + str(score))
     sayit("Computer's score: " + str(Computerscore))


 elif text == bot:
     sayit("You tied")
     sayit("Your score: " + str(score))
     sayit("Computer's score: " + str(Computerscore))

 else:
     sayit("Computer wins")
     Computerscore += 1
     sayit("your score: " + str(score))
     sayit("Computer's score: " + str(Computerscore))
    
    
    
def hangman():
    sayit("coming soon")
    
    
def memoryGame():
    for i in range (10):
      img = random.choice (name)
      t = newturtle(img)
      turtles.append(t)
      t.speed(10)
      t.left(90)
      gotorandom(t)


    time.sleep(2)
    t = random.choice(turtles)
    t.hideturtle()
    missing = t.shape()

    sayit("Which one went missing?")
    sayit(name)

    answer = input()

    if answer == missing:
      sayit("You got it!")

    else:
      sayit("wrong, it was " + missing)
    
    
    