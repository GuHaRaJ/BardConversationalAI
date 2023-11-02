import speech_recognition as sr
from playsound import playsound

def takeCommand():
    r = sr.Recognizer()
    # playsound('assets_sounds_jarvislistening (mp3cut.net).mp3')
    with sr.Microphone() as source:
        while True:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 400
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)###<---,0,4
            try:
                print("Recognizing.....")
                query = r.recognize_google(audio,language='en-in')
                print(f"You Said:{query}\n")
            except Exception as e:
                print("Say that again")
                return "None"
            return query


# while True:
#     takeCommand()