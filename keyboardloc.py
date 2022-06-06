import pyautogui
import time
import PIL.ImageGrab


def findRGB(xloc,yloc):
    rgb = PIL.ImageGrab.grab().load()[xloc,yloc]
    return rgb

temp = True
while temp:
    x = pyautogui.position()

    print(x)
    print(findRGB(x.x,x.y))
    time.sleep(2.5)
