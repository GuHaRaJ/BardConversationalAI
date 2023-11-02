import pyfiglet
import pyautogui
import webbrowser
import random
import datetime
print(">> Starting JARVIS................................................")
from TakeCommand import takeCommand
import os
from search import searchGoogle
import playsound
from location import my_location
from time import sleep
from Speak import Speak
import requests
from datetime import date
import calendar
from location import loc
from news import getNewsUrl
from system_stats import getcpuper,getbattery,getram
from playsound import playsound
import pyautogui
from quotes import quotes
quotes()
from volumecontrol import volumeup
from open_app_web import closeappweb
from open_app_web import openappweb
from search import searchYoutube
from volumecontrol import volumedown
from news import speak_news
from open_app_web import closeappweb
from fun import youtube
from greetme import greetMe



MUSICS_DIR = "D:\MUSIC"  ##create a folder and insert songs in that particular folder....

import speech_recognition as sr
from playsound import playsound




if __name__ == "__main__":
    playsound('assets_sounds_jarvislistening (mp3cut.net).mp3')
    while True:
        query = (takeCommand().lower())
        query = str(query)
        if len(query)<3:
            pass
        
        elif "wake up" in query:
            from greetme import greetMe
            print(pyfiglet.figlet_format("JARVIS",justify="center"))
            
            greetMe()
            while True:
                query = takeCommand().lower()
                query = query.replace("jarvis","")
                if len(query)<5:
                    pass

                elif "go to sleep" in query or "sleep" in query:
                    Speak("going into sleep mode")
                    break

                # elif "stop it" in query or "please stop it" in query or "its enough" in query or "ok stop it":
                #     pass
                ##########################################################################################
            
                ##############################################

                elif "how is the day outside" in query or "weather updates" in query or "how is the weather outside" in query:
                    from greetme import Temperature
                    Temperature()
                    from greetme import humidity
                    humidity()
                    from greetme import wind_speed
                    wind_speed()
                    
                
                elif "play music" in query or "play songs" in query or "play some music" in query:
                    from playmusic import startPlaymusic
                    Speak("playing songs from your local playlist")
                    startPlaymusic(MUSICS_DIR)
                
                
                elif "pause music" in query:
                    from playmusic import pauseMusic
                    Speak("music paused")
                    pauseMusic()
                
                
                elif "unpause music" in query or "resum playing the music" in query or "resume the music" in query:
                    from playmusic import unpauseMusic
                    unpauseMusic()
                
                
                elif "stop music" in query or "stop playing songs" in query:
                    from playmusic import stopMusic
                    Speak("music player has been stopped")
                    stopMusic()
                

####################################################FIREFOX#########################################################
                elif "tired" in query or "i am feeling tired" in query or "i am feeling bored" in query:
                    youtube()

                elif "where is" in query or "how far is" in query or "where exactly is" in query:
                    query = query.replace("where is","")
                    query = query.replace("from my location","")
                    try:
                        loc(query)
                    except:
                        Speak("unable to fetch")
                        pass
                
                elif "close the window" in query:
                    pyautogui.moveTo(500,47)
                    pyautogui.click()
                    pyautogui.hotkey("ctrl","w")
                
                
                elif "open" in query:
                    openappweb(query)
                

                elif "close" in query:
                    closeappweb(query)
                
                
                elif "close the current app" in query:
                    closeappweb(query)

                elif "ip address" in query:
                    ip = requests.get('https://api.ipify.org').text
                    Speak(f"Your ip address is {ip}")

                elif "where i am" in query or "current location" in query or "where am i" in query:
                    try:
                        city, state, country = my_location()
                        print(city, state, country)
                        Speak(
                            f"You are currently in {city} city which is in {state} state and country {country}")
                    except Exception as e:
                        Speak(
                            "Sorry, I coundn't fetch the required location")
                    
                
                elif 'news' in query:
                    Speak('reading the top headlines..')
                    speak_news()
                    Speak('Do you want to read the full news...')
                    test = takeCommand()
                    if 'yes' in test:
                        Speak('Opening browser...')
                        webbrowser.open(getNewsUrl())
                        Speak('You can now read the full news from this website.')
                    else:
                        Speak('No Problem')
                        break
                
                elif "screenshot" in query:
                    query = query.replace("jarvis ","")
                    im = pyautogui.screenshot()
                    im.save()
                    im.save("ss.jpg")
                
                elif "google" in query or "google search" in query:
                    query = query.replace("jarvis ","")
                    searchGoogle(query)

                elif "youtube" in query:
                    query = query.replace("jarvis ","")
                    searchYoutube(query)
    
                elif "stop" in query:
                    query = query.replace("jarvis ","")
                    pyautogui.press("k")
                    Speak("video stopped")
                
                elif "play" in query:
                    query = query.replace("jarvis ","")
                    pyautogui.press("k")
                    Speak("video played")
                
                elif "mute" in query:
                    query = query.replace("jarvis ","")
                    pyautogui.press("m")
                    Speak("video muted")
                
                elif "volume up" in query:
                    query = query.replace("jarvis ","")    
                    Speak("turning volume up")
                    volumeup()
                
                elif "volume down" in query:
                    query = query.replace("jarvis ","")
                    Speak("turning volume down")
                    volumedown()

######################################SYSTEM STATS###################################################               
                elif "how much power left" in query or "how much power is left" in query or "battery" in query or "battery status" in query or "how much power we have" in query or "can you check the battery" in query or "how much power are we left with" in query or "battery percentage" in query or "how much is the battery percentage" in query or "how much power are we left" in query:
                    from system_stats import getbattery
                    getbattery()
    
                elif "today's date" in query or "todays date" in query or "what's the date" in query:
                    from datetime import date
                    today = date.today()
                    Speak(f"Today's date is {today}")
                
                elif "what's the day" in query or "what is the day" in query or "today's day" in query:
                    my_date = date.today()
                    Speak(f"today's day is {calendar.day_name[my_date.weekday()]}")

                elif "the time" in query or "what's the time" in query or "time" in query or "what's the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    Speak(f"sir, the time is {strTime}")
                
                elif "system stats" in query or "how is the system operating" in query or "how is the system running" in query or "how is the system working" in query or "cpu usage" in query or "cpu running" in query:
                    Speak("performing a check")
                    getcpuper()
                    sleep(2)
                    getbattery()
                    sleep(2)
                    getram()
                
                elif "check the mails" in query or "did i receive any mails" in query:
                    from gmail import opengmail
                    opengmail()
                
                
                elif "terminate" in query or "jarvis terminate" in query:
                    Speak("Going off")
                    exit()

                elif "shutdown system" in query:
                    Speak("are you sure you want to shutdown your computer? (yes/no)")
                    if "yes" in query:
                        os.system("shutdown /s /t 1")
                            
                    elif "no" in query:
                        Speak("system will be running in normal")
                        continue
                
                elif "what do you mean" in query or "who is" in query or "what" in query or 'when' in query or "explain" in query or "where" in query or "whom" in query or "which" in query or "how" in query or "whose" in query:
                    from palm import palmtext
                    query = query.replace("jarvis","")
                    palmtext(query)
                

                elif "" in query:
                    from palm_chat import palmchat
                    palmchat(query)
                
                
                
                

                
                