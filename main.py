import random
import time
import keyboard
import mouse


def loop():
    time.sleep(3)
    while True:
        time.sleep(random.uniform(.1, .2))
        keyboard.press("4")
        time.sleep(random.uniform(.2, .6))
        mouse.click(button="left")
        time.sleep(random.uniform(.8, 1)) # at inventory
        mouse.click(button="left")
        time.sleep(random.uniform(1.9,2.2))


if __name__ == '__main__':
    loop()
