import time
import pyautogui

STEP = 0.135

START_DELAY = 1.0

pyautogui.PAUSE = 0
#pyautogui.FAILSAFE = False

def entry():
    pyautogui.press("right")
    time.sleep(STEP*6)
    pyautogui.press("down")
    time.sleep(STEP*4)

def rightDown():
    time.sleep(STEP*7)
    pyautogui.press("right")
    time.sleep(STEP)
    pyautogui.press("down")
def rightUp():
    time.sleep(STEP*7)
    pyautogui.press("right")
    time.sleep(STEP)
    pyautogui.press("up")

def cycle():
    pyautogui.press("left")
    time.sleep(STEP*9)
    pyautogui.press("up")

    time.sleep(STEP*8)
    pyautogui.press("right")
    time.sleep(STEP)
    pyautogui.press("down")

    rightUp()
    rightDown()
    rightUp()
    rightDown()
    rightUp()
    rightDown()
    rightUp()
    rightDown()
    time.sleep(STEP*8)

GAME_OVER_PIXEL = (1138, 328)  # Replace with a pixel that changes on Game Over
GAME_OVER_COLOR = (77, 193, 249)  # Replace with the color you see on Game Over

def is_game_over():
    return pyautogui.pixelMatchesColor(GAME_OVER_PIXEL[0], GAME_OVER_PIXEL[1], GAME_OVER_COLOR)

def beat_snake():
    while True:
        pyautogui.click(1282, 692)  # Click Play
        entry()
        while not is_game_over():
            cycle()
        print("Game over! Restarting...")
        time.sleep(0.5)


beat_snake()
import time
import pyautogui

STEP = 0.135

START_DELAY = 1.0

pyautogui.PAUSE = 0
#pyautogui.FAILSAFE = False

def entry():
    pyautogui.press("right")
    time.sleep(STEP*6)
    pyautogui.press("down")
    time.sleep(STEP*4)

def rightDown():
    time.sleep(STEP*7)
    pyautogui.press("right")
    time.sleep(STEP)
    pyautogui.press("down")
def rightUp():
    time.sleep(STEP*7)
    pyautogui.press("right")
    time.sleep(STEP)
    pyautogui.press("up")

def cycle():
    pyautogui.press("left")
    time.sleep(STEP*9)
    pyautogui.press("up")

    time.sleep(STEP*8)
    pyautogui.press("right")
    time.sleep(STEP)
    pyautogui.press("down")

    rightUp()
    rightDown()
    rightUp()
    rightDown()
    rightUp()
    rightDown()
    rightUp()
    rightDown()
    time.sleep(STEP*8)

def beat_snake():
    pyautogui.click(1282, 692)
    entry()
    while True:
        cycle()

beat_snake()
