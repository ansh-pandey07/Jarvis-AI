import os
from sqlite3 import Date
from tokenize import Special
import requests
import pyttsx3
import matplotlib.pyplot as plt
from PIL import Image

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

Api_key = "TdngjnMdb2lZ9SOjVB8GZSvtY4PeVh6mf6pynrBJ"

def NasaNews(Date):
    speak("Extracting Data from nasa")

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_key)
    Params = {'date':str(Date)}
    r = requests.get(Url,params=Params)
    Data = r.json()
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    Image_r = requests.get(Image_Url)
    Filename = str(Date) + '.jpg'
    print(Filename)

    with open(Filename,'wb') as f:

         f.write(Image_r.content)

    Path_2 = "D:\\Ansh Coder Jarvis\\Jarvis\\Jarvis\\Database\\NasaDatabase\\" + str(Filename)
    Path_1 = "D:\\Ansh Coder Jarvis\\Jarvis\\Jarvis\\" + str(Filename)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)
    img.show()

    speak(f"Title: {Title}")
    speak(f"Accroding to Nasa : {Info}")

def MarsImages():
    name = 'curiosity'
    speak("Write the date ?")
    dateOP= input("Write the date ?")
    date = f'{dateOP}'
    Api_ = str(Api_key)
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}'
    r = requests.get(url)
    Data= r.json()
    speak("Please enter The Number of Photos You Want To Get?")
    ansh = input("Please enter The Number of Photos You Want To Get?")
    OPBhai = int(ansh)
    Photos = Data['photos'][:OPBhai]

    for index , photo in enumerate(Photos):
        camera = photo['camera'] 
        rover = photo['rover']
        rover_name = rover['name']
        camera_name = camera['name']
        full_camera_name = camera['full_name']
        date_of_photo = photo['earth_date']
        img_url = photo['img_src']
        p = requests.get(img_url)
        name = str(index)
        img = f'{name + " " + date}.jpg'

        with open(img, 'wb')as file:
            file.write(p.content)

        Path_1 = "D:\\Ansh Coder Jarvis\\Jarvis\\Jarvis\\Database\\NasaDatabase\\MarsPhotos\\" + str(img)
        Path_2 = "D:\\Ansh Coder Jarvis\\Jarvis\\Jarvis\\" + str(img)
        os.rename(Path_1,Path_2)
        os.startfile(Path_2)

        speak(f"This Image Was Captured With : {full_camera_name}")
        speak(f"This Image Was Captured On : {date_of_photo}")

def SolarBodies(body):

    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    r = requests.get(url)
    Data = r.json()

    bodies = Data['bodies']
    Number = len(bodies)

    for bodyyy in bodies:
        print(bodyyy['id'],end=',')
    
    url_2 = f'https://api.le-systeme-solaire.net/rest/bodies/{body}'
    rrr = requests.get(url_2)
    data_2 = rrr.json()
    mass = data_2['mass']['massValue']
    volume = data_2['vol']['volValue']
    density = data_2['density']
    gravity = data_2['gravity']
    escape = data_2['escape']
    
    speak(f"Name of bodies in solar system : {Number}.")
    speak(f"Mass of {body} is {mass}.")
    speak(f"Gravity of {body} is {gravity}.")
    speak(f"Escape Velocity of {body} is {escape}.")
    speak(f"Density of {body} is {density} .")

