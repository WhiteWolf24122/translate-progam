import translators as ts
import keyboard as ky


def epic():
    print("epic")

ky.add_hotkey("shift + a", lambda: epic())

ky.wait("alt + shift + esc")