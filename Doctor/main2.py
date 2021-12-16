from importlib import import_module
import os
import pyautogui

for i in range(1,11):
    pyautogui.keyDown('Enter')
    pyautogui.write(f"{i}")