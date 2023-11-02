import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
from Speak import Speak
import webbrowser

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower() 

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        Speak("this is what i found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,2)
            Speak(result)
        
        except:
            Speak("there are no proper outputs available")

def searchYoutube(query):
    if "youtube" in query:
        Speak("this is what I found for your search!")
        query = query.replace("jarvis","")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        Speak("done, sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        Speak("Searching from wikipedia...")
        query = query.replace("wikipedia search","")
        query = query.replace("jarvis","")
        query = query.replace("search wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        Speak("According to wikipedia")
        print(results)
        Speak(results)

