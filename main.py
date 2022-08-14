import translators as ts
import keyboard as ky
import pyautogui as pya
import pyperclip
import time
import tkinter as tk



ky.add_hotkey("alt + n", lambda: translate())

def translate():
    time.sleep(.3)
    pya.tripleClick(pya.position())
    time.sleep(.1)

    ky.press_and_release("ctrl + c")
    time.sleep(.1)

    val = pyperclip.paste()
    val = val.replace("\n", "")
    window(ts.google(val))

def window(val):
    window = tk.Tk()
    value = tk.Label(text=val)
    value.pack()

    window.overrideredirect(True)
    window.wm_attributes("-topmost", 1)
    window.geometry(f"{(len(val)*6)+15}x30+{(pya.position().x-150)}+{(pya.position().y)-40}")
    window.title("Translation -> EN")
    window.after(3500, lambda: window.destroy())
    window.mainloop()

ky.wait("ctrl + alt + shift + esc")