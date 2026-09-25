import pyttsx3
from time import sleep
import speech_recognition as sr
from keyboard import write
from keyboard import press_and_release
from keyboard import press
from pyautogui import click

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(": Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f": User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def alef():
    click(x=805, y=1059)
    sleep(1)
    write("Alexa")
    sleep(1)
    press("Enter")
    sleep(15)
    click(x=399, y=110)

def alefs():
    click(x=399, y=110)
alef()