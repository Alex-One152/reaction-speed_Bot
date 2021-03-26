import pyautogui
import time
import cv2
import mss
import numpy as np

sct = mss.mss()

print("Жду зелёный")

while True:

    def queryMousePosition():
        pt = pyautogui.position()
        return {"x": pt.x, "y": pt.y}
    cur = queryMousePosition()
    y = cur['y']
    x = cur['x']
    mon = {"top":  y - 3, "left": x - 3, "width": 3, "height": 3}
    img = np.sum(np.array(sct.grab(mon)))

    green = 5652

    black_green = 3636
    yellow = 6120

    if img == green:
        pyautogui.click()
        print("Клик !!!")

    if img == black_green:
        print("Отдыхаю две секунды")
        time.sleep(2)
        pyautogui.click()
