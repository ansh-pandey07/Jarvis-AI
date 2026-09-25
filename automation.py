from asyncio import wrap_future
import datetime
from dis import dis
import os
from tokenize import Number
from urllib import request
import webbrowser as web
from winreg import QueryValue
from wsgiref.validate import WriteWrapper
import pyttsx3
import speech_recognition as sr
import geocoder
import requests
from os import startfile
from pyautogui import click
from geopy.distance import great_circle
from geopy.geocoders import  Nominatim
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep

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

def whatsappmsg(name, message):
    startfile("C:\\Users\\admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(20)
    click( x=129, y=104)
    sleep(5)
    write(name)
    sleep(5)
    click(x=188, y=249)
    sleep(5)
    click(x=940, y=994)
    sleep(5)
    write(message)
    press('enter')

def hindiMSG(name, messagehi):

    click(x=1, y=1079)
    sleep(0.5)
    write("whatsapp")
    sleep(0.5)
    click(x=242, y=560)
    sleep(20)
    click( x=129, y=104)
    sleep(2)
    write(name)
    sleep(1)
    click(x=188, y=249)
    sleep(1)
    click(x=940, y=994)
    sleep(1)
    write(messagehi)
    press('enter')

def whatsappcall(name):
    startfile("C:\\Users\\admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(20)
    click(x=129, y=104)
    sleep(5)
    write(name)
    sleep(5)
    click(x=188, y=249)
    sleep(5)
    click(x=1763, y=55)

def whatsappchat(name):
    startfile("C:\\Users\\admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(20)
    click(x=129, y=104)
    sleep(5)
    write(name)
    sleep(5)
    click(x=188, y=249)

def whatsappvideocall(name):
    startfile("C:\\Users\\admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(20)
    click(x=129, y=104)
    sleep(4)
    write(name)
    sleep(4)
    click(x=188, y=249)
    sleep(4)
    click(x=1710, y=57)
    sleep(4)
    click(x=1610, y=865)
    sleep(4)
    click(x=1610, y=865)

def chromeauto(command):

    query = str(command)

    if 'new tab' in query:
        press_and_release('ctrl+t')

    elif 'close tab' in query:
        press_and_release('ctrl+w')

    elif 'new window' in query:
        press_and_release('ctrl + n')

    elif 'history' in query:
        press_and_release('ctrl + h')

    elif 'download' in query:
        press_and_release('ctrl + j')

    elif 'bookmark' in query:
        press_and_release('ctrl + d')

        press('enter')

    elif 'incognito' in query:
        press_and_release('ctrl + shift + n')

    elif 'switch tab' in query:
        tab = query.replace("switch tab", "")
        Tab = tab.replace("to", "")
        num = Tab
        bb = f'ctrl + {num}'
        press_and_release(bb)

    elif 'open' in query:
        name = query.replace("open ", "")
        NameA = str(name)

        if 'youtube' in query:
            web.open("https://www.youtube.com/")

        elif 'instagram' in query:
            web.open("https://www.instagram.com/")

        elif 'facebook' in query:
            web.open("https://www.facebook.com/")

        else:
            string = "https://www." + NameA + ".com"
            string_2 = string.replace(" ", "")
            web.open(string_2)

def YoutubeAuto(command):
    query = str(command)

    if 'pause' in query:
        press('space bar')

    elif 'resume' in query:
        press('space bar')

    elif 'fullscreen' in query:
        press('f')

    elif 'skip' in query:
        press('l')

    elif 'back' in query:
        press('j')

    elif 'increase' in query:
        press_and_release('SHIFT + .')

    elif 'decrease' in query:
        press_and_release('SHIFT + ,')

    elif 'mute' in query:
        press('mute')

    elif 'previous video' in query:
        press_and_release('SHIFT + p')

    elif 'next video' in query:
        press_and_release('SHIFT + n')

    elif 'search' in query:
        click(x=824, y=131)
        speak("What sould I search")
        search = takeCommand().lower()
        write(search)
        sleep(1)
        press('enter')

    elif 'unmute' in query:
        press('m')

    elif 'open youtube' in query:
        web.open('https://www.youtube.com/')

def WindowsAuto(command):
    query = str(command)

    if 'home screen' in query:
        press_and_release('windows + m')

    elif 'minimize' in query:
        press_and_release('windows + m')

    elif 'show start' in query:
        press('windows')

    elif 'open settings' in query:
        press_and_release("windows + iF")

    elif 'open search' in query:
        press_and_release('windows + s')

    elif 'open widject' in query:
        press_and_release('window + h')

    elif 'restore windows' in query:
        press_and_release('windows + Shift + M')

    elif 'change new scree' in query:
        press_and_release("ctrl+windows+d")

def onlineClass (subject):
    speak("Joining The Class Sir")
    if 'science' in subject:
        from Database.OnlineClases.links import science
        Link = science()
        web.open(Link)
        sleep(10)
        click(x=682, y=714)
        sleep(1)
        click(x=765, y=717)
        sleep(1)
        click(x=1280, y=591)
        speak("Class Joined Sir.")

    elif 'maths' in subject:
        from Database.OnlineClases.links import maths
        Link = maths()
        web.open(Link)
        sleep(10)
        click(x=682, y=714)
        sleep(1)
        click(x=765, y=717)
        sleep(1)
        click(x=1280, y=591)
        speak("Class Joined Sir.")

    elif 'hindi' in subject:
        from Database.OnlineClases.links import hindi
        Link = hindi()
        web.open(Link)
        sleep(10)
        click(x=682, y=714)
        sleep(1)
        click(x=765, y=717)
        sleep(1)
        click(x=1280, y=591)
        speak("Class Joined Sir.")

    elif 'english' in subject:
        from Database.OnlineClases.links import english
        Link = english()
        web.open(Link)
        sleep(10)
        click(x=682, y=714)
        sleep(1)
        click(x=765, y=717)
        sleep(1)
        click(x=1280, y=591)
        speak("Class Joined Sir.")


    elif 'coding' in subject:
        from Database.OnlineClases.links import codingclass
        Link = codingclass()
        web.open(Link)
        sleep(10)
        click(x=682, y=714)
        sleep(1)
        click(x=765, y=717)
        sleep(1)
        click(x=1280, y=591)
        speak("Class Joined Sir.")

    elif 'sanskrit' in subject:
        from Database.OnlineClases.links import sanskrit
        Link = sanskrit()
        web.open(Link)
        sleep(10)
        click(x=682, y=714)
        sleep(1)
        click(x=765, y=717)
        sleep(1)
        click(x=1280, y=591)
        speak("Class Joined Sir.")

    elif 'social' in subject:
        from Database.OnlineClases.links import SST
        Link = SST()
        web.open(Link)
        sleep(10)
        click(x=682, y=714)
        sleep(1)
        click(x=765, y=717)
        sleep(1)
        click(x=1280, y=591)
        speak("Class Joined Sir.")

    elif 'computer' in subject:
        from Database.OnlineClases.links import computer
        Link = computer()
        web.open(Link)
        sleep(10)
        click(x=682, y=714)
        sleep(1)
        click(x=765, y=717)
        sleep(1)
        click(x=1280, y=591)
        speak("Class Joined Sir.")

    elif 'ctp' in subject:
        from Database.OnlineClases.links import ctp
        Link = ctp()
        web.open(Link)
        sleep(10)
        click(x=682, y=714)
        sleep(1)
        click(x=765, y=717)
        sleep(1)
        click(x=1280, y=591)
        speak("Class Joined Sir.")

def notepadAuto():

    speak('Tell Me The Query')
    speak('I am ready to write')
    writes = takeCommand()
    time = datetime.datetime.now().strftime("%H:M")
    filename = str(time).replace(":","-") + '-note.txt'
    with open(filename, 'w') as file:
        file.write(writes)

    path_1 = "D:\\Ansh Coder Jarvis\\Jarvis\\Jarvis\\" + str(filename)
    path_2 = "D:\\Ansh Coder Jarvis\\Jarvis\\Jarvis\\Database\\NotePad\\" + str(filename)
    path_2 = "D:\\Ansh Coder Jarvis\\Jarvis\\Jarvis\\Database\\NotePad\\" + str(filename)

    os.rename(path_1, path_2)
    os.startfile(path_2)

def closeNotepad():
    os.system("TASKKILL /F /im Notepad.exe")

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)
    goelocator = Nominatim(user_agent="myGeoCoder")
    location = goelocator.geocode(Place, addressdetails=True)
    target_latlon = location.latitude, location.longitude
    location = location.raw['address']
    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_loca = geocoder.ip('me')
    current_latlon = current_loca.latlng
    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ', 1)[0])
    distance = round(float(distance),2)
    
    web.open(url=Url_Place)
    speak(target)
    speak(f"Sir, {Place} is {distance} kilometer away from your location.")

def newGroup():
    startfile("C:\\Users\\admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(20)
    click(x=533, y=50)
    sleep(0.5)
    click(x=477, y=103)
    speak("Sir Please Tell Me Name Of The People To Invite In Group")
    player = input("Name of the poeple:")
    sleep(4)
    write(player)
    sleep(0.5)
    click(x=213, y=256)
    sleep(0.5)
    click(x=288, y=980)
    speak("Sir Would you want the photo In the Group")
    photo = takeCommand().lower()
    if 'yes' in photo:
        click(x=283, y=242)
        start = takeCommand().lower()
        if 'take photo' in start:
            click(x=379, y=296)

        elif 'upload' in start:
            click(x=379, y=296)

        elif 'web' in start:
            click(x=404, y=365)

    speak("Sir Please Tell Me Name Of The Group")
    name = takeCommand().lower()
    write(name)
    click(x=283, y=653)

def calls():

    speak('Sir Please Write The Number')

    saf = input("Tell Me The Number: ")
    click(x=904, y=347354399000)
    click(x=768, y=1046)
    write("phone")
    press('enter')
    sleep(5)
    click(x=487, y=444)
    write(saf)
    sleep(1)
    click(x=1326, y=696)
    speak("Enjoy Sir")

def inereset():
    speak("Sir Please tell me the market for search")
    mar = input("Write the market: ")
    os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    sleep(5)
    click(x=1095, y=636)
    sleep(1)
    click(x=826, y=61)
    sleep(1)
    write("https://www.moneycontrol.com/")
    sleep(1)
    press('enter')
    sleep(10)
    click(x=1064, y=174)
    sleep(2)
    click(x=833, y=111)
    write(mar)
    sleep(1.5)
    click(x=833, y=111)
    sleep(5)
    click(x=963, y=198)
    sleep(5)
    speak("Sir Please Select the Name Because I don't have this feature")    
    sleep(5)
    press_and_release("ctrl + c")
    speak("Sir I haved Copy")
    sleep(5)
    speak("Sir Please Select the Because I don't have this feature")    
    sleep(2)
    sleep(2)
    press_and_release("ctrl + c")
    speak("Sir I haved Copy")
    sleep(1)
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")
