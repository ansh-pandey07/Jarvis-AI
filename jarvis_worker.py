from PyQt5.QtCore import QThread, pyqtSignal

import pyttsx3
import speech_recognition as sr
import google.generativeai as genai

# ---------------- Gemini ----------------

genai.configure(api_key="YOUR_NEW_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- Voice Engine ----------------

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# ---------------- Functions ----------------

def speak(audio):
    try:
        print(f"Jarvis: {audio}")
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print("Speak Error:", e)


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.pause_threshold = 1

        try:
            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )
        except:
            return None

    try:

        print("Recognizing...")

        query = r.recognize_google(
            audio,
            language="en-in"
        )

        print("User:", query)

        return query

    except Exception as e:

        print("Recognition Error:", e)

        return None


def ai_chat(prompt):

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        print("Gemini Error:", e)

        return "Sorry, I couldn't process that."


# ---------------- Worker ----------------

class JarvisWorker(QThread):

    statusChanged = pyqtSignal(str)

    responseGenerated = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.running = True

    def stop(self):
        self.running = False

    def run(self):

        while self.running:

            # Listening
            self.statusChanged.emit("LISTENING")

            query = takeCommand()

            if not query:
                self.statusChanged.emit("READY")
                continue

            # Thinking
            self.statusChanged.emit("THINKING")

            answer = ai_chat(query)

            self.responseGenerated.emit(answer)

            # Speaking
            self.statusChanged.emit("SPEAKING")

            speak(answer)

            self.statusChanged.emit("READY")