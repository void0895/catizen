import pyautogui as puto


def add(x, y, target_x, target_y):
    puto.moveTo(x, y)
    puto.click()
    puto.mouseDown()
    puto.dragTo(target_x, target_y, duration=1)
    puto.mouseUp()
