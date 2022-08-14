import translators as ts
import keyboard as ky
import pyautogui as pya
import pyperclip
import time
import tkinter as tk
import json

languages = []
with open("langs.json") as file:
    parsed = json.loads(file.read())

for i in parsed:
    languages.append(i)

ky.add_hotkey("alt + n", lambda: translate())
ky.add_hotkey("alt + t", lambda: trans_to())

def translate():
    time.sleep(.3)
    pya.tripleClick(pya.position())
    time.sleep(.1)

    ky.press_and_release("ctrl + c")
    time.sleep(.1)

    val = pyperclip.paste()
    val = val.replace("\n", "")
    window(ts.google(val))


def trans_to():
    window = tk.Tk()

    clicked = tk.StringVar()
    clicked.set("English")

    drop = tk.OptionMenu(window, clicked, *languages)
    drop.pack()

    text = tk.Text(width=200, height=3)
    text.pack()

    button = tk.Button(window, text="Translate", command= lambda: tras(text.get("1.0", tk.END), clicked.get())).pack()
    button = tk.Button(window, text="Close", command= lambda: window.destroy()).pack()

    window.overrideredirect(True)
    window.wm_attributes("-topmost", 1)
    window.geometry(f"300x150+{(pya.position().x-150)}+{(pya.position().y)-40}")
    window.title(f"Translation -> {clicked.get()}")
    window.mainloop()

def tras(val, lang_long):
    val = val.replace("\n", "")

    with open("langs.json") as file:
        parsed = json.loads(file.read())
    
    value = ts.google(val, to_language=parsed[lang_long])
    pyperclip.copy(value)


    w = tk.Tk()
    lab = tk.Label(w, text="Translated and Copyed to clipbaord").pack()
    w.overrideredirect(True)
    w.wm_attributes("-topmost", 1)
    w.geometry(f"200x50+{(pya.position().x-150)}+{(pya.position().y)-40}")
    w.title(f"Translation -> {lang_long}")
    w.after(1500, lambda: w.destroy())
    w.mainloop()

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