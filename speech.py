import pyttsx3
engine = pyttsx3.init()

def sayit(str):
    print(str)
    engine.say(str)
    engine.runAndWait()