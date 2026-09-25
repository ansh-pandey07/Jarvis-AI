from ast import Pass
import pyttsx3
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

speak("Tell Me The Password")

def passw(pass_inp):
    password = "messi"
    passs =str(password)
    if passs ==str(pass_inp):
        import jarvisGui

    else:
        speak("Your Password is incorrect")

if __name__ == "__main__":
    speak("This File is password Protected")
    passssssssssss = takeCommand()

    passw(passssssssssss)