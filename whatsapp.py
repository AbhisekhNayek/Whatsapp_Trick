import pyautogui
import time
time.sleep(4)
count =1
while count<=50:
    pyautogui.typewrite("Type Your Text...")
    pyautogui.press("enter")
    count=count + 1
