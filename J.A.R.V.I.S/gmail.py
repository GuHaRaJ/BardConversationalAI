import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
from Speak import Speak
import smtplib


def opengmail():
    Speak("checking the mails...")
    sleep(0.5)
    Speak("displaying it on the screen")
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")


def sendEmail(self, to, content) -> None:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('g.g.guharaj@gmail.com', 'password')
    server.sendmail('email', to, content)
    server.close()



# opengmail()





