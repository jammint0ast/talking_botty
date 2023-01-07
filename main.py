
#!/bin/python3
from turtle import * 
from time import sleep
from random import randint
import random
screen = Screen()
speed(0)
score = 0
computerScore = 0
positive = ["yes", "sure", "fine", "all right", "Y", "y", "yeah", "affirmative", "true", "yep", "ok", "okay", "why not", "alright"]
negative = ["no", "nope", "nah", "N", "n", "negative", "false", ]
op = ["rock", "paper", "scissors"]

import pyttsx3
engine = pyttsx3.init()


def sayit(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def gotorandom(): 
  x = randint(-300, 300)
  y = randint(-200, 200)
  goto(x, y)
def randomstamps(n): 
  for i in range(n): 
    gotorandom()
    stamp()
def Square(size):
  for i in range(4):
    forward (size)
    left(90)
    
def pattern_yeah():
  speed (0)
  for i in range (74):
    Square(100)
    left (5)
def pattern_2(size):
  for i in range(5):
    forward (size)
    left(144)
    
def RokPapSci():
  global score, computerScore
  sayit ("chose one")
  

  
  
  
  for X in op:
    sayit (X)
    
  answer = input()
  
  while answer not in op:
    sayit ("Invalid answer pick one")
    
    answer = input()
   
  bot = random.choice(op)
  
  sayit ("The computer chose " + bot)
  
  outcome = [answer, bot]
  playerWins = [['rock', 'scissors'], ['scissors', 'paper'], ['paper', 'rock']]
  if outcome in playerWins:
    sayit ("You won!")
    score += 1
    sleep(1)
    sayit ("Your score: " +  str(score))
    sayit ("Computer's score: " + str(computerScore))
    
  elif answer == bot:
    sayit ("You tied")
    sleep(1)
    sayit ("Your score: " + str (score))
    sayit ("Computer's score: " + str (computerScore))
    
  else:
    computerScore += 1
    sayit ("Computer wins")
    sayit ("Your score: " + str (score))
    sayit ("Computer's score: " + str (computerScore))
  
  

sayit ("Hello!\nBefore we start talking, please only use lowercases and write single words. Thank you, this will help me understand you")

while 1:
  answer = input()

  if answer in positive:
    sayit ("alright let's move on...")
    
    break
  else:
    sayit ("Please re-read, and answer with 'ok'")
  

sayit("What is your favorite school subject?")

subject = input()


if subject == "math":
  sayit ("Cool, I also like math!")
  
else:
  sayit ("what, you don't like Math? That's a shame.")

sayit ("Alright, what is your age then?")
age = int(input())

if age <= 20:
  sayit ("Pretty young my friend!")

else:
  sayit ("Wow, you're old! :)")
  
sleep(1)

sayit ("Want to hear a joke?")

joke = input()

if joke in positive:
  sayit ("Why did the scarecrow get promoted?")
  
  
  
else:
  sayit ("You're no fun. And humans say AI has no sense of humor!")
  quit()
  
sleep(1)

sayit("She was outstanding in her field!")

sleep(2)

sayit("Was the joke funny?")

answer = input()

if answer in positive:
  sayit ("Do you want to hear another one?")
  
else:
  sayit ("What! I am severly offended")
  quit()
  
answer = input()

if answer in positive:
  sayit ("What do you call a pig that does Karate?")
  
else:
  sayit ("Okay, bye")
  quit()
  
sleep(2)

sayit ("A pork chop!")

sleep(1)
sayit ("Do you want do end the conversation?")
answer = input()





if answer in positive:
  sayit ("Okay, Goodbye")
  quit()
  
elif answer in negative:
  sayit("Well I have nothing for you now...")
  
sleep(2)
sayit("How about you give me a knock knock joke?")

answer = input()

if answer in positive :
  sayit ("Alringht what's the Knock Knock?")
  
else:
  sayit ("Well you're no fun. Bye!")
  quit()

while 1 :

  joke = input()

  if joke == "knock knock":
    sayit("Who's there")
    break
  else:
    sayit ("I don't understand")
  

joke = input()

x = joke

sayit (x + " who?")

x2 = input()

sayit(x2 + ",Ha ha ,ha , ha. very funny my friend!")

sleep(2)

sayit ("Okay, bye")
sleep(1)

sayit ("I'm just kidding, do you want me to draw something?")

answer = input()

if answer in positive:
  sayit ("Alright")
  
else:
  sayit ("C'omon, it's really cool! I'm just gonna show it anyway.")
  
screen.setup (500, 500)

  
screen.bgpic("Background_test_trinket.png")

  

sayit ("I am drawing a pattern")
pattern_yeah()  

sayit ("Is the pattern noice?")

answer = input()

if answer in positive:
  for i in range (9):
    pattern_2(100)
    left(40)
    
else:
  sayit("...")
  sleep(1)
  
sayit("Do you want to play Rock, Paper Scissors?")

answer = input()

if answer in positive:
  RokPapSci()
  
elif answer in negative:
  sayit ("Common, it is really fun")
  RokPapSci()
while 1: 
  sayit ("Do you want to play again?")
  
  answer = input()
  
  
  if answer in positive:
    RokPapSci()
    
  else:
    break


sayit ("Well I'm getting tired of talking about myself\nHow about you give me a hobby you like to do.")

sayit ("""And just make it simple because my commputing isn't that good, for an example: "soccer" or "video games" """)  

answer = input()

if answer in positive:
  sayit("Alright, what's the hobby?")
  
  
else:
  sayit ("Ok bye, I was anyways getting tired of myself")
  quit()   
  
Hobby = input()

sayit ("So, you like " + Hobby + ", well me to!")
sleep(2)
sayit ("Well, I guess it is time to wrap up don't you think?")

warpans = input()

if warpans in positive:
  sayit(" I'm just gonna do a quick review of you from the input that I have collected")
  
elif warpans in negative:
  sayit ("I'm getting tired anyhow so bye-bye!")
  quit()
  

sayit ("Ok so far, your favorite subject is " + subject + " and your age is: " + str(age))
sayit("Bye - Bye")  
quit()
  

  



  
  

  






  
  
  
  

  

  

