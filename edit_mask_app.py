import openai
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr

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


openai.api_key = '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'

speak("Please tell The Image To Mask And The Mask Image And A Prompt")

response = openai.Image.create_edit(
  image=open(input("Write The Image To Mask in Address Form:"), "rb"),
  mask=open(input("Write The Mask Image in Address Form:"), "rb"),
  prompt=input("Enter Here Prompt:-"),
  n=1,
  size="1123x969"
)
image_url = response['data'][0]['url']
print(image_url)