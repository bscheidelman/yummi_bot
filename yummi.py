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
    print("q")
    if locateEnemy() != None:
        try:
            checkCD = pyautogui.locateOnScreen('qbase.png')
            checkCD = pyautogui.center(checkCD)
            li = locateEnemy()
            pyautogui.moveTo(li[0]+48, li[1]+70, duration = 0.04)
            time.sleep(0.05)
            keyboard.press('q')
            keyboard.release('q')
            tick = 10
            print('hi')
            while tick > 0:
                try:
                    li = locateEnemy()
                    pyautogui.moveTo(li[0]+48, li[1]+70, duration = 0.04)
                except:
                    break
                print(tick)
                tick -= 1
        except:
            print("q on cd")


def yummiW():
    print("w")
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

                time.sleep(0.1)
                shopping()          
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
    print("e")
    pyautogui.moveTo(1450, 709, duration = 0.1)
    shop.shopOne()


    val = findRGB(603, 168)
    if val == (1, 13, 7):
        keyboard.press('e')
        keyboard.release('e')


def yummiR():
    print("r")
    nli = locateEnemy()
    if nli != None:
        if (nli[0] > r1 and nli[0] < r2) and (nli[1] > r3 and nli[1]< r4):
            try:
                checkCD = pyautogui.locateOnScreen('rbase.png')
                #checkCD = pyautogui.center(checkCD)
                #print("ulting")
                #pyautogui.moveto(enemyLoc.x,enemyLoc.y, 3)
                #time.sleep(10)
                pyautogui.moveTo(nli[0]+48, nli[1]+48, duration = 0.04)
                keyboard.press('r')
                keyboard.release('r')
                time.sleep(2.75)

            except:
                print(" r on cd")
            
def levelUp():
    print("lvl")
    lvlOrder = ["r","q","e","w"]
    for val in lvlOrder:
        with keyboard.pressed(Key.ctrl):
            keyboard.press(val)
            keyboard.release(val)

def yummiSums():
    print('sums')
    pyautogui.moveTo(1450, 709, duration = 0.1)
    shop.shopOne()


    val = findRGB(653, 176)
    if val == (1, 13, 7):
        keyboard.press('f')
        keyboard.release('f')


    #Ignite
    nli = locateEnemy()
    if nli != None:
        if (nli[0] > 708 and nli[0] < 1092) and (nli[1] > 380 and nli[1]< 751):
            pyautogui.moveTo(nli[0]+48, nli[1]+70, duration = 0.04)
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

def startOfGame():
    side = ""
    try:
        sideFind = pyautogui.locateOnScreen('nexus.png')
        sideFind = pyautogui.center(sideFind)
        side = "red"
    except:
        side = "blue"
    side = "red"

    global r1
    global r2
    global r3
    global r4
    if side == "red":
        r1 = 808
        r2 = 1092
        r3 = 480
        r4 = 751
    else:
        r1 = 708
        r2 = 1092
        r3 = 380
        r4 = 751
    print(side)

def playGame():
    time.sleep(1)
    startOfGame()

    playing = True
    while playing:
        
        shopping()
        yummiQ()
        yummiW()
        yummiE()
        yummiSums()
        levelUp()
        yummiR()
        time.sleep(0.1)


playGame()
