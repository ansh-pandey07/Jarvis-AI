from email.mime import image
import pyttsx3
import pytesseract
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
speak("PLEASE Enter the path correctly")
path  = input('Enter the path:')
image_1 = f'{path}'

img_obg_1 = Image.open(image_1)

text_1 = pytesseract.image_to_string(img_obg_1)
speak(text_1) 