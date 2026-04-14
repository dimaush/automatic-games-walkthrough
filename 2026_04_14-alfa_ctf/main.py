import pyautogui as pag
from time import sleep


def click(x, y):
    pag.moveTo(x, y, 0.4)
    sleep(0.1)
    pag.click()


click(1250, 400) # exit from console

while True:
    click(410, 800) # burger button
    click(410, 750) # /offline command
    sleep(2)
    click(520, 600) # Moscow, but 600->670 - Financial University
    sleep(2)
    click(520, 705) # approve, but 520->490 - link /offline in message text
