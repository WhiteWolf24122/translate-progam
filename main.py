import translators as ts
import keyboard as ky
import pyautogui as pya
import pyperclip
import time
import tkinter as tk



ky.add_hotkey("alt + n", lambda: translate())

def translate():
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

    window.wm_attributes("-topmost", 1)
    window.geometry(f"{len(val)*7}x50+{(pya.position().x-150)}+{(pya.position().y)-150}")
    window.title("Translation -> EN")
    window.after(15000, lambda: window.destroy())
    window.mainloop()

ky.wait("ctrl + alt + shift + esc")