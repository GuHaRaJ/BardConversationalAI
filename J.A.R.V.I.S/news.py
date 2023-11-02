from Speak import Speak
import json
import requests
from time import sleep

news_api = ""##get the api key from news_api
def speak_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey='+news_api
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    Speak('Source: Google News')
    sleep(3)
    Speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        Speak(articles['title'])
        if index == len(arts)-1:
            break
        sleep(5)        
        Speak('Moving on the next news headline..')
        sleep(5)
    Speak('These were the top headlines..')

def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey='+news_api


#speak_news()