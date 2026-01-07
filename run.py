import time
import keyboard
import os
import subprocess
import pyautogui
import sys


## Put gator oppe til venstre og potato nede til venstre og alts til høyre
## +waypoint alts   healing
## +waypoint gator  army    summon army spot
## +waypoint gator  default     punching spot
## +waypoint alts   look_set
## +waypoint alts   get_punched

alt1Navn = "tomtatohandye"

total_score = 0

gator_yield = (484, 111)
## Focus offset of this is y - 60
gator_focus = (484, 111 - 60)
gator_e = (92, 452)

potato_yield = (487, 627)
potato_focus = (487, 627 - 60)

alt1_yield = (1446, 113)
alt1_focus = (1446, 113 - 60)

on_screen_enter = (1650, 832)

## Army ability
ability_cooldown = 35

focus_cooldown = 1
yield_cooldown = 0.4
tween_cooldown = 2
enter_cooldown = 0.2
key_cooldown = 0.4
type_cooldown = 0.05
wait_for_kill = 15
wait_for_rejoin = 25
walk_til_tp = 0.7

def punch():
    pyautogui.click(*gator_focus)
    time.sleep(focus_cooldown)

    pyautogui.click(*gator_yield)
    time.sleep(yield_cooldown)

    for char in "twp default":
        pyautogui.press(char)
        time.sleep(type_cooldown)
    time.sleep(type_cooldown)
    keyboard.press_and_release("enter")
    time.sleep(tween_cooldown)


    pyautogui.click(*alt1_focus)
    time.sleep(focus_cooldown)

    pyautogui.click(*alt1_yield)
    time.sleep(yield_cooldown)

    for char in "twp look_set":
        pyautogui.press(char)
        time.sleep(type_cooldown)
    time.sleep(type_cooldown)
    keyboard.press_and_release("enter")
    time.sleep(yield_cooldown)


    pyautogui.click(*gator_focus)
    time.sleep(focus_cooldown)

    pyautogui.click(*gator_yield)
    time.sleep(yield_cooldown)

    for char in f"lookat {alt1Navn}":
        pyautogui.press(char)
        time.sleep(type_cooldown)
    time.sleep(type_cooldown)
    keyboard.press_and_release("enter")
    time.sleep(focus_cooldown)

    for i in range(3):
        pyautogui.press("o")
        time.sleep(0.3)

    pyautogui.click(*gator_e)
    time.sleep(1)

    pyautogui.click(*gator_yield)
    time.sleep(yield_cooldown)


    pyautogui.click(*alt1_focus)
    time.sleep(focus_cooldown)

    pyautogui.click(*alt1_yield)
    time.sleep(yield_cooldown)

    for char in "twp get_punched":
        pyautogui.press(char)
        time.sleep(type_cooldown)
    time.sleep(type_cooldown)
    keyboard.press_and_release("enter")
    time.sleep(tween_cooldown)

    pyautogui.click(*gator_focus)
    time.sleep(focus_cooldown)

    #punch
    pyautogui.click(*gator_focus)
    time.sleep(0.3)
    
    #punch
    pyautogui.click(*gator_focus)
    time.sleep(1)

def new():
    global total_score


    pyautogui.click(*alt1_focus)
    time.sleep(focus_cooldown)

    pyautogui.click(*alt1_yield)
    time.sleep(yield_cooldown)

    for char in "twp get_punched":
        pyautogui.press(char)
        time.sleep(type_cooldown)
    time.sleep(type_cooldown)
    keyboard.press_and_release("enter")
    time.sleep(tween_cooldown)

    pyautogui.click(*gator_focus)
    time.sleep(focus_cooldown)

    pyautogui.click(*gator_yield)
    time.sleep(yield_cooldown)

    for char in "twp default":
        pyautogui.press(char)
        time.sleep(type_cooldown)
    time.sleep(type_cooldown)
    keyboard.press_and_release("enter")
    time.sleep(tween_cooldown)

    pyautogui.click(*gator_e)
    time.sleep(focus_cooldown)


    pyautogui.mouseDown(655, 97)
    time.sleep(0.1)
    pyautogui.mouseUp

    pyautogui.mouseDown(108, 133)
    time.sleep(0.1)
    pyautogui.mouseUp

    time.sleep(wait_for_kill)

    total_score += 1
    print(total_score)

    pyautogui.click(*alt1_focus)
    time.sleep(focus_cooldown)

    pyautogui.click(*alt1_yield)
    time.sleep(yield_cooldown)

    for char in "rj":
        pyautogui.press(char)
        time.sleep(type_cooldown)
    time.sleep(type_cooldown)
    keyboard.press_and_release("enter")
    time.sleep(yield_cooldown)


    pyautogui.click(*gator_focus)
    time.sleep(focus_cooldown)

    pyautogui.click(*gator_yield)
    time.sleep(yield_cooldown)

    for char in "twp escape":
        pyautogui.press(char)
        time.sleep(type_cooldown)
    time.sleep(type_cooldown)
    keyboard.press_and_release("enter")
    time.sleep(yield_cooldown)

    time.sleep(wait_for_rejoin)


    pyautogui.click(*alt1_focus)
    time.sleep(focus_cooldown)

    pyautogui.click(1789, 73)
    time.sleep(yield_cooldown)

    pyautogui.click(*alt1_focus)
    time.sleep(focus_cooldown)

    keyboard.press("s")
    time.sleep(walk_til_tp)
    keyboard.release("s")

    pyautogui.click(*alt1_yield)
    time.sleep(yield_cooldown)

    for char in "goto steve":
        pyautogui.press(char)
        time.sleep(type_cooldown)
    time.sleep(type_cooldown)
    keyboard.press_and_release("enter")
    time.sleep(tween_cooldown)

    pyautogui.click(418, 596)
    time.sleep(focus_cooldown)

def setup():
    while True:
        new()
        time.sleep(2)
    
def scoreCheck():
    print(total_score)

def test():
    time.sleep(2)
    print("testing")
    keyboard.press("s")
    time.sleep(walk_til_tp)
    keyboard.release("s")
keyboard.on_press_key("k", lambda e: test())


## Start controls
keyboard.on_press_key("o", lambda e: sys.exit())
print("sys exiting")
keyboard.on_press_key("u", lambda e: setup())
print("setup started")
keyboard.on_press_key("i", lambda e: scoreCheck())

keyboard.wait("esc")