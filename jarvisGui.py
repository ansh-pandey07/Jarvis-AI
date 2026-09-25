import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
from http import client
from re import M
import time
from more_itertools import take
import pywhatkit
import cv2
import instaloader
import matplotlib.pyplot as plt
import cv2
import numpy as np
import datetime
import sys
from googletrans import Translator
import wikipedia #pip install wikipedia
import webbrowser
import urllib.request
import webbrowser as web
import bs4
import os
import pyautogui
from win10toast import ToastNotifier
import wolframalpha
import smtplib
import requests
import phonenumbers
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from pywikihow import search_wikihow 
from jarvisUi import Ui_MainWindow
from keyboard import write
from gtts import gTTS
from googletrans import Translator
from keyboard import press_and_release
from pyautogui import click
from bs4 import BeautifulSoup
from phonenumbers import carrier
from time import sleep
from keyboard import press
from phonenumbers import geocoder
from pywikihow import RandomHowTo, search_wikihow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from Database.GuiProgram.SpeedTestUi import Ui_SpeedTest
from PyQt5.uic import loadUiType

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

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="YOUR_API_HERE"'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")



def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=942,y=59)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important

    def Download(link):


        url = YouTube(link)
        video = url.streams.first()


        video.download('D:\\Python\\Jarvis\\Database\\Youtube')


    Download(Link)


    speak("Done Sir , I Have Downloaded The Video .")

    speak("You Can Go And Check It Out.")


    os.startfile('D:\\Python\\Jarvis\\Database\\Youtube')




def SpeedTest():

    def run_uit():

        speak("I Am Checking Speed Sir , Wait For A While .")

        import speedtest
        speed = speedtest.Speedtest()
        upload = speed.upload()
        correct_Up = int(int(upload)/800000)

        download = speed.download()

        correct_down = int(int(download)/800000)

        speak(f"Downloading Speed Is {correct_down} M B Per Second .")
        speak(f"Uploading Speed Is {correct_Up} M B Per Second .")

        exit()

    class MainThread(QThread):

        def __init__(self):

            super(MainThread,self).__init__()

        def run(self):
            run_uit()

    StartExe = MainThread()

    class StartExecution(QMainWindow):

        def __init__(self):

            super().__init__()

            self.ui = Ui_SpeedTest()

            self.ui.setupUi(self)

            self.ui.label = QMovie("C:\\Users\\admin\\Downloads\\How To Make Jarvis-20220203T043852Z-001\\How To Make Jarvis\\DataBase\\Gui Materials\\speedTest.gif")

            self.ui.gif.setMovie(self.ui.label)

            self.ui.label.start()

            StartExe.start()

    App = QApplication(sys.argv)
    speedtest = StartExecution()
    speedtest.show()
    exit(App.exec_())


def calculate(audio_data):
    app_id = 'UTLPWL-4LXR7HQGLW'
    client = wolframalpha.Client(app_id)
    res = client.query(audio_data)
    answer = next(res.results).text
    speak(answer)

def Alarm(query):
    Timehere = open('C:\\Users\\admin\\PycharmProjects\\ Jarvis\\Data1.txt', 'a')
    Timehere.write(query)
    Timehere.close()
    os.startfile("C:\\Users\\admin\\PycharmProjects\\ Jarvis\\Database\\ExtraPro\\alarm.py")

def restart():
    speak("Ok Sir    ")
    speak("Restarting your computer")
    click()
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('enter')
    sleep(3)
    pyautogui.press('r')
    pyautogui.press('enter')

def Sleep():
    speak('Ok sir    ')
    speak("Initializing sleep mode")
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
    sleep(2)
    pyautogui.press('s')
    pyautogui.press('s')
    pyautogui.press('enter')

def CoronaVirus(Country):
    countries = str(Country).replace(" ", "")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text, 'lxml')

    corona = soups.find_all('div', class_='maincounter-number')

    Data = []

    for case in corona:
        span = case.find('span')

        Data.append(span.string)

    cases, Death, recovored = Data

    speak(f"Cases : {cases}")
    speak(f"Deaths : {Death}")
    speak(f"Recovered : {recovored}")


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=45f8eff9c4bb4bdc9d62bdd9f3ec43b6'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

def My_Location():
    op = "https://google.com/maps/place/16th+Ave,+Gaur+City+2,+Ghaziabad,+Uttar+Pradesh+201009/@28.62255,77.4203379,17z/data=!3m1!4b1!4m5!3m4!1s0x390cefcb0f8c4db9:0xaea9c6228fe3fe69!8m2!3d28.62255!4d77.4225319"
    speak("Checking.....")
    web.open(op)
    ip_addres = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_addres + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    speak(f"Sir, You are Now In {state, country}")

def TakeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(": Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print(f": User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def Tran():
    speak('Tell me the line')
    line = TakeHindi()
    translate = Translator()
    result = translate.translate(line)
    Text = result.text
    speak(f'The Translation For This Line: '+Text)

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('coderanshcoder.it@gmail.com', 'coderansh@Pass')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()
  
def walfram(query):
    api_key = 'EKTJXH-L954GXE4K6'
    requeter = wolframalpha.Client(api_key)
    requested = requeter.query(query)

    try:
        Answer = next(requested.result).text
        return Answer

    except:
        speak('An String Value Is Not Answerable .')


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Welcome back Ansh sir")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def Music():
    speak("Tell Me The NamE oF The Song!")
    musicName = takeCommand()

    if 'mood' in musicName:
        os.startfile('D:\\Code, Music and etc\\Ansh_Project\\Music\\24kGoldn-Mood.mp3')

    elif 'believer' in musicName:
        os.startfile('D:\\Code, Music and etc\\Ansh_Project\\Music\\Believer Mp3 Imagine Dragons.mp3')

    elif 'apna time aayega' in musicName:
        os.startfile('D:\\Code, Music and etc\\Ansh_Project\\Music\\Apna Time Aayega - Gully Boy 128 Kbps.mp3')

    elif 'patlamaya' in musicName:
        os.startfile('D:\\Code, Music and etc\\Ansh_Project\\Music\\PatlamayaDevam(PagalWorld)(1).mp3')

    elif 'yalgaar' in musicName:
        os.startfile('D:\\Code, Music and etc\\Ansh_Project\\Music\\Yalgaar(PaglaSongs).mp3')

    else:
        pywhatkit.playonyt(musicName)

    speak("Your Song Has Been Started! , Enjoy Sir!")

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):

        toast = ToastNotifier()
        toast.show_toast(" Jarvis ", "The Jarvis Is Now Activated", duration=3)
        wishMe()
        while True:
        # if 1:
            self.query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'eye use to move' in self.query:
                import eyemouse
                eyemouse   

            elif 'change new screen' in self.query:
                press_and_release("ctrl+windows+d")
    
            
            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")
            
            elif 'search on youtube' in self.query:
                speak("What sould I search?")
                command = takeCommand().lower()
                sleep(5)
                webbrowser.open("https://www.youtube.com/results?search_self.query=" + command)

            elif 'calculate' in self.query:
                speak('Tell me sir')
                audio_data = takeCommand()
                calculate(audio_data)

            

            elif 'take screenshot' in self.query:
                speak("sir, please teel me the name for this screenshot file")
                name = takeCommand().lower()
                speak("PLEASE SIR HOLD THE SCREEN FOR FEW SECONDS, I AM TALKING SCREEN SHOT")
                sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("Sir I am done. the screenshot saved in our main folder")

            elif 'Jor se bolo' in self.query:
                speak("jai mata di")

            elif 'whatsapp message' in self.query:
                name = self.query.replace("send whatsapp", "")
                name = name.replace("send", "")
                name = name.replace("message", "")
                name = name.replace("java", "")
                name = name.replace("jarvis", "")
                name = name.replace("to", "")
                Name = str(name)
                speak(f"Whats The message for {name}")
                MSG = takeCommand().lower()
                from automation import whatsappmsg
                whatsappmsg(Name,MSG)

            elif 'hindi chat' in self.query:
                name = self.query.replace("hindi chat", "")
                name = name.replace("hindi", "")
                name = name.replace("chat", "")
                name = name.replace("java", "")
                name = name.replace("jarvis", "")
                name = name.replace("to", "")
                Name = str(name)
                speak(f"Whats The message for {name}")
                HINDIMISG = TakeHindi()
                from automation import hindiMSG
                hindiMSG(name, HINDIMISG)

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret,img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif 'whatsapp call' in self.query:
                from automation import whatsappcall
                name = self.query.replace("call ", "")
                name = name.replace("to", "")
                name = name.replace("jarvis ", "")
                Name = str(name)
                whatsappcall(name)

            elif 'chat' in self.query:
                speak("With Whom ?")
                name = takeCommand().lower()
                from  automation import whatsappchat
                whatsappchat(name)

            elif 'video call' in self.query:
                from automation import whatsappvideocall
                name = self.query.replace("video", "")
                name = name.replace("call", "")
                name = name.replace("to", "")
                Name = str(name)
                whatsappvideocall(name)

            elif 'corona cases' in self.query:

                speak("Which Country's Information ?")

                cccc = takeCommand()
                CoronaVirus(cccc)

            elif 'download' in self.query:
                DownloadYouTube()

            elif 'turn on Alexa mod' in self.query:
                from Database.Homeauto.usealexa import alef
                alef()



            elif 'turn of Alexa mod' in self.query:
                from  Database.Homeauto.usealexa import alefs
                alex()

            elif 'input to Alexa' in self.query:
                from Database.Homeauto.alexa import alex
                alex()

            elif 'disconnect to alexa' in self.query:
                from Database.Homeauto.alexa import disalex
                disalex()

            elif 'remember that' in self.query:
                remeberMsg = self.query.replace("remember that", "")
                remeberMsg = remeberMsg.replace("jarvis", "")
                remeberMsg = remeberMsg.replace("java", "")
                speak("Tell Me to remind you that :"+remeberMsg)
                remeber = open('data.txt', 'w')
                remeber.write(remeberMsg)
                remeber.close()

            elif 'what do you remember' in self.query:
                remeber = open('data.txt', 'r')
                speak("You tell me that" + remeber.read())

            elif 'open google' in self.query:
                webbrowser.open("google.com")

            elif 'search on Google' in self.query:
                speak("sir, what should i search on google")

                cm = takeCommand().lower()
                webbrowser.open(f"{cm}")

            elif 'tell me news' in self.query:
                speak("please wait sir, I am feteching the latest news")
                news()

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                sleep(1)
                pyautogui.keyUp("alt")

            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")



            elif 'play music' in self.query:
                music_dir = 'D:\\Code, Music and etc\\Ansh_Project\\Music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'home screen' in self.query:
                press_and_release('windows + m')

            elif 'minimize' in self.query:
                press_and_release('windows + m')

            elif 'show start' in self.query:
                press('windows')

            elif 'settings' in self.query:
                press_and_release("windows + i")

            elif 'close chrome' in self.query:
                os.system("TASKKILL /F /im Chrome.exe")

            elif 'wins' in self.query:
                press_and_release('windows + s')

            elif 'widject' in self.query:
                press_and_release('window + h')

            elif "translator" in self.query:
                Tran()



            elif 'restore windows' in self.query:
                press_and_release('windows + Shift + M')

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'code' in self.query:
                codePath = "C:\\Users\\admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\"
                os.startfile(codePath)

            elif 'volume up' in self.query:
                pyautogui.press("volumeup")

            elif 'volume down' in self.query:
                pyautogui.press("volumedown")

            elif 'vloume turnoff' in self.query:
                pyautogui.press("volumemute")


            elif 'hide all file' in self.query or 'hide thise file' in self.query or 'visible for everyone' in self.query:
                speak("Sir please tell me you want to hide this folder or make it visible to every one")
                condition1 = takeCommand().lower()
                if "hide" in condition1:
                    os.system("attrib +h /s /d")
                    speak("Sir all files our hide in this folder are now hidden.")

                elif "visible" in condition1:
                    os.system("attrib -h /s /d")
                    speak("Sir all files our unhide n this folder for know.")

                elif "leave it" in condition1 or "lieve for know" in condition1:
                    speak("Ok sir")

            elif "weather" in self.query:
                speak("Name the state to see the teamperature")
                tem = input("Name the state to see the teamperature")
                search = f"teamperature in {tem}"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")

            elif "call" in self.query:
                from automation import calls
                calls()

            elif 'track phone number' in self.query:
                speak("Write Number to track :")
                num = input("Write Number to track")
                anNumber = phonenumbers.parse(num)
                yourLocation = geocoder.description_for_number(anNumber, "en")
                speak(yourLocation)
                print(yourLocation)

                service_provider = phonenumbers.parse(num)
                speak(carrier.name_for_number(service_provider, "en"))
                print(carrier.name_for_number(service_provider, "en"))

            elif 'you need a break' in self.query:
                speak("Ok Sir Just say wake up jarvis")
                break

            elif 'take photo' in self.query:
                cam = cv2.VideoCapture(0)
                cv2.namedWindow("test")
                img_counter = 0
                while True:
                    ret, frame = cam.read()
                    if not ret:
                        print("failed to grab frame")
                        break
                    cv2.imshow("test", frame)
                    k = cv2.waitKey(1)
                    if k % 256 == 27:
                        # ESC pressed
                        print("Escape hit, closing...")
                        break
                    elif k % 256 == 32:
                        # SPACE pressed
                        img_name = "opencv_frame_{}.png".format(img_counter)
                        cv2.imwrite(img_name, frame)
                        print("{} written!".format(img_name))
                        img_counter += 1
                cam.release()
                cv2.destroyAllWindows()

            elif 'music' in self.query:
                Music()

            elif 'my location' in self.query:
                My_Location()

            elif 'stop' in self.query:
                press('space bar')

            elif 'resume' in self.query:
                press('space bar')

            elif 'full screen' in self.query:
                press('f')

            elif 'skip' in self.query:
                press('l')

            elif 'back' in self.query:
                press('j')

            elif 'increase' in self.query:
                press_and_release('SHIFT + .')

            elif 'decrease' in self.query:
                press_and_release('SHIFT + ,')

            elif 'mute' in self.query:
                press('m')

            elif 'previous video' in self.query:
                press_and_release('SHIFT + p')

            elif 'next video' in self.query:
                press_and_release('SHIFT + n')

            elif 'open search' in self.query:
                click(x=824, y=131)
                speak("What sould I search")
                search = takeCommand().lower()
                write(search)
                sleep(1)
                press('enter')

            elif 'unmute' in self.query:
                press('m')

            elif 'open youtube' in self.query:
                web.open('https://www.youtube.com/')


            elif 'instagram profile' in self.query:
                speak("sir please enter the user name correctly")
                name = input("Enter user name here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                sleep(5)
                speak("sir would you like to download profile picture of the account.")
                condition = takeCommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("I am done sir , your pic has download")
                else:
                    pass

            elif 'open mobile camera' in self.query:
                URL = "http://192.168.29.86:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    img = cv2.imdecode(img_arr,-1)
                    cv2.imshow('IPWecam',img)
                    q = cv2.waitKey(1)
                    if q==ord("q"):
                        break;

                cv2.destroyAllWindows()

            elif 'how to' in self.query:
                speak('Getting Data From The Internet !') 
                op = self.query.replace('jarvis', '')
                op = self.query.replace('Jarvis', '')
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) ==1
                speak(how_to_func[0].summary)

            # '''elif 'alarm' in self.query:
            #     speak("Sir please tell the time  to set alram for example, set alarm to five thurty am")
            #     tt = takeCommand()
            #     tt = tt.replace("set alram to ", "")
            #     tt = tt.upper()
            #     Myalarm.alarm(tt)'''

            # elif 'alarm' in self.query:
            #     speak("Enter The Time !")
            #     time = input(": Enter The Time :")

            #     while True:
            #         Time_Ac = datetime.datetime.now()
            #         now = Time_Ac.strftime("%H:%M:%S")

            #         if now == Time_Ac:
            #             speak("Time To Waktee Up Sir!")
            #             playsound('C:\\Users\\admin\\PycharmProjects\\ Jarvis\\Database\\Sounds\\1.mp3')
            #             speak("Alarm Closed!")

            #         elif now>time:
            #             break

            elif 'solar system' in query:
                from Nasa import SolarBodies
                speak('Tell Me The Name Of Bodies')
                bod = takeCommand()
                body = bod.replace(" ", "")
                body = body.replace(" ", "")
                Body = str(body)
                SolarBodies(body=Body)

            elif 'photos of mars' in self.query:
                speak("Fetching mars photos....")   
                from Nasa import MarsImages
                MarsImages()

            elif 'space news' in self.query:
                speak("Tell Me the date  for news extracting Process")
                speak("Please enter the date like 2021-1-1 first year then month then date:")
                from Nasa import NasaNews
                value = input("Please enter the date like 2021-1-1 first year then month then date:")
                sleep(5)
                NasaNews(value)

            elif 'minecraft' in self.query:
                from Database.GameAuto.minecraft import mine
                mine()

            # elif 'send email to' in self.query:
            #     try:
            #         speak("please write the email correctly")
            #         com = input("Sender email write:")
            #         speak("What should I say?")
            #         content = takeCommand()
            #         to = f"{com}"
            #         sendEmail(to, content)
            #         speak("Email has been sent!")
            #     except Exception as e:
            #         print(e)
            #         speak("Sorry my friend Ansh bhai. I am not able to send this email")

            elif 'where is' in self.query:
                from automation import GoogleMaps
                Place = self.query.replace("where is", "")
                Place = Place.replace("jarvis", "")
                Place = Place.replace("Jarvis", "")
                Place = Place.replace("Java", "")
                GoogleMaps(Place)

            elif 'new tab' in self.query:
                press_and_release('ctrl+t')

            elif 'close tab' in self.query:
                press_and_release('ctrl+w')

            elif 'new window' in self.query:
                press_and_release('ctrl + n')

            elif 'history' in self.query:
                press_and_release('ctrl + h')

            elif 'download' in self.query:
                press_and_release('ctrl + j')

            elif 'bookmark' in self.query:
                press_and_release('ctrl + d')
                press('enter')


            elif 'incognito' in self.query:
                press_and_release('ctrl + shift + n')



            elif 'switch tab' in self.query:
                tab = self.query.replace("switch tab", "")
                Tab = tab.replace("to", "")
                num = Tab
                bb = f'ctrl + {num}'
                press_and_release(bb)

            elif 'about' in self.query:
                from Nasa import Astro
                self.query = self.query.replace("jarvis ","")
                self.query = self.query.replace("about ","")
                Astro(self.query)

            elif 'real math' in self.query:
                from Database.GameAuto.skysmash import start
                start()

            elif 'close' in self.query:
                from Database.GameAuto.skysmash import shutdown
                shutdown()

            elif 'connect' in self.query:
                from Database.remoteauto.sauto import connectan
                connectan()

            # elif 'open' in self.query:
                # name = self.query.replace("open ", "")
                # NameA = str(name)

                # if 'youtube' in self.query:
                #     web.open("https://www.youtube.com/")

                # elif 'instagram' in self.query:
                #     web.open("https://www.instagram.com/")

                # elif 'facebook' in self.query:
                #     web.open("https://www.facebook.com/")

                # else:
                #     string = "https://www." + NameA + ".com"
                #     string_2 = string.replace(" ", "")
                #     web.open(string_2)

            
            elif 'sleep' in self.query or 'sleep mode' in self.query:
                Sleep()

            elif "write a note" in self.query:
                from automation import notepadAuto
                notepadAuto()

            elif 'dismiss' in self.query:
                from automation import closeNotepad
                closeNotepad()

            elif 'online' in self.query:
                from automation import onlineClass
                speak('Tell Me The Class Sir')
                Class = takeCommand().lower()

                onlineClass(Class)

            elif 'speed test' in self.query:
                SpeedTest()
        
            elif 'quit' in self.query:
                    speak("BY sir thanks for time yuo give to me")
                    quit()

                                                                                        
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:\IMAGES\mainop.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:\IMAGES\insta.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.ui.movie.start()
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss") 
        label_date = current_date.toString(Qt.ISODate)        
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_3.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())



