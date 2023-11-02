from Speak import Speak
import pyautogui
import webbrowser
import random

def youtube():
    Speak("i am very sorry to hear that,But i know what to do ")
    Speak("playing your favourite's from youtube")
    a = (1,2,3,4,5,6,7)
    b = random.choice(a)
    if b == 1:              #b
        webbrowser.open("https://www.youtube.com/watch?v=4u-4KljtRHM")
        pyautogui.press("k")
    elif b == 2:
        webbrowser.open("https://www.youtube.com/watch?v=OtKZMe50loA")
        pyautogui.press("k")
    elif b == 3:
        webbrowser.open("https://www.youtube.com/watch?v=fRD_3vJagxk")
        pyautogui.press("k")
    elif b == 4:
        webbrowser.open("https://www.youtube.com/watch?v=5WDQgBGfx40")
        pyautogui.press("k")
    elif b == 5:
        webbrowser.open("https://www.youtube.com/watch?v=pxCWiYFkvTg")
        pyautogui.press("k")
    elif b == 6:
        webbrowser.open("https://youtu.be/sUJ4pjfWArA")
        pyautogui.press("k")
    elif b == 7:
        webbrowser.open("https://youtu.be/CTP03doBUmo?si=_5Q0zC4qUq9PAaDW")
        pyautogui.press("k")