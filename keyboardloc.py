import pyautogui
import time

temp = True
while temp:
    x = pyautogui.position()
    print(x)
    time.sleep(2.5)
