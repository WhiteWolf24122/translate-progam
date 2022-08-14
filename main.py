import translators as ts
import keyboard as ky
import pyautogui as pya
import pyperclip
import time



ky.add_hotkey("alt + t", lambda: copy())

def copy():
    pya.tripleClick(pya.position())
    time.sleep(1)

    ky.press_and_release("ctrl + c")
    time.sleep(.1)

    val = pyperclip.paste()
    val = val.replace("\n", "")
    
    print(val)

ky.wait("ctrl + alt + shift + esc")