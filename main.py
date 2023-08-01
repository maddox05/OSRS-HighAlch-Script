import random
import time
import pyautogui


hotkey = "esc" # select hotkey

def loop():
    time.sleep(3)
    while True:
        time.sleep(random.uniform(.1, .2))
        pyautogui.press(hotkey)
        time.sleep(random.uniform(.2, .6))
        pyautogui.click(button="left")
        time.sleep(random.uniform(.8, 1)) # at inventory
        pyautogui.click(button="left")
        time.sleep(random.uniform(1.9,2.2))


if __name__ == '__main__':
    loop()
