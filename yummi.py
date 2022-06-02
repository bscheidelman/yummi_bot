import PIL.ImageGrab
import pyautogui
from pynput.mouse import Button, Controller
from pynput.keyboard import Controller, Key, Listener
import time
import ScreenToText
import shop



def findRGB(xloc,yloc):
    rgb = PIL.ImageGrab.grab().load()[xloc,yloc]
    return rgb

def locateEnemy():
    try:
        enemyLoc = pyautogui.locateOnScreen('hpbar.png')
        enemyLoc = pyautogui.center(enemyLoc)
    except:
        return None
    return [enemyLoc.x,enemyLoc.y]

keyboard = Controller()

def yummiQ():
    if locateEnemy() != None:
        keyboard.press('q')
        keyboard.release('q')
        tick = 20
        while tick > 0:
            try:
                li = locateEnemy()
                pyautogui.moveTo(li[0]+48, li[1]+70, duration = 0.1)
            except:
                break
            tick -= 1

def yummiW():
    try:
        
        onChamp = pyautogui.locateOnScreen('cat.png')
        onChamp = pyautogui.center(onChamp)

        onChamp = pyautogui.locateOnScreen('yellow.png')
        onChamp = pyautogui.center(onChamp)
    except:
        tick = 0
        while True:
            time.sleep(0.6)
            tick += 1
            if tick % 3 == 0:
                pyautogui.moveTo(1450, 709, duration = 0.1)
                keyboard.press('w')
                keyboard.release('w')
            try:
                onChamp = pyautogui.locateOnScreen('cat.png')
                onChamp = pyautogui.center(onChamp)

                onChamp = pyautogui.locateOnScreen('yellow.png')
                onChamp = pyautogui.center(onChamp)
                break
            except:
                try:
                    onChamp = pyautogui.locateOnScreen('yellow.png')
                    onChamp = pyautogui.center(onChamp)
                    break
                except:
                    a = 0

def yummiE():
    pyautogui.moveTo(1450, 709, duration = 0.1)
    shop.shopOne()

    li = ScreenToText.grabText(603,175,678,188)
    nli = []
    for val in li:
        nli.append(int(val))
    if nli[0]/nli[1] < .7:
        keyboard.press('e')
        keyboard.release('e')

def yummiR():
    nli = locateEnemy()
    if nli != None:
        if (nli[0] > 708 and nli[0] < 1092) and (nli[1] > 380 and nli[1]< 751):
            pyautogui.moveTo(nli[0]+48, nli[1]+48, duration = 0.1)
            keyboard.press('r')
            keyboard.release('r')
            time.sleep(2.75)
            

def checkDead():
    try:
        isDead = pyautogui.locateOnScreen('death.png')
        isDead = pyautogui.center(isDead)
    except:
        return False
    print('rip')
    return True

def levelUp():
    lvlOrder = ["r","q","e","w"]
    for val in lvlOrder:
        with keyboard.pressed(Key.ctrl):
            keyboard.press(val)
            keyboard.release(val)

def yummiSums():
    '''
    #Heal
    pyautogui.moveTo(1450, 709, duration = 0.1)
    shop.shopOne()
    li = ScreenToText.grabText(603,175,678,188)
    ili = []
    for val in li:
        ili.append(int(val))
    if ili[0]/ili[1] < .3:
        keyboard.press('f')
        keyboard.release('f')
    '''
    #Ignite
    nli = locateEnemy()
    if nli != None:
        if (nli[0] > 708 and nli[0] < 1092) and (nli[1] > 380 and nli[1]< 751):
            pyautogui.moveTo(nli[0]+48, nli[1]+70, duration = 0.1)
            keyboard.press('d')
            keyboard.release('d')
         
def shopping():

    pyautogui.moveTo(704, 277, duration = 0.1)
    keyboard.press('p')
    keyboard.release('p')
    time.sleep(0.1)
    shop.shopOne()
    pyautogui.moveTo(860, 516, duration = 0.1)
    time.sleep(0.1)
    shop.shopTwo()
    time.sleep(0.1)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

def playGame():
    time.sleep(1)
    playing = True
    while playing:
        shopping()
        yummiQ()
        yummiW()
        #yummiE()
        yummiSums()
        levelUp()
        checkDead()
        yummiR()
        time.sleep(3)





playGame()
