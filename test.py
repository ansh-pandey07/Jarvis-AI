from deep_translator import GoogleTranslator

hindi_text = "मौसम कैसा है"

english = GoogleTranslator(
    source='auto',
    target='en'
).translate(hindi_text)

print(english)

import pvporcupine
import pyaudio
import struct


porcupine = pvporcupine.create(
    keywords=["jarvis"]
)

pa = pyaudio.PyAudio()

stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

print("Listening for Jarvis...")

while True:
    pcm = stream.read(porcupine.frame_length)
    pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

    result = porcupine.process(pcm)

    if result >= 0:
        print("Wake word detected!")
        break
