import webbrowser, requests
from Speak import Speak
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time


def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']

    return city, state,country


### STRICTLY USE FIREFOX ELSE FAULTS MAY HAPPEN...........
def loc(query):
    service = Service(executable_path='G:\J.A.R.V.I.S\geckodriver-v0.31.0-win64\geckodriver.exe')## mention your executable path here........
    options = webdriver.FirefoxOptions()
    options.set_preference('geo.prompt.testing', True)
    options.set_preference('geo.prompt.testing.allow', True)
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://www.google.com/maps")
    time.sleep(8)
# driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[23]/div[1]/div[3]/div[5]/div/button/div").click()

    driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[23]/div[1]/div[3]/div[5]/div/button/div").click()
    time.sleep(5)

#search part--> copied the xpath of the class
    driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/div[2]").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div/input").send_keys(query)
    driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]").click()
    Speak("analyzing the best and the fastest route to the required destination")
    time.sleep(7)

    distance = driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[2]/div")
    Speak(f"distance from your current location to {query} is {distance.text}")
    time.sleep(5)
    timing = driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[1]")
    Speak(f"the approximate time taken to reach the destination from the current location is {timing.text}")








