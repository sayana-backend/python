import pyautogui
import threading
from pynput import keyboard

is_clicking = False

def click_mouse():
    global is_clicking
    while is_clicking:
        pyautogui.doubleClick()

def on_press(key):
    global is_clicking
    try:
        if key.char.lower() in ['c', 'c']:
            if not is_clicking:
                is_clicking = True
                threading.Thread(target=click_mouse).start()
            else:
                is_clicking = False
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

