import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
from Speak import Speak

dictapp = {"commandprompt":"cmd","mspaint":"paint","word":"winword","excel":"excel","firefox":"firefox","vscode":"code","powerpoint":"powerpnt","settings":"ms-settings:"}

def openappweb(query):
    Speak("launching" + query)
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    Speak("closing")
    if "close the tab"in query or "close firefox" in query:
        os.system("taskkill /im firefox.exe /f")
        Speak("Tab closed")



