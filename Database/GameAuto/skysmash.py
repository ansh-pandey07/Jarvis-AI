import pyttsx3
import speech_recognition as sr
from time import sleep
from keyboard import write
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

def start():
    click(x=815, y=1058)
    write("Bluestack")
    sleep(1)
    click(x=862, y=523)
    sleep(15)
    click(x=1602, y=119)
    sleep(1)
    click(x=256, y=434)
    speak("Game Has started sir")

def shutdown():
    sleep(1)
    click(x=1865, y=17)
    sleep(0.1)
    click(x=1087, y=538)
    speak("Game Has dissmiss sir")
