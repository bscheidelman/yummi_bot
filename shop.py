from pynput.mouse import Button, Controller
import time

def shopOne():

    mouse = Controller()


    mouse.press(Button.left)
    mouse.release(Button.left)

    time.sleep(0.1)

def shopTwo():
    mouse = Controller()

    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.1)