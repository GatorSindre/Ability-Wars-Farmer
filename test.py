import pyautogui
import time
import keyboard

keyboard.wait("o")

time.sleep(0.5)

for char in "twp here":
    pyautogui.press(char)
    time.sleep(0.3)

time.sleep(0.5)
keyboard.press_and_release("enter")