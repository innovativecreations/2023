# import pyttsx3
#
# engine = pyttsx3.init()
#
# # engine.say("I'm just a guy who is fascinated by the working of everything")
# #
# # engine.runAndWait()
#
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()
#
##########################################################################
# import speech_recognition as sr
#
# r = sr.Recognizer()
#
# filename = "Recording.wav"
#
# # open the file
# with sr.AudioFile(filename) as source:
#     # listen for the data (load audio to memory)
#     audio_data = r.record(source)
#     # recognize (convert from speech to text)
#     text = r.recognize_google(audio_data)
#     print(text)


#######################################################################


import speech_recognition as sr

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import os
import pygame

voice2 = 'en-GB-SoniaNeural'
# Fetch the service account key JSON file contents
cred = credentials.Certificate('first-71449-firebase-adminsdk-6y6sr-0886524152.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://first-71449-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


# Convert text to speech
def speak(data):
    voice = 'en-US-SteffanNeural'
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def updateFB(child, state, refPath="/"):
    # As an admin, the app has access to read and write all data, regradless of Security Rules
    ref = db.reference(refPath)
    data = ref.get()

    data[child] = state
    print(data)
    ref.set(data)


wallColour = [255, 255, 255]
tableColour = [0, 0, 0]

knownCommand = {"command": ["turn on light",
                            "turn on fan",
                            "turn on second light",
                            "turn on all the lights",
                            "turn off light",
                            "turn off fan",
                            "turn off second light",
                            "turn off all the lights",
                            "zero mode",
                            "study mode",
                            "normal mode"],
                "reply": ["light one is on",
                          "done, fan is on",
                          "done, fan is on",
                          "ok, all lights are on",
                          "done, first light is off",
                          "ok, fan is off",
                          "done, second light is off",
                          "ok, all the lights are off"]}

print("vr begins")
r = sr.Recognizer()


def rec():
    with sr.Microphone() as s2:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(s2)
        audio = r.listen(s2)
        try:
            c = r.recognize_google(audio)
            c = c.lower()
            return c
        except Exception as e:
            print(e)


while True:
    command = rec()
    print(command)
    print("done")
    if command in knownCommand["command"]:
        if command == knownCommand["command"][0]:
            print("light one turned on")
            updateFB("relay1", 0)
            speak(knownCommand["reply"][0])
        elif command == knownCommand["command"][1]:
            updateFB("relay2", 0)
            speak(knownCommand["reply"][1])
        elif command == knownCommand["command"][2]:
            updateFB("relay1", 1)
            updateFB("relay3", 1)
            updateFB("relay4", 1)
            speak(knownCommand["reply"][2])
        if command == knownCommand["command"][4]:
            updateFB("relay1", 1)
            speak(knownCommand["reply"][4])
        elif command == knownCommand["command"][5]:
            updateFB("relay2", 1)
            speak(knownCommand["reply"][5])
        elif command == knownCommand["command"][7]:
            updateFB("relay1", 0)
            updateFB("relay3", 0)
            updateFB("relay4", 0)
            speak(knownCommand["reply"][7])
        elif command == knownCommand["command"][8]:
            updateFB("mode", 0, refPath="ledStrip/")
            speak("done")
        elif command == knownCommand["command"][9]:
            updateFB("mode", 2, refPath="ledStrip/")
            updateFB("r", wallColour[0], refPath="ledStrip/wall/")
            updateFB("g", wallColour[1], refPath="ledStrip/wall/")
            updateFB("b", wallColour[2], refPath="ledStrip/wall/")
            updateFB("r", tableColour[0], refPath="ledStrip/table/")
            updateFB("g", tableColour[1], refPath="ledStrip/table/")
            updateFB("b", tableColour[2], refPath="ledStrip/table/")
            speak("done")
        elif command == knownCommand["command"][10]:
            updateFB("mode", 1, refPath="ledStrip/")
            speak("done")
