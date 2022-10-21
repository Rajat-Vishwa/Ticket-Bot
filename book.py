import pyautogui
import time

name = 'Rajat V'
age = '18'

def execute():
    pyautogui.click()
    pyautogui.typewrite(name)
    pyautogui.press('tab')
    pyautogui.typewrite(age)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.scroll(-750)
    time.sleep(0.1)
    
def executeAddress():
    pyautogui.click()
    pyautogui.typewrite('Gram Beohara')
    pyautogui.press('tab')
    pyautogui.typewrite('Post Beohara')
    pyautogui.press('tab')
    pyautogui.typewrite('Lalganj')
    pyautogui.press('tab')
    pyautogui.typewrite('276202')
    pyautogui.press('tab',presses=3,interval=0.1)
    time.sleep(0.1)
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')

def searchAddress():
    adLoc = pyautogui.locateOnScreen('address.PNG')
    if adLoc == None:
        searchAddress()
    else:
        pyautogui.moveTo(adLoc)
        executeAddress()
        return

def searchName():
    loc = pyautogui.locateOnScreen('name.PNG')
    if loc == None:
        searchName()
    else:
        pyautogui.moveTo(loc)
        execute()
        return

def searchPay():
    pyautogui.scroll(-500)
    time.sleep(0.1)
    payLoc = pyautogui.locateOnScreen('pay.PNG')
    if payLoc == None:
        searchPay()
    else:
        pyautogui.moveTo(payLoc,duration=0.1)
        pyautogui.click()

def countin():
    conLoc = pyautogui.locateOnScreen('continue.PNG')
    if conLoc == None:
        countin()
    else:
        pyautogui.moveTo(conLoc)
        pyautogui.click()

def con():
    Loc = pyautogui.locateOnScreen('confirmCheck.PNG')
    if Loc == None:
        con()
    else:
        pyautogui.moveTo(Loc)
        pyautogui.click()
    
def anc():
    Loc = pyautogui.locateOnScreen('anchor.PNG')
    if Loc == None:
        anc()
    else:
        pyautogui.scroll(-200)
        time.sleep(0.3)


def pay():
    Loca = pyautogui.locateOnScreen('card.PNG')
    if Loca == None:
        pay()
    else:
        pyautogui.moveTo(Loca)
        pyautogui.click()
        pyautogui.typewrite('4346586967023451')

anc()
while True:
    searchName()
    con()
    searchAddress()
    pay()
    break