import pyautogui
from time import sleep
def browser():
    pyautogui.press('winleft')
    sleep(0.5)
    pyautogui.press('down')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)


def ataque():
    pyautogui.press('F5')
    sleep(2)
    pyautogui.moveTo(x=809, y=1003)
    sleep(0.5)
    pyautogui.click()
    sleep(10)


def contador():
    pyautogui.moveTo(x=869, y=307)
    sleep(1)
    pyautogui.moveTo(x=869, y=358)
    sleep(0.5)
    pyautogui.click()
