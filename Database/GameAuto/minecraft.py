from re import X
from ssl import SSL_ERROR_EOF
import pyttsx3
import speech_recognition as sr
import pyautogui
from time import sleep
from keyboard import press_and_release
from keyboard import press
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


def mine():
    click(x=798, y=1060)
    sleep(1)
    write("tlauncher")
    sleep(1)
    press("enter")
    sleep(20)
    click(x=1066, y=824)
    speak("Program lanching sir")
    sleep(25)
    speak("The Game has started")
    sleep(1)
    speak("Sir what do you want to play")
    snormu = takeCommand().lower()
    if 'single player' in snormu:
        speak("launching single player sir")
        click(x=925, y=498)
        speak("Do you want a new world")
        wo = takeCommand().lower()
        if 'yes' in wo:
            
            click(x=1273, y=924)
            sleep(1)
            click(x=950, y=275)
            sleep(1)
            press_and_release('ctrl + a')
            sleep(0.5)
            speak("What is the Name Of the New world ?")
            new = takeCommand().lower()
            write(new)
            sleep(0.5)
            speak("Sir Do You want survival mod or Creative mod ?")
            creorsur = takeCommand().lower()
            if 'creative' in creorsur:
                click(x=706, y=457)
                click(x=706, y=457)
                speak("done sir")
                click(x=715, y=1002)
            else:
                click(x=715, y=1002)

        else:
            click(x=515, y=278)

    elif 'multiplayer' in snormu:
        click(x=436, y=206)