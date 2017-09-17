import pyautogui
import time
if __name__ == '__main__':
    while True:
        x, y = pyautogui.position()
        # x, y = pyautogui.displayMousePosition()
        print("X : {0}\tY : {1}".format(x, y))
        print(input())
        pyautogui.moveTo(428, 184)
        time.sleep(5)