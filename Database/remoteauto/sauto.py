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


def connectan():
    speak("Fron Who should I Connect?")
    query = takeCommand().lower()
    if 'chhota' in query:
        click(x=0, y=1079)
        write("remote Desktop Connection")
        sleep(1)
        click(x=862, y=523)
        sleep(1)
        click(x=966, y=316)
        sleep(1)
        press_and_release('ctrl + a')
        sleep(1)
        write('192.168.1.6')
        sleep(1)
        click(x=1063, y=471)
        sleep(1)
        write('ANSHIKA')
        press('enter')
        sleep(1)
        click(x=1031, y=498)
    else:
        a = input("Enter Ip Address?")
        b = input("Enter Acount Name?")
        c = input("Enter Password?")

        click(x=0, y=1079)
        write("remote Desktop Connection")
        sleep(1)
        click(x=862, y=523)
        sleep(1)
        click(x=966, y=316)
        sleep(1)
        press_and_release('ctrl + a')
        sleep(1)
        write(a)
        press('enter')
        sleep(1)
        click(x=806, y=415)
        sleep(1)
        click(x=877, y=605)
        sleep(1)
        click(x=989, y=284)
        sleep(1)
        write(b)
        sleep(1)
        click(x=909, y=336)
        sleep(1)
        write(c)
        sleep(1)
        click(x=895, y=666)
        sleep(1)
        press('enter')
        sleep(1)
        click(x=1031, y=498)
