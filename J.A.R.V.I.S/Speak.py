from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time



#Firefox as thee browser..
service = Service(executable_path='G:\J.A.R.V.I.S\geckodriver-v0.31.0-win64\geckodriver.exe')#give your executable path...
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(service=service, options=options)
driver.get("https://tts.5e7en.me/")



def Speak(Text):
    lengthofText = len(str(Text))

    if lengthofText ==0:
        pass

    else:
        print("")
        print(f"AI :{Text}.")
        print("")
        Data = str(Text)
        xpathofsec = '//*[@id="text"]'
        driver.find_element(By.XPATH, '//*[@id="text"]').click()
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="button"]').click()
        driver.find_element(By.XPATH,value= '//*[@id="text"]').clear()

        if lengthofText>=30:
            time.sleep(4)                         #should change............
        
        elif lengthofText>=40:
            time.sleep(6)
        
        elif lengthofText>=55:
            time.sleep(8)

        elif lengthofText>=70:
            time.sleep(10)

        elif lengthofText>=100:
            time.sleep(13)

        elif lengthofText>=120:
            time.sleep(14)
        
        else:
            time.sleep(2)




"""
offline voice....
# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# print(voices[0])
"""