from Speak import Speak
import pywhatkit
import webbrowser
import wikipedia
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
    if "youtube search" in query:
        Speak("this is what I found for your search!")
        query = query.replace("jarvis","")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        Speak("done, sir")
    elif "open youtube" in query:
        Speak("opening youutube from firefox")
        web = "https://www.youtube.com/"
        webbrowser.open(web)


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

