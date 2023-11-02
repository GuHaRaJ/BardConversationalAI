import datetime
import requests
from bs4 import BeautifulSoup
from Speak import Speak
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from time import sleep


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        Speak("Hello, welcome back")
    elif hour >12 and hour<=16:
        Speak("Hello, welcome back")
    else:
        Speak("Hello, welcome back")
        
def Temperature():
    search = " temperature in bangalore"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    final_temp = data.find("div",class_ = "BNeawe").text
    Speak("the weather in bangalore is "+final_temp)

def humidity():
    s = HTMLSession()
    url = "https://www.google.com/search?client=firefox-b-d&q=humidity+in+bangalore"
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'})
    final_hum = r.html.find('span#wob_hm',first=True).text
    Speak("with a humidity of " + final_hum)


def wind_speed():
    h = HTMLSession()
    url = "https://www.google.com/search?client=firefox-b-d&q=humidity+in+bangalore"
    r = h.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'})
    final_wind_speed = r.html.find('span#wob_ws',first=True).text
    Speak("with a wind speed of " + final_wind_speed)
    sleep(0.7)

    
def help():
    Speak("how may i assist you")  


